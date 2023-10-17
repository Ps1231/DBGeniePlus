from faker import Faker
import random
import string

fake = Faker()

# Function to generate fake data based on column data type


def generate_regular_fake_data(column_name, column_info):
    data_type = column_info.split()[0].upper()

    if 'ENUM' in data_type:
        return generate_enum_data(column_info)
    elif 'DECIMAL' in data_type:
        return generate_decimal_data(column_info)
    size = int(column_info.split('(')[1].split(')')[
               0]) if '(' in column_info else None
    if 'BOOLEAN' in data_type:
        return fake.boolean()
    elif 'DATE' in data_type:
        return fake.date_between(start_date='-1y', end_date='today')
    elif 'TIME' in data_type:
        return fake.time(pattern='%H:%M:%S')
    elif 'DATETIME' in data_type:
        return fake.date_time_this_year()
    elif 'AGE' in column_name.lower():
        return fake.random_number(2)
    elif 'VARCHAR' in data_type:
        return generate_varchar_data(size)
    elif 'CHAR' in data_type:
        return generate_char_data(size)
    elif 'BIGINT' in data_type:
        return generate_bigint_data(size)
    elif 'INT' in data_type:
        return generate_int_data(size)
    elif 'TEXT' in data_type:
        return generate_text_data(size)
    elif 'CITY' in column_name.upper():
        return generate_city_data(size)
    elif 'COLOR' in column_name.lower() or 'COLOUR' in column_name.lower():
        return generate_color_data(size)
    elif 'GENDER' in column_name.lower():
        return generate_gender_data(size)
    elif 'STATE' in column_name.upper():
        return generate_state_data(size)
    elif 'EMAIL' in column_name.upper():
        return generate_email_data(size)
    elif 'COUNTRY' in column_name.upper():
        return generate_country_data(size)
    elif 'PASSWORD' in column_name.upper():
        return generate_password_data(size)
    elif 'FIRST_NAME' in column_name.upper():
        return generate_first_name_data(size)
    elif 'LAST_NAME' in column_name.upper():
        return generate_last_name_data(size)
    elif 'NAME' in column_name.upper():
        return generate_name_data(size)
    elif 'ADDRESS' in column_name.upper():
        return generate_address_data(size)
    elif any(word in column_name.upper() for word in ['PHONE', 'CONTACT', 'MOBILE']):
        return fake.random_number(10)

# Function for inserting enum values
def generate_enum_data(column_info):
    enum_values_with_quotes = column_info.split('(')[1].split(')')[
        0].split(',')
    enum_values = [value.strip().strip("'")
                   for value in enum_values_with_quotes]
    random_enum_value = fake.random_element(elements=enum_values)
    return random_enum_value.strip("'")

# Function for inserting Varchar values
def generate_varchar_data(size):
    if size is not None and size > 50:
        return fake.text(max_nb_chars=size)
    elif size is not None:
        return ''.join(random.choice(string.ascii_uppercase) for _ in range(size))
    else:
        return random.choice(string.ascii_uppercase)

# Function for inserting values of char DataType
def generate_char_data(size):
    if size is not None and size > 50:
        return fake.text(max_nb_chars=size)
    elif size is not None:
        return ''.join(random.choice(string.ascii_letters) for _ in range(size))
    else:
        return random.choice(string.ascii_uppercase)

# Function for inserting values of bigint DataType
def generate_bigint_data(size):
    if size is not None:
        return fake.random_int(min=1, max=10 ** size - 1)
    else:
        return fake.random_number(10)

# Function for inserting values of int DataType
def generate_int_data(size):
    if size is not None:
        return fake.random_int(min=1, max=10 ** size - 1)
    else:
        return fake.random_int(min=1, max=99999)

# Function for inserting values of decimal DataType
def generate_decimal_data(column_info):
    parts = column_info.split('(')[1].split(')')[0].split(',')
    precision = int(parts[0])
    scale = int(parts[1]) if len(parts) > 1 else 2
    return abs(fake.pydecimal(left_digits=precision - scale, right_digits=scale))

# Function for inserting fake text of given size
def generate_text_data(size):
    if size is not None:
        return fake.text(max_nb_chars=size)
    return fake.text(max_nb_chars=200)

# Function for inserting name of random cities
def generate_city_data(size):
    if size is not None and size <= 2:
        return fake.city_suffix()
    elif size is not None and size >= 20:
        return fake.city_suffix()
    elif size is not None:
        return fake.text(max_nb_chars=size)
    return fake.city()

# Function for inserting random colors
def generate_color_data(size):
    fake_color = fake.color_name()
    if len(fake_color) > size:
        fake_color = fake_color[:size]
    return fake_color

# Function for inserting random gender
# you can modify according to your convienience
def generate_gender_data(size):
    if size > 5:
        return fake.random_element(elements=('male', 'female'))
    else:
        return fake.random_element(elements=('M', 'F'))

# Function for inserting random names for state
def generate_state_data(size):
    if size is not None and size >= 3:
        return fake.state_abbr()
    elif size is not None and size < 3:
        return fake.text(max_nb_chars=size)
    return fake.state_abbr()

# Function for inserting random emails
def generate_email_data(size):
    email = fake.email()
    if len(email) > size:
        email = email[:size]
    return email

# Function for inserting random countries
def generate_country_data(size):
    fake_country = fake.country()
    if len(fake_country) > size:
        fake_country = fake_country[:size]
    return fake_country

# Function for inserting random passwords
def generate_password_data(size):
    if size is not None:
        return fake.password(length=size)
    else:
        return fake.password()

# Function for inserting random values of first name
def generate_first_name_data(size):
    first_name = fake.first_name()
    if len(first_name) > size:
        first_name = first_name[:size]
    return first_name

# Function for inserting random values of last name
def generate_last_name_data(size):
    last_name = fake.last_name()
    if len(last_name) > size:
        last_name = last_name[:size]
    return last_name

# Function for inserting random values of name
def generate_name_data(size):
    name = fake.name()
    if len(name) > size:
        name = name[:size]
    return name

# Function for inserting random addresses
def generate_address_data(size):
    fake_add = fake.address()
    if len(fake_add) > size:
        fake_add = fake_add[:size]
    return fake_add
