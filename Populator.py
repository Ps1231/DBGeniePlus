import random
from FakeDataGenerator import generate_regular_fake_data
from DuplicateChecker import checker, checkerf
# Function to insert fake data into tables


def insert_fake_data(connection, config, table_name, table_data, num_records=10):
    cursor = connection.cursor()

    for _ in range(num_records):
        insert_query = f"INSERT INTO {table_name} ("

        # Add column names for insertion
        for column in table_data['columns']:
            column_name = next(iter(column))
            insert_query += f"{column_name}, "

        insert_query = insert_query.rstrip(', ') + ") VALUES ("

        # Generate fake data based on column data type
        for column in table_data['columns']:
            column_name = next(iter(column))
            column_info = column[column_name]
            fake_data = None

            if 'foreign_keys' in table_data:
                # Check if the column name matches the fk_column in foreign key
                for fk in table_data['foreign_keys']:
                    if column_name == fk['fk_column']:
                        # If it's a foreign key, fetch data from the referenced table
                        referenced_table = fk['references_table']
                        referenced_column = fk['references_column']

                        cursor.execute(
                            f"SELECT {referenced_column} FROM {referenced_table}")
                        values = cursor.fetchall()

                        if values:
                            fake_data = random.choice(values)[0]
                            fake_data = checkerf(connection, config, table_name, table_data, column_name,
                                                 fake_data, column_info, referenced_table, referenced_column, values)

                            # query = f"SELECT {column_name} FROM {table_name} WHERE {column_name} = %s"
                            # cursor.execute(query, (fake_data,))
                            # result = cursor.fetchall()
                            # values1 = [row[0] for row in result]

                            # while fake_data in values1:
                            #     fake_data = random.choice(values)[0]
                        break  # Stop checking other foreign keys
                    else:
                        # Generate fake data for non-foreign key columns
                        fake_data = generate_regular_fake_data(
                            column_name, column_info)
                        fake_data = checker(
                            connection, config, table_name, table_data, column_name, fake_data, column_info)

            else:
                # Generate fake data for regular columns
                fake_data = generate_regular_fake_data(
                    column_name, column_info)
                fake_data = checker(
                    connection, config, table_name, table_data, column_name, fake_data, column_info)
            insert_query += f"'{fake_data}', "

        insert_query = insert_query.rstrip(', ') + ");"
        print(f"Insert Query: {insert_query}")

        # Execute the insert query
        cursor.execute(insert_query)
        connection.commit()

# Usage example:
# insert_fake_data(connection, config, 'table_name', table_data, num_records=10)
