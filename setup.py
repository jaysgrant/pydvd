#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import errno
import sqlite3
from configparser import ConfigParser

CONFIG_PATH = os.path.join(os.path.dirname(__file__), 'config/config.ini')

def create_dir(subdir):
    if not os.path.exists(subdir):
        os.makedirs(subdir)


def get_settings(config_path=CONFIG_PATH):
    config = ConfigParser()
    config.read(config_path)
    return config


def db_connect():
    config = get_settings()
    con = sqlite3.connect(config.get('main', 'datasource'))
    return con


try:
    subdir = os.path.join(os.path.dirname(__file__), 'data')
    create_dir(subdir)
except OSError as e:
    print(e)

try:
    con = db_connect()
    cur = con.cursor()
    sql_create_film_inv_table = (" CREATE TABLE IF NOT EXISTS film_inv (\n"
                                 "film_id integer PRIMARY KEY AUTOINCREMENT UNIQUE Not NULL, \n"
                                 "film_name varchar Not NULL,\n"
                                 "film_genre varchar,\n"
                                 "date_added datetime\n"
                                 "); ")
    cur.execute(sql_create_film_inv_table)
    con.commit()
except sqlite3.Error as e:
    print(e)
except Exception as e:
    print(e)
finally:
    if con:
        con.close()

