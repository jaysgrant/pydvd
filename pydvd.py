#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import setup
import pydvd_utils
import datetime
import sqlite3

NOW = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


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
    print('1. Add a movie to the database.')
    print('2. Display a list of all the movies in the database.')
    print('3. Search the database based on movie title or genre.')
    print('4. Update a movie in the database.')
    print('5. Delete a movie from the database.')
    print('6. Exit PyDVD.')

    while "the answer is invalid":
        reply = str(input('Select your desired action (1-6): ')).lower().strip()
        if reply[:1] == '1':
            insert_record()
            main()
        if reply[:1] == '2':
            query_all()
            main()
        if reply[:1] == '3':
            conditional_query()
            main()
        if reply[:1] == '4':
            record_update()
            main()
        if reply[:1] == '5':
            delete_record()
            main()
        if reply[:1] == '6':
            program_exit()


def delete_record():
    while True:
        try:
            delete_id = int(input('Which database record do you wish to delete? '))
            break
        except:
            print("Please enter a numerical value.")
    try:
        pydvd_utils.record_delete(str(delete_id))
    except sqlite3.Error as e:
        print(e)
    except Exception as e:
        print(e)


def program_exit():
    question = 'Are you sure you want to exit the application?'
    answer = yes_no(question)
    if answer is True:
        exit()
    else:
        main()


def record_update():
    question = 'Field to search, either name or genre,'
    while True:
        try:
            record_id = int(input('Which database record do you wish to update? '))
            break
        except:
            print("Please enter a numerical value.")
    while "the answer is invalid":
        question_answer = str(input(question + ' (n/g): ')).lower().strip()
        if question_answer[:1] == 'n':
            field_name = 'film_name'
            field_value = str(input('New film name: '))
            try:
                pydvd_utils.record_update(field_name, field_value, record_id)
                main()
            except sqlite3.Error as e:
                print(e)
            except Exception as e:
                print(e)
        if question_answer[:1] == 'g':
            field_name = 'film_genre'
            field_value = str(input('New film genre: '))
            try:
                pydvd_utils.record_update(field_name, field_value, record_id)
                main()
            except sqlite3.Error as e:
                print(e)
            except Exception as e:
                print(e)


def yes_no(question):
    while "the answer is invalid":
        reply = str(input(question + ' (y/n): ')).lower().strip()
        if reply[:1] == 'y':
            return True
        if reply[:1] == 'n':
            return False


def insert_record():
    name = str(input('Name of movie: '))
    genre = str(input('Genre of movie: '))
    date = NOW
    table_name = 'film_inv'

    try:
        pydvd_utils.record_insert(table_name, name, genre, date)
    except sqlite3.Error as e:
        print(e)
    except Exception as e:
        print(e)


def conditional_query():
    question = 'Field to search, either name or genre,'
    while "the answer is invalid":
        question_answer = str(input(question + ' (n/g): ')).lower().strip()
        if question_answer[:1] == 'n':
            field_name = 'film_name'
            field_value = str(input('Film name to search for: '))
            try:
                pydvd_utils.conditional_query(field_name, field_value)
                main()
            except sqlite3.Error as e:
                print(e)
            except Exception as e:
                print(e)
        if question_answer[:1] == 'g':
            field_name = 'film_genre'
            field_value = str(input('Genre to search for: '))
            try:
                pydvd_utils.conditional_query(field_name, field_value)
                main()
            except sqlite3.Error as e:
                print(e)
            except Exception as e:
                print(e)


def query_all():
    try:
        pydvd_utils.query_all()
    except sqlite3.Error as e:
        print(e)
    except Exception as e:
        print(e)


def main():
    check_setup(subdir=os.path.join(os.path.dirname(__file__), 'data'))
    main_menu()


if __name__ == '__main__':
    main()
