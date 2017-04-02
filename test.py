import psycopg2


conn=psycopg2.connect('dbname=postgres user=postgres host=localhost port=5439')
cursor=conn.cursor()
cursor.execute('select count(id) from gaode.spois')
print cursor.fetchone()[0]