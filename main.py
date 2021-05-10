import sqlite3
from sqlite3 import Error

# this function establishes the connection with sqlite


def create_connection(db_file):
    connection = None
    try:
        connection = sqlite3.connect(db_file)
        return connection
    except Error as err:
        print(err)

    return connection

# this function creates a table using python


def create_table(connection, create_table_query):
    try:
        conn = connection.cursor()
        conn.execute(create_table_query)
    except Error as err:
        print(err)

# this main function is where the above functions will be used


def main():
    database = "Desktop/sqlite/db/pythonsqlite.db"

    create_classes_table = """ CREATE TABLE IF NOT EXISTS classes (
										id integer PRIMARY KEY,
										class_name text NOT NULL,
										begin_date text,
										end_date text
									);"""

    create_tasks_table = """CREATE TABLE IF NOT EXISTS tasks (
										id integer PRIMARY KEY,
										task_name text NOT NULL,
										priority integer,
										status_id integer NOT NULL,
										project_id integer NOT NULL,
										begin_date text NOT NULL,
										end_date text NOT NULL,
										FOREIGN KEY (project_id) REFERENCES projects (id)
									);"""

    connection = create_connection(database)

    if connection is not None:
        create_table(connection, create_classes_table)
        create_table(connection, create_tasks_table)
    else:
        print("Error! cannot create the database connection!")


if __name__ == '__main__':
    main()
