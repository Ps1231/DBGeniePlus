# Function to create corresponding database and tables
from DatabaseCreator import create_mysql_tables_from_yaml
import argparse

# Function to take yaml file as argument(input) in terminal to ru the program


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Generate fake data and populate MySQL tables based on a YAML configuration file.")
    parser.add_argument(
        "config_file", help="Path to the YAML configuration file")

    args = parser.parse_args()
    return args.config_file


config_file_path = parse_arguments()
# Function to create corresponding database and tables
create_mysql_tables_from_yaml(config_file_path)
