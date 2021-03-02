  
from typing import List, Dict
from flask import Flask
import mysql.connector
import json
import os

app = Flask(__name__)


def get_user() -> List[Dict]:
    password =  os.getenv("DB_PASSWORD") or "root"
    host = os.getenv("DB_HOSTNAME") or "mysql"
    database = os.getenv("DB_NAME") or "api"
    port = os.getenv("DB_PORT") or '3306'
    config = {
        'user': 'root',
        'password': password,
        'host': host,
        'port': port,
        'database': database
    }
    print("config ", config)
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM users LIMIT 1')
    results = [name for name in cursor]
    cursor.close()
    connection.close()

    return results[0]


@app.route('/')
def index() -> str:
    return "hello user : {}".format(get_user())


if __name__ == '__main__':
    app.run(host='0.0.0.0')