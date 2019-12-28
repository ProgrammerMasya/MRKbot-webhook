from settings import *
from app.db.db import DB


db_obj = DB(
    "dbname='masya' "
    f"user='{config['db_user']}' "
    f"host='{config['db_host']}' "
    f"password='{config['db_password']}'"
)


def get_data():
    return db_obj.get_all()


def write_in_txt():
    data = get_data()
    f = open('db.txt', 'w')
    for person_data in data:
        f.write(str(person_data) + '\n')

write_in_txt()
