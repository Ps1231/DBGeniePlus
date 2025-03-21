import yaml
import pymysql
from Populator import insert_fake_data


def create_mysql_tables_from_yaml(config_file_path):

    # Load the YAML configuration file
    with open(config_file_path, 'r') as yaml_file:
        config = yaml.safe_load(yaml_file)

        # Connect to the MySQL server (without specifying a database initially)
    connection = pymysql.connect(
        host=config['mysql']['host'],
        user=config['mysql']['user'],
        password=config['mysql']['password'],
        charset='utf8mb4'
    )
    cursor = connection.cursor()
    num_records = config['mysql']['num_records']
    # Create the database if it doesn't exist
    database_name = config['mysql']['database']
    create_database_query = f"CREATE DATABASE IF NOT EXISTS {database_name};"
    cursor.execute(create_database_query)
    print(
        f"Database '{database_name}' created successfully or already exists.")

    # Connect to the MySQL database
    connection = pymysql.connect(
        host=config['mysql']['host'],
        user=config['mysql']['user'],
        password=config['mysql']['password'],
        database=config['mysql']['database'],
        charset='utf8mb4',
        collation='utf8mb4_general_ci'
    )
    cursor = connection.cursor()
    try:
        # Create tables based on the configuration
        for table_name, table_data in config['table_definition'].items():
            create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ("

            # Add columns
            for column in table_data['columns']:
                column_name = next(iter(column))
                column_info = column[column_name]
                create_table_query += f"{column_name} {column_info}, "

            # Add primary key constraint
            if 'primary_key' in table_data:
                primary_key = ', '.join(table_data['primary_key'])
                create_table_query += f"PRIMARY KEY ({primary_key}), "

            # Add foreign key constraints
            if 'foreign_keys' in table_data:
                for fk in table_data['foreign_keys']:
                    create_table_query += (
                        f"FOREIGN KEY ({fk['fk_column']}) "
                        f"REFERENCES {fk['references_table']}({fk['references_column']}), "
                        f"ON DELETE CASCADE ON UPDATE CASCADE, "
                    )

            create_table_query = create_table_query.rstrip(', ') + ");"

            # Execute the create table query
            cursor.execute(create_table_query)
            print(f"Table '{table_name}' created successfully.")
            # num_records = int(
            #     input("Enter no of entries for table ", table_name))

            insert_fake_data(connection, config, table_name,
                             table_data, num_records)

    except pymysql.Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        connection.close()
