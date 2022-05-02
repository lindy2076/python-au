from random import randint
import requests
import vk_api
from PIL import Image
from hashlib import sha256
from os import remove


def random_int():
    return randint(1,10000)


def check_token(token):
    try:
        session = vk_api.VkApi(token=token)
        session2 = vk_api.upload.VkUpload(session)
        method = session2.vk.docs.getWallUploadServer
        url = method()['upload_url']
        return 1
    except Exception as wtf:
        return 0

    
def hash_token(token):
    res = sha256(token.encode('utf-8'))
    return res.hexdigest()


def iter_frames(im):  #https://stackoverflow.com/questions/61958291/gifs-read-with-pillow-have-black-borders
    disposal_method_last = 0
    duration = 0
    try:
        i= 0
        while 1:
            im.seek(i)
            duration = im.info['duration']
            print(i, duration)
            disposal_method = disposal_method_last
            disposal_method_last = im.__dict__.get('disposal_method', 0)
            if disposal_method == 2 or (disposal_method == 1 and i == 0):
                imframe = Image.new('RGBA', im.size, color=(255,0,0,0))
                imframe.paste(im.crop(im.dispose_extent), box=(im.dispose_extent[0],im.dispose_extent[1]))
            elif disposal_method == 1 and i!=1:
                newStuff = im.crop(im.dispose_extent)
                im.seek(i-1)
                imframe = im.copy()
                im.seek(i)
                imframe.paste(newStuff, im.dispose_extent, newStuff.convert("RGBA"))
            else:
                imframe = im.copy()
            yield imframe, duration
            i += 1
    except EOFError:
        pass


def save_pics(img_path, _id):
    im = Image.open(img_path)
    k = 0
    d = 0
    for frame, duration in iter_frames(im):
        frame.convert(mode='RGBA').save('temp/frames/' + str(k) + '_' + _id + '.png')
        d += duration
        k += 1
    print('done')
    d = int(d / k)
    return k, d


def join_apng(n, durations, _id):
    files = []
    for i in range(n):
        files.append(Image.open('temp/frames/' + str(i) + '_' + _id + '.png'))
    files[0].save('temp/' + _id + '_temp.png', save_all=True, append_images=files[0:], duration=durations, loop=0, format="PNG")
    for i in range(n):
        remove('temp/frames/' + str(i) + '_' + _id + '.png')
    print('done')


def convert_gif(path, _id):
    n, avg_dur = save_pics(path, _id)
    join_apng(n, avg_dur, _id)
    return 1


def request_img(url, _id=""):
    good_mimes = ['image/png', 'image/gif', 'image/x-png']
    try:
        image = requests.get(url, stream=True)
        image_mime = image.headers['Content-Type']
    except Exception as wtf:
        print('pic loading failed' + str(wtf.__class__))
        return 'проверьте ссылку...', 0
    else:
        if image.ok and image_mime in good_mimes:
            print('ok')
            temp_file = 'temp/' + _id + '_temp.png'
            with open(temp_file, 'wb') as handle:
                for block in image.iter_content(1024):
                    if not block:
                        break
                    handle.write(block)
            if image_mime == 'image/gif':
                convert_gif(temp_file, _id)
            return 'картинка по ссылке загрузилась на сервер!', 1
        else:
            res = 'формат картинки не пнг и не гиф...', 0
            print('fuck.')
    return res


def save_img(pic_file, _id):
    res = 'nil', 0
    pic_file_mime = pic_file.mimetype
    if pic_file_mime in ['image/png', 'image/gif', 'image/x-png']:
        temp_file = 'temp/' + _id + '_temp.png'
        with open(temp_file, 'wb') as handle:
            content = pic_file.read(1024)
            while content:
                handle.write(content)
                content = pic_file.read(1024)
        if pic_file_mime == 'image/gif':
            convert_gif(temp_file, _id)
        res = 'картинка с компьютера загрузилась на сервер!', 1
    else:
        res = 'формат файла не гиф и не пнг...', 0
    return res


def vk_send_message(token, peer_id, doc_id, doc_owner, randint_):
    session = vk_api.VkApi(token=token)
    try:
        res = session.method("messages.send", {
            'random_id': randint_,
            'peer_id': peer_id,
            'attachment': 'doc' + str(doc_owner) + '_' + str(doc_id)
        })
    except Exception as wtf:
        print('failed ' + str(wtf.__class__))
        return 'failure'
    return res


def vk_graffiti_upload(token):
    session = vk_api.VkApi(token=token)
    temp_file = 'temp/' + hash_token(token) + '_temp.png'
    session2 = vk_api.upload.VkUpload(session)
    values = {
        'group_id': None,
        'peer_id': None,
        'type': 'graffiti'
    }
    try:
        method = session2.vk.docs.getWallUploadServer
        url = method(**values)['upload_url'] # ссылку для загрузки получаем
    except Exception as wtf:
        return 'invalid token idk ' + str(wtf.__class__)
    response = requests.post(url, files={'file': open(temp_file, 'rb')}).json() # работаем
    print(response)
    try:
        res = session2.vk.docs.save(**response)
    except Exception as wtf:
        return 'invalid file format probably ' + str(wtf.__class__)
    print(res) # очень хорошо

    doc_info = res['graffiti']

    print(doc_info['id'], doc_info['owner_id'], doc_info['url'])
    return doc_info['id'], doc_info['owner_id']


def vk_upload_and_send(token, peer_id, randint_):
    session = vk_api.VkApi(token=token)
    doc_id, doc_owner = vk_graffiti_upload(session)

    try:
        s = vk_send_message(session, peer_id, doc_id, doc_owner, randint_)
    except Exception as wtf:
        return 'invalid id or no permission to send messages ' + str(wtf.__class__)
    print('message_id:', s)
    return s


def vk_doc_info(token, doc_id, doc_owner):
    session = vk_api.VkApi(token=token)
    res = session.method("docs.getById", {
        'docs': doc_owner + "_" + doc_id
    })
    return res


def vk_get_doc_link(token, doc_id, doc_owner):
    data = vk_doc_info(token, doc_id, doc_owner)
    try:
        link = data[0]['url']
        return link
    except Exception as wtf:
        print('vk_get_doc_link ' + str(wtf.__class__))
        return 0


if __name__ == '__main__':
    n, avg_dur = save_pics('test2.gif')
    join_apng(n, avg_dur)
