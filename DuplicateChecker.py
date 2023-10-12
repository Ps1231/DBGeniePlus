import mysql.connector as mysql
from FakeDataGenerator import generate_regular_fake_data
import mysql.connector as mysql

import random


def checker(connection, config, table_name, table_data, column_name, fake_data, column_info):
    cursor = connection.cursor()
    query = f"SELECT {column_name} FROM {table_name} WHERE {column_name} = %s"
    cursor.execute(query, (fake_data,))
    result = cursor.fetchall()
    values = [row[0] for row in result]

    while fake_data in values:
        fake_data = generate_regular_fake_data(column_name, column_info)

    return fake_data


def checkerf(connection, config, table_name, table_data, column_name, fake_data, column_info, referenced_table, referenced_column, values):
    cursor = connection.cursor()

    query = f"SELECT {column_name} FROM {table_name} WHERE {column_name} = %s"
    cursor.execute(query, (fake_data,))
    result = cursor.fetchall()
    values1 = [row[0] for row in result]

    while fake_data in values1:
        fake_data = random.choice(values)[0]

    return fake_data
