#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sqlite3
from configparser import ConfigParser
import csv
import fileinput

CONFIG_PATH = os.path.join(os.path.dirname(__file__), 'config/config.ini')


def get_settings(config_path=CONFIG_PATH):
    config = ConfigParser()
    config.read(config_path)
    return config


def db_connect():
    config = get_settings()
    con = sqlite3.connect(config.get('main', 'datasource'))
    return con


def record_insert(table_name, name, genre, date):
    con = db_connect()
    cur = con.cursor()
    cur.execute('''INSERT INTO ''' + table_name + '''(film_name, film_genre, date_added)
                  VALUES(?,?,?)''', (name, genre, date))
    print("Record ID " + str(cur.lastrowid) + " created.")
    con.commit()
    con.close()


def query_all():
    con = db_connect()
    cur = con.cursor()
    print('\n')
    # todo The line below should return the column names, but currently does not work.
    # cur.execute('PRAGMA table_info(film_inv)')
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
    con.close()


def record_delete(delete_id):
    con = db_connect()
    cur = con.cursor()
    cur.execute('''DELETE FROM film_inv WHERE film_id = ? ''', delete_id,)
    con.commit()
    con.close()


def csv_export():
    con = db_connect()
    cur = con.cursor()
    cur.execute('''SELECT film_id, film_name, film_genre, date_added FROM film_inv''')
    all_rows = cur.fetchall()
    with open('output.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['Film ID', 'Film Name', 'Film Genre', 'Date Added'])
        writer.writerows(all_rows)
        f.close()
    con.close()

