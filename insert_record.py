#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime
import pydvd_utils
import sqlite3

NOW = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
date = NOW
name = 'Serenity'
genre = 'SciFi'
table_name = 'film_inv'


def main():
    try:
        pydvd_utils.record_insert(table_name, name, genre, date)
    except sqlite3.Error as e:
        print(e)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
