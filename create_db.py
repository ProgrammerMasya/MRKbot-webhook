import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from settings import *

def create_database():
    con = None
    con = psycopg2.connect(
    f"dbname='{config['db_name']}'"
    f"user='{config['db_user']}'"
    f"host='{config['db_host']}'"
    f"password='{config['db_password']}'"
)

    dbname = "masya"

    con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = con.cursor()
    cur.execute('CREATE DATABASE ' + dbname)
    con.commit()
    con = psycopg2.connect(
        "dbname='denis' "
        f"user='{config['db_user']}'"
        f"host='{config['db_host']}'"
        f"password='{config['db_password']}'"
    )
    cur = con.cursor()
    cur.execute("CREATE TABLE mrk (id SERIAL PRIMARY KEY, vk_id INTEGER, grupe CHARACTER VARYING(6))")
    con.commit()
    cur.close()
    con.close()


if __name__ == '__main__':
    create_database()