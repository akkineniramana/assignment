  
from typing import List, Dict
from flask import Flask
import mysql.connector
import json
import os

app = Flask(__name__)


def get_user() -> List[Dict]:
    password =  os.getenv("database_password") or "root"
    host = os.getenv("database_name") or "mysql"
    database = os.getenv("MYSQL_SERVICE_HOST") or "api"
    port = os.getenv("MYSQL_SERVICE_PORT") or '3306'
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
    cursor.execute('SELECT * FROM users')
    results = [{"user": name} for name in cursor]
    cursor.close()
    connection.close()

    return results


@app.route('/')
def index() -> str:
    return json.dumps({'user': get_user()})


if __name__ == '__main__':
    app.run(host='0.0.0.0')