import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Generate fake data and populate MySQL tables based on a YAML configuration file.")
    parser.add_argument(
        "config_file", help="Path to the YAML configuration file")

    args = parser.parse_args()
    return args.config_file
