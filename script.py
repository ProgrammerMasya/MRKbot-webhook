
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
            vk_obj.send_message(person_id, "ДАМЫ И ГОСПОДА, ОБЯЗАТЕЛЬНО ЗАЙДИТЕ ВСЕ СЮДА И ЗАРЕГЕСТРИРУЙТЕСЬ! ТУТ ВСЯ ИНФА, ЧТО ТАКОЕ МРК КОНФ, О ЧЕМ ОН, ЧТО ТАМ БУДЕТ И КОГДА!\n\n"
                                           "https://mrcconf.github.io\n\n"
                                           "Максимально распространяйте!\n\n"
                                           "это будет ПУШКА КОНФЕРЕНЦИЯ 🤙🏻🤙🏻🤙🏻🤙🏻🤙🏻🤙🏻🤙🏻\n\n"
                                           "РАЗНЕСЕМ МРК МОТИВАЦИЕЙ И УСПЕХОМ 🤟🏻", '')
        except:
            pass


def main():
    send_auto_rasp()


if __name__ == '__main__':
    main()
