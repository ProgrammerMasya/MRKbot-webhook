import command_system
import psycopg2
from settings import *
conn = psycopg2.connect(
    "dbname='masya' "
    f"user='{config['db_user']}' "
    f"host='{config['db_host']}' "
    f"password='{config['db_password']}'"
)

cursor = conn.cursor()


def autorasp(user_id, content):

    if content in [
        '8к1191', '8к1591', '8к1391', '8к1111', '7к1191', '7к1591',
        '7к1391', '61391', '8к2491', '8к2492', '8к2493', '7к2491',
        '7к2492', '7к2493', '8к2411', '7к2411', '62491', '8к3791',
        '8к3291', '7к3791', '7к3291', '7к1111', '61191', '61591',
        '61111', '62492', '62493', '62411', '63791', '63291', '9к9191',
        '9к9091', '9к9291', '9к9111', '9к9391', '9к9392', '9к9393',
        '9к9394', '9к9311', '9к9591', '9к9491'
    ]:
        cursor.execute(""" SELECT * FROM mrk WHERE vk_id=%s""", (user_id,))
        user_data = cursor.fetchone()
        if not user_data:
            cursor.execute(""" INSERT INTO mrk(vk_id, grupe) VALUES (%s, %s)""",
                           (user_id, content))
            conn.commit()
            message = "Подписка оформлена!"
        else:
            message = "Вы уже подписались на автоматическое расписание"

    elif content == 'stop':
        cursor.execute(""" DELETE FROM mrk WHERE vk_id=%s """, (user_id,))
        conn.commit()
        message = "Подписка отменена"


    else:
        message = "Указанной вами группы не существует"

    return message, "",


rasp_command = command_system.Command()

rasp_command.keys = ['/autorasp']
rasp_command.description = "Подписка на автоматическое расписание"
rasp_command.process = autorasp

