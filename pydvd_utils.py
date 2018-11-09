#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sqlite3
from configparser import ConfigParser
import datetime

CONFIG_PATH = os.path.join(os.path.dirname(__file__), 'config/config.ini')
NOW = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

name = 'Star Wars'
genre = 'SciFi'
date = NOW


def get_settings(config_path=CONFIG_PATH):
    config = ConfigParser()
    config.read(config_path)
    return config


def db_connect():
    config = get_settings()
    con = sqlite3.connect(config.get('main', 'datasource'))
    return con


def film_insert(name, genre, date):
    con = db_connect()
    cur = con.cursor()
    cur.execute('''INSERT INTO film_inv(film_name, film_genre, date_added)
                  VALUES(?,?,?)''', (name, genre, date))
    print("Record ID " + str(cur.lastrowid) + " created.")
    con.commit()
    con.close


def film_query():
    con = db_connect()
    cur = con.cursor()
    cur.execute('''SELECT film_id, film_name, film_genre, date_added FROM film_inv''')
    all_rows = cur.fetchall()
    for row in all_rows:
        print('{0} : {1}, {2}, {3}'.format(row[0], row[1], row[2], row[3]))
    con.close()


try:
    film_insert(name, genre, date)
except sqlite3.Error as e:
    print(e)
except Exception as e:
    print(e)

try:
    film_query()
except sqlite3.Error as e:
    print(e)
except Exception as e:
    print(e)
