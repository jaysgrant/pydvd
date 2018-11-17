#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pydvd_utils
import sqlite3


field_name = 'film_genre'
field_value = 'SciFi'


def main():
    try:
        pydvd_utils.conditional_query(field_name, field_value)
    except sqlite3.Error as e:
        print(e)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
