from consts import USERS_IMAGES_FULL
from app.model.vk.vk import Vk
from settings import *
from app.db.db import DB


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
    data = get_data()
    for person_data in data:
        person_id, group = person_data[0], person_data[1]
        file = USERS_IMAGES_FULL.get(group)
        vk_obj.send_message(person_id, "Получай", '', file)
