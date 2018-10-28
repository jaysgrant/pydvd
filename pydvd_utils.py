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












