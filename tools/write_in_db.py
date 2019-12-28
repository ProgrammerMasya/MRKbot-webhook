from settings import *
import re
import psycopg2


conn = psycopg2.connect(
    "dbname='masya' "
    f"user='{config['db_user']}' "
    f"host='{config['db_host']}' "
    f"password='{config['db_password']}'"
)
curr = conn.cursor()


def write_in_db():
    f = open('db.txt', 'r')
    for person_data in f:
        a = int(re.search(r'(\w+)', person_data).group(1))
        b = re.search(r"('\w+')", person_data).group(1)
        c = b.strip("'")
        curr.execute(""" INSERT INTO mrk(vk_id, grupe) VALUES (%s, %s)""", (a, c))
        conn.commit()


write_in_db()
# curr.execute(""" SELECT vk_id, grupe FROM mrk""")
# aa = curr.fetchall()
# for a in aa:
#     print(a)
