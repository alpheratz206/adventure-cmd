import mariadb

conn = mariadb.connect(
    host="localhost",
    database="Adventure")
cur = conn.cursor() 

cur.execute("SELECT Description FROM State") 

for Description in cur: 
    print(f"State description: {Description}")