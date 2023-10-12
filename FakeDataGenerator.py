from faker import Faker
import random
import string
import datetime
fake = Faker()

# Function to generate fake data based on column data type


def generate_regular_fake_data(column_name, column_info):
    # Extract the data type from the column_info string
    data_type = column_info.split()[0].upper()
    # Extract the size (if specified) from the column_info
    if 'ENUM' in data_type:
        enum_values_with_quotes = column_info.split('(')[1].split(')')[
            0].split(',')
        enum_values = [value.strip().strip("'")
                       for value in enum_values_with_quotes]
        random_enum_value = fake.random_element(elements=enum_values)
        return random_enum_value.strip("'")
    elif 'BOOLEAN' in data_type:
        # Generate a random boolean value
        return fake.boolean()
    elif 'DATE' in data_type:
        return fake.unique.date_between(start_date='-1y', end_date='today')
    elif 'TIME' in data_type:
        return fake.time(pattern='%H:%M:%S')

    elif 'DATETIME' in data_type:
        return fake.date_time_this_year()
    # Check if the data type is integer (INT)
    elif 'BIGINT' in data_type:
        size = int(column_info.split('(')[1].split(')')[
            0]) if '(' in column_info else None
        if size is not None:
            return fake.unique.random_int(min=1, max=10 ** size - 1)
        else:
            return fake.random_int(min=7000000000, max=9999999999)
    elif 'INT' in data_type:
        # Generate a random integer within a specified range

        size = int(column_info.split('(')[1].split(')')[
            0]) if '(' in column_info else None
        if size is not None:
            return fake.unique.random_int(min=1, max=10 ** size - 1)
        else:
            return fake.unique.random_int(min=1, max=99999)
    elif 'DECIMAL' in data_type:
        # Extract precision and scale from the column_info, e.g., DECIMAL(4, 2)
        parts = column_info.split('(')[1].split(')')[0].split(',')
        precision = int(parts[0])
        # Default scale to 2 if not specified
        scale = int(parts[1]) if len(parts) > 1 else 2

        # Generate a fake decimal value with the specified precision and scale
        return fake.pydecimal(left_digits=precision - scale, right_digits=scale)
    elif 'TEXT' in data_type:
        size = int(column_info.split('(')[1].split(')')[
            0]) if '(' in column_info else None
        if size is not None:
            return fake.text(max_nb_chars=size)
        return fake.text(max_nb_chars=200)
    elif 'CITY' in column_name.upper():
        size = int(column_info.split('(')[1].split(')')[
            0]) if '(' in column_info else None
        if size is not None and size <= 2:
            return fake.city_suffix()  # Generate a city suffix for short sizes
        elif size is not None and size >= 20:
            # Generate text for larger sizes
            return fake.city_suffix()
        elif size is not None:
            return fake.text(max_nb_chars=size)
        return fake.city()

    elif 'STATE' in column_name.upper():
        size = int(column_info.split('(')[1].split(')')[
            0]) if '(' in column_info else None
        if size is not None and size >= 3:
            return fake.state_abbr()
        elif size is not None and size < 3:
            return fake.text(max_nb_chars=size)
        return fake.state_abbr()

    elif 'EMAIL' in column_name.upper():
        return fake.unique.email()

    elif 'PASSWORD' in column_name.upper():
        return fake.password(length=8)
    elif 'FIRST_NAME' in column_name.upper():
        return fake.unique.first_name()
    elif 'LAST_NAME' in column_name.upper():
        return fake.unique.last_name()
    elif 'NAME' in column_name.upper():
        size = int(column_info.split('(')[1].split(')')[
            0]) if '(' in column_info else None
        if size is not None and size > 50:
            return fake.unique.name()
        elif size is not None:
            return fake.text(max_nb_chars=size)
        else:
            return fake.unique.name()
    elif 'ADDRESS' in column_name.upper():
        return fake.address()
    elif 'PHONE' or 'CONTACT' or 'MOBILE' in column_name.upper():
        return fake.random_int(min=7000000000, max=9999999999)

    elif 'VARCHAR' in data_type:
        size = int(column_info.split('(')[1].split(')')[
            0]) if '(' in column_info else None
        if size is not None and size > 50:
            return fake.text(max_nb_chars=size)
        elif size is not None:
            return ''.join(random.choice(string.ascii_uppercase) for _ in range(size))
        else:
            return random.choice(string.ascii_uppercase)

    elif 'CHAR' in data_type:
        size = int(column_info.split('(')[1].split(')')[
            0]) if '(' in column_info else None
        if size is not None and size > 50:
            return fake.text(max_nb_chars=size)
        elif size is not None:
            return ''.join(random.choice(string.ascii_letters) for _ in range(size))
        else:
            return random.choice(string.ascii_uppercase)
