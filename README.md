# "DBGeniePlus" (Enhanced Database Generator and Populator)
<br>

## Table of Contents
1. [Introduction](#introduction)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Usage](#usage)
5. [YAML File Format](#yamlfileformat)
6. [Customization](#customization)
7. [Dependencies](#dependencies)
8. [Contributing](#contributing)
9. [Acknowledgments](#acknowledgments)
<br>
   
## 1. Introduction <a name="introduction"></a>
This Python project allows you to automatically generate and populate a database using a YAML configuration file. You can specify the database details and table structure in the YAML file, and the script will create the database schema and populate the tables with fake data. It's a useful tool for setting up and testing databases for development and testing purposes.

<br>

## 2. Prerequisites <a name="prerequisites"></a>
Before you begin, ensure you have met the following requirements:
- <b>Python 3.x </b> installed on your system
  
- <b>MySQL Server:</b> Installed and running. You should have the necessary credentials (username, password, database name) for connecting to the MySQL server.
  
- <b>Git:</b> Installed if you want to clone this project from a Git repository.
  
- Install required libraries using pip from terminal
  ```bash
  pip install -r requirement.txt
  ```
<br>

## 3. Installation  <a name="installation"></a>

### 3.1  Installing Git

If you don't have Git installed, follow the instructions below based on your operating system:

#### Linux (Ubuntu/Debian)

```bash
sudo apt update
sudo apt install git
```
#### macOS
```bash
brew install git
```
#### Windows
Download the Git installer from [Git for Windows] (https://gitforwindows.org/) and follow the installation steps.
<br></br>
### 3.2  Installing Python
You can download Python from the official website [Python.org](https://www.python.org/downloads/) and follow the installation instructions for your specific OS.
<br></br>
### 3.3  Installing MySQL Server
Follow the official installation instructions for MySQL based on your OS:
-[MySQL Installation Guide for Linux](https://dev.mysql.com/doc/mysql-installation-excerpt/5.7/en/linux-installation.html)
-[MySQL Installation Guide for macOS](https://dev.mysql.com/doc/mysql-installation-excerpt/5.7/en/macos-installation.html)
-[MySQL Installation Guide for Windows](https://dev.mysql.com/doc/mysql-installation-excerpt/5.7/en/windows-installation.html)

<br>

## 4. Usage  <a name="usage"></a> 

### 4.1 Clone the Repository
To get started, clone this repository using Git:
```bash
git clone https://github.com/Ps1231/Automatic-Database-Generator-and-Populator
```
### 4.2 Navigate to the Project Directory
Change your working directory to the project folder:
```bash
cd Automatic-Database-Generator-and-Populator
```
### 4.3  Create a YAML configuration file 
This specifies the database details and table structure. See the YAML File Format section for details.

   
### 4.4 Run the Application
Run the main.py script with the YAML file as an argument:
```bash
 python main.py your_yaml_file.yaml
```
 The script will generate the database schema and populate the tables with data based on the configuration in the YAML file.

<br>

## 5. YAML File Format  <a name="yamlfileformat"></a>
``` yaml
mysql:
  host: your_database_host
  user: your_database_user
  password: your_database_password
  database: your_database_name
  num_records: no_of _records_to_be_generated
table_definition:
  TableName:
    columns:
      - Column1_Name: Column1_DataType
      - Column2_Name: Column2_DataType
      # Add more columns as needed
    foreign_keys:
      - fk_column: ForeignKey_Column_Name
        references_table: Referenced_Table_Name
        references_column: Referenced_Column_Name
      # Add more foreign keys as needed
    primary_key:
      - PrimaryKey_Column_Name
      # Add more primary key columns as needed

  # Define more tables as needed

# Define additional tables and configurations as needed
```
Sample yaml file is given here as config.yaml
- <TableName>: The name of the table.
- <Column1_Name>: The name of a column in the table.
- <Column1_DataType>: The data type of the column.
- primary_key: Adding Primary key column of the table. (Can have composite primary key)
- <PrimaryKey_Column_Name>: The name of primary key column.
- foreign_keys: Adding foreign key detai of the table.
- <fk_column>: The name foreign key column.
- <references_table>: The name referenced table for foreign key.
- <references_column>: The name referenced column for foreign key.
<br></br>
## 6. Customization <a name="customization"></a>
You can customize various aspects of the database generation and population process to suit your specific needs.
You can customize the number of entries generated for each table by modifying the num_records variable in your Yaml file creating customized yaml file using given template.
<br></br>
## 7. Dependencies <a name="dependencies"></a>
- ArgumentParser: Used to give YAML file as argument from terminal.
- PyYAML: Used for parsing YAML configuration files.
- Faker: Used for generating fake data.
- Pymysql: Used for Database connectivity.
<br></br>
## 8. Contributing <a name="contributing"></a>
Contributions are welcome! If you have any suggestions or improvements, please open an issue or create a pull request.
<br></br>
## 9. Acknowledgments <a name="acknowledgments"></a>
The project uses the Faker library for generating fake data.
Thanks to SQLAlchemy and PyYAML for their great libraries that make this project possible.



