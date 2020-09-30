from flask import Flask, render_template, url_for, request, g, redirect
import sqlite3, os
from FDatabase import FDatabase


DATABASE = 'my.db'
DEBUG = True
SECRET_KEY = 'NOTIME'

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(DATABASE=os.path.join(app.root_path,'my.db')))

def connect_db():
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn

def create_db():
    db = connect_db()
    with app.open_resource('init-db.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()

def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return  g.link_db

@app.route('/', methods=['POST', 'GET'])
def index():
        return render_template("index.html")


@app.route('/users')
def users():
    db = get_db()
    dbase = FDatabase(db)
    return render_template("users.html", results = dbase.get_active())

@app.route('/logins', methods=['POST', 'GET'])
def logins():
    db = get_db()
    dbase = FDatabase(db)
    if request.method == "POST":
        login = request.form['login']
        return render_template("login.html", results = dbase.getlog(login))
    else:
        return render_template("login0.html")

@app.route('/id', methods=['POST', 'GET'])
def id():
    db = get_db()
    dbase = FDatabase(db)
    if request.method == "POST":
        id = request.form['id']
        return render_template("id.html", results = dbase.getid(id))
    else:
        return render_template("id0.html")

@app.route('/by-login')
def by_login():
    db = get_db()
    dbase = FDatabase(db)
    login = request.args['login']
    return render_template("login.html", results = dbase.getlog(login))

@app.route('/by-id')
def by_id():
    db = get_db()
    dbase = FDatabase(db)
    id = request.args['id']
    return render_template("id.html", results = dbase.getid(id))

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
            g.link_db.close()


if __name__ == "__main__":
    app.run(debug=True)
