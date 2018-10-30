#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sqlite3
from configparser import ConfigParser


CONFIG_PATH = os.path.join(os.path.dirname(__file__), 'config/config.ini')


def get_settings(config_path=CONFIG_PATH):
    config = ConfigParser()
    config.read(config_path)
    return config


def db_connect():
    config = get_settings()
    con = sqlite3.connect(config.get('main', 'datasource'))
    return con


con = db_connect()
cur = con.cursor()


sql_create_film_inv_table = """ CREATE TABLE IF NOT EXISTS film_inv (
                                        film_id integer PRIMARY KEY AUTOINCREMENT UNIQUE Not NULL, 
                                        film_name varchar Not NULL,
                                        film_genre varchar,
                                        date_added datetime
                                    ); """

cur.execute(sql_create_film_inv_table)

