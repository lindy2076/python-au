import requests
import vk_api


def send_message(session, peer_id, doc_id, doc_owner, randint_):
    res = session.method("messages.send", {
        'random_id': randint_,
        'peer_id': peer_id,
        'attachment': 'doc' + str(doc_owner) + '_' + str(doc_id)
    })
    return res


def main(token, image_path, peer_id, randint_):
    image = requests.get(image_path, stream=True) # берем пихаем картинку в temp
    if image.status_code != 200:
        return 'invalid pic'

    temp_file = "temp/" + 'amogus.png'
    with open(temp_file, 'wb') as handle:  #FIXME вообще надо бы на размер и формат проверять файлики ну ладно
        for block in image.iter_content(1024):
            if not block:
                break
            handle.write(block)
    
    session = vk_api.VkApi(token=token)
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
    try:
        s = send_message(session, peer_id, doc_info['id'], doc_info['owner_id'], randint_)
    except Exception as wtf:
        return 'invalid id or no permission to send messages ' + str(wtf.__class__)
    print('message_id:', s)
    return s

if __name__ == '__main__':
    main(0,'https://psv4.userapi.com/c534536/u362519748/docs/d48/7ae32a43aec1/ezgif_com-gif-maker.png',0, 0)
