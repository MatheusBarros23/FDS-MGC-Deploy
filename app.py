from flask import Flask
from flask_mysqldb import MySQL

from prepara_banco import prepara_banco

app = Flask(__name__)
app.config.from_pyfile('config.py')
db = MySQL(app)

from views import *

#executo o bd antes!
prepara_banco()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)

