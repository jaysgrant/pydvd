#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pydvd_utils
import sqlite3

field_name = 'film_genre'
field_value = 'SciFi'
record_id = '1'


def main():
    try:
        pydvd_utils.record_update(field_name, field_value, record_id)
    except sqlite3.Error as e:
        print(e)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
