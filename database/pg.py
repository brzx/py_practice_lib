import psycopg2 as pg

conn = pg.connect(database="work", user="postgres", password="123123", host="127.0.0.1", port="5432")
cur = conn.cursor()
cur.execute("select * from analysis_view limit 3;")
rows = cur.fetchall()
for i in rows:
    print(i)

cur.close
conn.close
