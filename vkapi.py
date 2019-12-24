import requests
import random
import json
import vk

session = vk.Session()
api = vk.API(session, v=5.0)


def send_message(user_id, token, message, attachment="", file=None):
    if file:
        _send_photo_with_doc(user_id, token, message, file)
    else:
        api.messages.send(
            access_token=token,
            user_id=str(user_id),
            message=message,
            attachment=attachment,
        )


def _save_photo(user_id, token, file):
    openedfile = open(file, "rb")
    files = {"file": openedfile}
    fileonserver = json.loads(
        requests.post(
            api.photos.getMessagesUploadServer(access_token=token)["upload_url"],
            files=files,
        ).text
    )
    attachment = api.photos.saveMessagesPhoto(
        access_token=token,
        server=fileonserver["server"],
        photo=fileonserver["photo"],
        hash=fileonserver["hash"],
    )
    openedfile.close()
    return f'photo{attachment[0]["owner_id"]}_{attachment[0]["id"]}'


def _save_doc(user_id, token):
    txt = open('mrk.txt')
    url = txt.readline()
    openedfile = open('rasp/rasp.pdf', "rb")
    files = {"file": openedfile}
    data = api.docs.getMessagesUploadServer(type='doc', peer_id=user_id, access_token=token)
    fileonserver = json.loads(
        requests.post(
            data["upload_url"],
            files=files,
        ).text
    )
    attachment = api.docs.save(
        access_token=token,
        file=fileonserver["file"],
        title=url.split('/')[4].split('.')[0],
        tags='MRK',
    )
    openedfile.close()
    return f'doc{attachment[0]["owner_id"]}_{attachment[0]["id"]}'


def _send_photo_with_doc(user_id, token, message, file):
    photo = _save_photo(user_id, token, file)
    pdf_file = _save_doc(user_id, token)
    attachments = [photo, pdf_file]
    if message:
        api.messages.send(
            access_token=token, user_id=user_id, message=message, attachment=attachments
        )
    else:
        api.messages.send(access_token=token, user_id=user_id, attachment=attachments)
