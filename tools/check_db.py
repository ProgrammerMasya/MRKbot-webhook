import psycopg2

con = psycopg2.connect(
        f"dbname='masya'"
        f"user='user_name'"
        f"host='68.183.75.150'"
        f"password='password'"
    )
cur = con.cursor()

cur.execute('SELECT COUNT(*) FROM mrk')
people = cur.fetchall()


print(people)
