from db_connection import get_conn_cursor


class DB:
    def __init__(self, conn_string):
        self.conn, self.cursor = get_conn_cursor(conn_string)

    def get_all(self):
        self.cursor.execute(""" SELECT vk_id, grupe FROM mrk""")
        return self.cursor.fetchall()

