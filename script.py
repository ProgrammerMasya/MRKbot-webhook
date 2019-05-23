
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
        try:
            a = str(person_data[0]).replace("(","").replace(")","").replace(",","")
            person_id = a
            vk_obj.send_message(person_id, "Прошёл первый день MRCConf. "
                                           "🔥Было много ярких эмоций и по "
                                           "просьбе аудитории мы прикрепляем "
                                           "презентацию Дениса Тамковича, "
                                           "Middle Python Engineer из "
                                           "EPAM Systems 🎁\n"
                                           "https://vk.com/tmkkkv\n\n"
                                           "https://docs.google.com/pr"
                                           "esentation/d/1p8-tPvpNTgetJeOLi"
                                           "Tei6l0cW5mO5fKcA8UI6AxDMvM/edit"
                                           "#slide=id.p", '')
        except:
            pass


def main():
    send_auto_rasp()


if __name__ == '__main__':
    main()