
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
            vk_obj.send_message(person_id, "Итак, по ссылке можно получить курс по купону, который "
                                           "даёт лучшую цену"
                                           "вот ссылка: https://www.udemy.com/course/business-python/?couponCode=EBANOEIT"
                                           "как раз в день стипендии \n"
                                           "благодарите за промокод сайт ebanoe.it и стипендию", '')
        except:
            pass


def main():
    send_auto_rasp()


if __name__ == '__main__':
    main()
