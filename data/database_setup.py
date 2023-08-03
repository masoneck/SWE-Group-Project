import os
import sqlite3
import sys

from pathlib import Path


def setup_db(file_name):
    conn = sqlite3.connect(file_name)
    cursor = conn.cursor()
    # Create tables
    create_orders_table(cursor)
    create_users_table(cursor)
    create_items_table(cursor)
    create_discounts_table(cursor)
    # Close connections
    cursor.close()
    conn.close()

def delete_db(file_name):
    try:
        return os.remove(file_name)
    except FileNotFoundError:
        pass 

def create_items_table(cursor):
    cursor.execute("""
    CREATE TABLE Items(
        item_id        INTEGER PRIMARY KEY AUTOINCREMENT,
        name           VARCHAR,
        stock          INTEGER UNSIGNED,
        price          MONEY,
        department_id  INTEGER UNSIGNED
    )""")

def create_orders_table(cursor):
    cursor.execute("""
    CREATE TABLE Orders(
        order_id    INTEGER PRIMARY KEY AUTOINCREMENT,
        date        DATETIME,
        customer_id VARCHAR,
        total       MONEY,
        status      VARCHAR,
        sales_items VARCHAR
    )""")

def create_users_table(cursor):
    cursor.execute("""
    CREATE TABLE Users(
        user_id    INTEGER PRIMARY KEY AUTOINCREMENT,
        email      VARCHAR,
        first_name VARCHAR,
        last_name  VARCHAR,
        order_ids  VARCHAR
    )""")

def create_discounts_table(cursor):
    cursor.execute("""
    CREATE TABLE Discounts(
        phrase  VARCHAR,
        amount  MONEY
    )""")

if __name__ == '__main__':
    db_file_name = 'database.db' if len(sys.argv) == 1 else sys.argv[1]
    setup_db(db_file_name.strip())