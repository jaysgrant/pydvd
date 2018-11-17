#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pydvd_utils
import sqlite3

delete_id = '2'


def main():
    try:
        pydvd_utils.record_delete(delete_id)
    except sqlite3.Error as e:
        print(e)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
