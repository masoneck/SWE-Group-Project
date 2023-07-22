
import sqlite3
import sys

from pathlib import Path


def setup_db(file_name):
    conn = sqlite3.connect(file_name)
    cursor = conn.cursor()
    # Create Orders table
    create_orders_table(cursor)
    # Create User table
    create_users_table(cursor)
    # Create items table
    create_items_table(cursor)


def create_items_table(cursor):
    # TODO
    # cursor.execute(
    #     "CREATE TABLE"
    # )


def create_orders_table(cursor):
    cursor.execute(
        "CREATE TABLE Orders("
        "order_id   INT PRIMARY KEY,"
        "date       DATETIME,"
        "total      MONEY,"
        "items      VARCHAR)"  # dict of item_id:item_amuunt, ...

    )

def create_users_table(cursor):
    cursor.execute(
        "CREATE TABLE Users("
        "user_id    INT PRIMARY KEY"
        "email      VARCHAR,"
        "first_name VARCHAR,"
        "last_name  VARCHAR,"
        "role       ENUM('customer', 'employee', 'administrator')"
        "password   VARCHAR,"  # hash
        "order      VARCHAR)"  # comma-seperated list of order_id's
    )


if __name__ == '__main__':
    db_file_name = 'database.db' if len(sys.argv) == 1 else sys.argv[1]
    setup_db(db_file_name.strip())