import time
import pymysql
import os

host = os.getenv("DJANGO_DB_HOST", "db")
port = int(os.getenv("DJANGO_DB_PORT", 3306))
user = os.getenv("DJANGO_DB_USER", "django")
password = os.getenv("DJANGO_DB_PASSWORD", "django")
db = os.getenv("DJANGO_DB_NAME", "djangodb")

while True:
    try:
        conn = pymysql.connect(host=host, port=port, user=user, password=password, database=db)
        conn.close()
        print("MySQL está disponible")
        break
    except pymysql.err.OperationalError:
        print("MySQL no disponible, esperando...")
        time.sleep(2)
