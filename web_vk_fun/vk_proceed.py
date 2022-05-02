import requests
import vk_api


def send_message(session, peer_id, doc_id, doc_owner, randint_):
    res = session.method("messages.send", {
        'random_id': randint_,
        'peer_id': peer_id,
        'attachment': 'doc' + str(doc_owner) + '_' + str(doc_id)
    })
    return res


def graffiti_upload(session):
    temp_file = "static/amogus.png"
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


def upload_and_send(token, peer_id, randint_):
    session = vk_api.VkApi(token=token)
    doc_id, doc_owner = graffiti_upload(session)

    try:
        s = send_message(session, peer_id, doc_id, doc_owner, randint_)
    except Exception as wtf:
        return 'invalid id or no permission to send messages ' + str(wtf.__class__)
    print('message_id:', s)
    return s

if __name__ == '__main__':
    print(upload_and_send(0, 2000000125, 10) )
