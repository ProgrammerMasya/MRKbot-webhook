import psycopg2


def get_conn(conn_string):
    return psycopg2.connect(conn_string)


def get_conn_cursor(conn_string):
    conn = get_conn(conn_string)
    cursor = conn.cursor()
    return conn, cursor
