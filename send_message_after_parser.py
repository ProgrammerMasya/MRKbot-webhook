from get_groups import extract_text
from app.model.vk.vk import Vk
from settings import *
from app.db.db import DB
import vk

USERS_IMAGES_FULL = extract_text('rasp/rasp.pdf')

db_obj = DB(
    "dbname='masya' "
    f"user='{config['db_user']}' "
    f"host='{config['db_host']}' "
    f"password='{config['db_password']}'"
)

vk_obj = Vk(config['token'])


def get_data():
    return db_obj.get_all()


def send_auto_rasp():
    users_images_full = extract_text('rasp/rasp.pdf')
    data = get_data()
    for person_data in data:
        try:
            person_id, group = person_data[0], person_data[1]
            file = users_images_full.get(group)
            vk_obj.send_message(person_id, "Получай", '', file)
        except:
            pass


