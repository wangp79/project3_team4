from asyncio.base_futures import _format_callbacks
from curses import noecho
from multiprocessing.util import ForkAwareThreadLock
from optparse import Values
import os
from tkinter import Variable
from tkinter.tix import COLUMN
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, redirect,url_for
from flask import request
from flask import render_template
import pandas as pd
import sqlite3
from pandas import read_sql_query, read_sql_table
from sqlalchemy import create_engine

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

import os
# basedir = os.path.abspath(os.path.dirname(__file__))



app= Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '') or "sqlite:///NEO.db"
# os.path.join(basedir, 'NEO.db')
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '') 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Neo(db.Model): 
    __tablename__='Neos'  
    id = db.Column(db.Integer, primary_key=True)
    des = db.Column(db.String(225))
    orbit_id = db.Column(db.String)
    jd = db.Column(db.String(40))
    dist = db.Column(db.String())
    dist_min = db.Column(db.String())
    dist_max = db.Column(db.String())
    v_rel = db.Column(db.String())
    v_inf = db.Column(db.String())
    t_sigma_f = db.Column(db.String(40))
    body = db.Column(db.String(20))
    h = db.Column(db.String())

    def __init__(self, des, orbit_id, jd, dist, dist_min, dist_max, v_rel, v_inf,t_sigma_f, body, h):
        self.des = des
        self.orbit_id = orbit_id
        self.jd = jd
        self.dist = dist
        self.dist_min = dist_min
        self.dist_max = dist_max
        self.v_rel = v_rel
        self.v_int = v_inf
        self.t_sigma_f = t_sigma_f
        self.body = body
        self.h = h 

db.create_all()


con = sqlite3.connect("NEO.db")
cursor = con.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(cursor.fetchall())



# converting sqlite to Dataframe *******************

cnx = sqlite3.connect('NEO.db')
records_df = pd.read_sql_query('select * from NEOs', cnx)
scatterplot_data = pd.read_sql_query('select v_rel, h from NEOs', cnx)
bubblechart_data = pd.read_sql_query('select dist_min, h from NEOs where dist_min <= .05 and h <= 22.0', cnx)
print(bubblechart_data)
cnx.commit()


bubblechart_data.insert(1,'y',0)
print(bubblechart_data)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/index')
def index_page():
    return render_template('index.html')

# @app.route('/api/result')
# def result():
#     json_data = records_df.to_json(orient='values')
#     return json_data


## conn to scatterplot 
@app.route('/scatterplot')
def display_scatter():
    return render_template('scatterplot.html')
 
## send chart_1 json data to scatterplot html
@app.route('/api/scatterplot')
def display_api_scatter():
    chart_1 = scatterplot_data.to_json(orient='values') #values, table, columns
    return chart_1


## conn to bubblechart 
@app.route('/bubblechart')
def display_bubble():
    return render_template('bubblechart.html')
 
## send chart_2 json data to bubblechart html
@app.route('/api/bubblechart')
def display_api_bubble():
    chart_2 = bubblechart_data.to_json(orient='values') #values, table, columns
    return chart_2

if __name__ == '__main__':
    app.run(debug=True)

    










# @app.route('/user/<name>')
# def index(name):
#     return f'<h1>hello {name}</h1>'

# @app.route('/admin')
# def admin():
#     return redirect(url_for('index',name='Admin!')) # when use url_for function, passing function NAME. if will redirect to a dynamic use additional parameter passing a given name

# @app.route('/<user>')
# def temp(user):
#     return render_template('index.html', user_name=user,name_listing=['paul','alex','jack'])  #user_name is parameter passing from HTML {{user_name}} need equal to the dynamic name from flask



