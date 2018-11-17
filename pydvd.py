#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import setup
import pydvd_utils


def check_setup(subdir):
    print('\n')
    if not os.path.exists(subdir):
        print('Setup appears to not have been run, this will be done first. \n')
        try:
            setup.main()
            print('Setup completed. An empty database has been created. \n')
        except Exception as e:
            print(e)


def main_menu():
    print('Select your desired action. \n')
    print('1. Add a movie to the database.')
    print('2. Display a list of all the movies in the database.')
    print('3. Search the database based on movie title or genre.')
    print('4. Update a movie in the database.')
    print('5. Delete a movie from the database.')
    print('6. Exit PyDVD.')


def main():
    check_setup(subdir=os.path.join(os.path.dirname(__file__), 'data'))
    main_menu()


if __name__ == '__main__':
    main()
