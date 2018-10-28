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


# table definition
table_name = 'film_inv'
id_field = 'film_id'
id_type = 'integer'
char_type = 'varchar'
name_field = 'film_name'
genre_field = 'film_genre'
date_field = 'date_added'
default_val = 'default value'

con = db_connect()
cur = con.cursor()
cur.execute('CREATE TABLE {tn} ({cn} {ft} PRIMARY KEY UNIQUE Not NULL)'\
            .format(tn=table_name, cn=id_field, ft=id_type))


cur.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ft} Not NULL DEFAULT '{df}'"\
            .format(tn=table_name, cn=name_field, ft=char_type, df=default_val))

cur.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ft}"\
            .format(tn=table_name, cn=genre_field, ft=char_type))

cur.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ft}"\
            .format(tn=table_name, cn=date_field, ft='datetime', df=default_val))

