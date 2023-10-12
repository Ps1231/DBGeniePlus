# Automatic-Database-Generator-and-Populator
<br>

## Table of Contents
1. [Introduction](#introduction)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Usage](#usage)
5. [YAML File Format](#yamlfileformat)
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
  pip install pymysql pyyaml faker ArgumentParser
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
```bash
Download the Git installer from [Git for Windows] (https://gitforwindows.org/) and follow the installation steps.
```
### 3.2  Installing Python
You can download Python from the official website [Python.org](https://www.python.org/downloads/) and follow the installation instructions for your specific OS.

### 3.3  Installing MySQL Server
Follow the official installation instructions for MySQL based on your OS:
-[MySQL Installation Guide for Linux](https://dev.mysql.com/doc/mysql-installation-excerpt/5.7/en/linux-installation.html)
-[MySQL Installation Guide for macOS](https://dev.mysql.com/doc/mysql-installation-excerpt/5.7/en/macos-installation.html)
-[MySQL Installation Guide for Windows](https://dev.mysql.com/doc/mysql-installation-excerpt/5.7/en/windows-installation.html)

<br>

## 4. Usage  <a name="usage"></a>

1. Create a YAML configuration file that specifies the database details and table structure. See the YAML File Format section for details.
   
2. Run the main.py script with the YAML file as an argument:
```bash
 python main.py your_yaml_file.yaml
```

3. The script will generate the database schema and populate the tables with data based on the configuration in the YAML file.

<br>

## 5. YAML File Format  <a name="yamlfileformat"></a>
``` yaml
mysql:
  host: your_database_host
  user: your_database_user
  password: your_database_password
  database: your_database_name

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


