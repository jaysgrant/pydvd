#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sqlite3
from configparser import ConfigParser
import datetime

CONFIG_PATH = os.path.join(os.path.dirname(__file__), 'config/config.ini')
NOW = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
date = NOW

# variables for testing purposes, modify as needed
name = 'The Muppet Movie'
genre = 'Family'
field_name = 'film_genre'
field_value = genre
record_id = '1'
delete_id = '4'


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


def query_all():
    con = db_connect()
    cur = con.cursor()
    cur.execute('''SELECT film_id, film_name, film_genre, date_added FROM film_inv''')
    all_rows = cur.fetchall()
    for row in all_rows:
        print('{0} : {1}, {2}, {3}'.format(row[0], row[1], row[2], row[3]))
    con.close()


def conditional_query(field_name, field_value):
    con = db_connect()
    cur = con.cursor()
    cur.execute('''SELECT film_id, film_name, film_genre, date_added FROM film_inv WHERE '''
                + field_name + '''=?''', (field_value,))
    all_rows = cur.fetchall()
    for row in all_rows:
        print('{0} : {1}, {2}, {3}'.format(row[0], row[1], row[2], row[3]))
    con.close()


def record_update(field_name, field_value, record_id):
    con = db_connect()
    cur = con.cursor()
    cur.execute('''UPDATE film_inv SET ''' + field_name + '''= ? WHERE film_id = ? ''', (field_value, record_id))
    cur.execute('''SELECT film_id, film_name, film_genre, date_added FROM film_inv WHERE film_id =? ''', (record_id,))
    all_rows = cur.fetchall()
    for row in all_rows:
        print('{0} : {1}, {2}, {3}'.format(row[0], row[1], row[2], row[3]))
    con.commit()


def record_delete(delete_id):
    con = db_connect()
    cur = con.cursor()
    cur.execute('''DELETE FROM film_inv WHERE film_id = ? ''', delete_id,)
    con.commit()
    con.close


# These function calls will exist in a different file, and are only here for testing purposes
try:
    film_insert(name, genre, date)
except sqlite3.Error as e:
    print(e)
except Exception as e:
    print(e)

try:
    query_all()
except sqlite3.Error as e:
    print(e)
except Exception as e:
    print(e)

try:
    conditional_query(field_name, field_value)
except sqlite3.Error as e:
    print(e)
except Exception as e:
    print(e)

try:
    record_update(field_name, field_value, record_id)
except sqlite3.Error as e:
    print(e)
except Exception as e:
    print(e)

try:
    record_delete(delete_id)
except sqlite3.Error as e:
    print(e)
except Exception as e:
    print(e)
