#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sqlite3
from configparser import ConfigParser
import csv

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


def cond_query_all(table_name):
    con = db_connect()
    cur = con.cursor()
    cur.execute('''SELECT * from ''' + table_name)
    all_rows = cur.fetchall()
    return all_rows


def query_all():
    con = db_connect()
    cur = con.cursor()
    print('\n')
    cur.execute('''SELECT film_id, film_name, film_genre, date_added FROM film_inv''')
    all_rows = cur.fetchall()
    for row in all_rows:
        print('{0} : {1}, {2}, {3}'.format(row[0], row[1], row[2], row[3]))
    con.close()


def film_query(field_name, field_value):
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
    filename = 'output.csv'
    con = db_connect()
    cur = con.cursor()
    cur.execute('''SELECT film_id, film_name, film_genre, date_added FROM film_inv''')
    all_rows = cur.fetchall()
    with open(filename, 'w') as f:
        writer = csv.writer(f)
        columns = get_column_names()
        writer.writerow(columns)
        writer.writerows(all_rows)
        f.close()
    con.close()
    remove_empty_lines(filename)
    csv_path = os.path.dirname(os.path.abspath(filename))
    print('File saved to', csv_path)


def remove_empty_lines(filename):
    if not os.path.isfile(filename):
        print("{} does not exist ".format(filename))
        return
    with open(filename) as filehandle:
        lines = filehandle.readlines()
    with open(filename, 'w') as filehandle:
        lines = filter(lambda x: x.strip(), lines)
        filehandle.writelines(lines)


def get_column_names():
    column_names = []
    con = db_connect()
    cur = con.cursor()
    cur.execute("PRAGMA table_info(film_inv)")
    data_extract = cur.fetchall()
    # print(data_extract)
    for column in data_extract:
        column_names.append(column[1])
        column_names = [s.replace('_', ' ') for s in column_names]
        column_names = [s.title() for s in column_names]
    return column_names


def get_genre_name(record_id):
    con = db_connect()
    cur = con.cursor()
    cur.execute('''SELECT genre_name FROM genre_names WHERE genre_id =? ''', (record_id,))
    genre_name = cur.fetchone()
    genre_name = ''.join(genre_name)
    return genre_name
