from flask import Flask
import mysql.connector
import os

app = Flask(__name__)

def menu():
    return """
    <a href="/">Homepage</a> <a href="/autrepage">Autre page</a> 
    """

def getdb():
    return {
        'host': os.environ.get('DB_HOST'),
        'user': "root",
        'password': os.environ.get('DB_PASS'),
        'database': "pyapp",
    }

def visites() -> int:
    count = 0
    with mysql.connector.connect(**getdb()) as db :
        with db.cursor() as c:
            c.execute("SELECT compteur FROM compteur")
            resultats = c.fetchall()
            (count,) = resultats[0]
    return count

def add_visit():
    with mysql.connector.connect(**getdb()) as db :
        with db.cursor() as c:
            c.execute("UPDATE compteur SET compteur = compteur + 1")
            db.commit()

@app.route("/")
def homepage():
    print(getdb())
    add_visit()
    count = str(visites())
    return "<h1>Démo app</h1>" + menu() + " <p>home page</a> <p>nombre de visites : " + count + "</p>"

@app.route("/autrepage")
def autrepage():
    return "<h1>Démo app</h1>" + menu() + " <p>une autre page</p>"
