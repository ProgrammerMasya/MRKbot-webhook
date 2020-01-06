
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
            vk_obj.send_message(person_id, "Всем привет, хочу познакомить Вас с одним человеком!\n\n Его зовут Илья. "
                                           "Активно работает над различными проектиками, много кодит и в целом живёт "
                                           "профессией программиста! Разрабатывает open source библиотеку для "
                                           "Яндекс.Музыки, пишет статьи на Habr, когда есть о чем, сейчас разрабатывает "
                                           "бота для Telegram, реализующий функционал приложения Яндекс музыки. Не стоит "
                                           "на месте, прокачивает себя, использует современные технологии!\n\n Несколько "
                                           "месяцев назад он завёл Telegram-канал, где делится своими успехами, делами и "
                                           "рассказывает интересные вещи. Иногда проводит розыгрыши среди подписчиков. "
                                           "Канал ушел в слишком серьезную тему не для всех, поэтому сейчас он разбавляет "
                                           "его простыми постиками, просто делиться полезной, так и нет, информацией с "
                                           "другими ✨\n\n Вот его канал: https://t.me/MarshalC", '')
        except:
            pass


def main():
    send_auto_rasp()


if __name__ == '__main__':
    main()
