#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import db_init
import pydvd_utils
import datetime
import sqlite3

NOW = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def check_setup(subdir):
    print('\n')
    if not os.path.exists(subdir):
        print('Setup appears to not have been run, this will be done first. \n')
        try:
            db_init.main()
            print('Setup completed. An empty database has been created. \n')
        except Exception as e:
            print(e)


def main_menu():
    print('1. Add a movie to the database.')
    print('2. Display a list of all the movies in the database.')
    print('3. Search the database based on movie title or genre.')
    print('4. Update a movie in the database.')
    print('5. Delete a movie from the database.')
    print('6. Export table to CSV.')
    print('X. Exit PyDVD.')

    while "the answer is invalid":
        reply = str(input('Select your desired action (1-6, or x to exit): ')).lower().strip()
        if reply[:1] == '1':
            insert_record()
            main()
        if reply[:1] == '2':
            query_all()
            main()
        if reply[:1] == '3':
            film_query()
            main()
        if reply[:1] == '4':
            record_update()
            main()
        if reply[:1] == '5':
            delete_record()
            main()
        if reply[:1] == '6':
            csv_export()
            main()
        if reply[:1] == 'x':
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
            field_value = get_genre_name()
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
    try:
        name = str(input('Name of movie: '))
        date = NOW
        film_table = 'film_inv'
        genre_name = get_genre_name()
        pydvd_utils.record_insert(film_table, name, genre_name, date)
    except sqlite3.Error as e:
        print(e)
    except Exception as e:
        print(e)


def film_query():
    question = 'Field to search, either name or genre,'
    while "the answer is invalid":
        question_answer = str(input(question + ' (n/g): ')).lower().strip()
        if question_answer[:1] == 'n':
            field_name = 'film_name'
            field_value = str(input('Film name to search for: '))
            try:
                pydvd_utils.film_query(field_name, field_value)
                main()
            except sqlite3.Error as e:
                print(e)
            except Exception as e:
                print(e)
        if question_answer[:1] == 'g':
            field_name = 'film_genre'
            field_value = get_genre_name()
            try:
                pydvd_utils.film_query(field_name, field_value)
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


def csv_export():
    try:
        pydvd_utils.csv_export()
    except sqlite3.Error as e:
        print(e)
    except Exception as e:
        print(e)


def get_genre_name():
    genre_table = 'genre_names'
    print('Select the ID of the genre for your movie form the list below.')
    all_rows = pydvd_utils.cond_query_all(genre_table)
    for row in all_rows:
        print(row)
    while True:
        try:
            genre = int(input('Genre of movie: '))
            break
        except:
            print("Please enter a numerical value.")
    genre_name = str(pydvd_utils.get_genre_name(genre))
    return genre_name


def main():
    check_setup(subdir=os.path.join(os.path.dirname(__file__), 'data'))
    main_menu()


if __name__ == '__main__':
    main()
