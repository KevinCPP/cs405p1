# Importing the required Python libraries for MySQL connection
import mysql.connector
from mysql.connector import Error

# Function to establish a connection to the MySQL database
def connect_to_db(host, username, password, database):
    try:
        connection = mysql.connector.connect(host=host,
                                             user=username,
                                             password=password,
                                             database=database)
        if connection.is_connected():
            print("Successfully connected to the database")
            return connection
    except Error as e:
        print(f"Error: {e}")
        return None

# Function to close the database connection
def close_db(connection):
    if connection.is_connected():
        connection.close()
        print("Database connection closed")

# Function to create the address table
def initialize_address_table(cursor, logger):
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS Addresses (
        ID INT AUTO_INCREMENT PRIMARY KEY,
        EntityName VARCHAR(255) NOT NULL,
        StreetAddress VARCHAR(255),
        City VARCHAR(50),
        State CHAR(2),
        ZipCode CHAR(5)
    );
    '''
    cursor.execute(create_table_query)
    if logger:
        logger.write(create_table_query)

# Function to insert an address into the address table
def insert_address(cursor, entity_name, street_address, city, state, zip_code, logger):
    insert_query = '''
    INSERT INTO Addresses (EntityName, StreetAddress, City, State, ZipCode)
    VALUES (%s, %s, %s, %s, %s);
    '''
    cursor.execute(insert_query, (entity_name, street_address, city, state, zip_code))
    if logger:
        logger.write(insert_query)

# Function to parse and insert addresses from the file to the database
def parse_and_insert_addresses(cursor, raw_addresses, logger):
    for raw_address in raw_addresses:
        lines = raw_address.split('\n')
        entity_name = lines[0]
        street_address = lines[1]
        city, state_zip = lines[2].split(", ")
        state_zip_split = state_zip.split(" ")
        state = state_zip_split[0]
        zip_code = " ".join(state_zip_split[1:])

        insert_address(cursor, entity_name, street_address, city, state, zip_code, logger)

# Function to read addresses from the file
def read_addresses_from_file(file_path):
    with open(file_path, 'r') as f:
        return f.read().strip().split('\n\n')  # Assume each address is separated by a blank line

def create_addresses_table(sql_creds, logger):
    raw_addresses = read_addresses_from_file('addresses.txt')
    connection = connect_to_db(sql_creds.host, sql_creds.username, sql_creds.password, sql_creds.database)
    if connection is not None:
        cursor = connection.cursor()
        initialize_address_table(cursor, logger)
        parse_and_insert_addresses(cursor, raw_addresses, logger)
        
        # Commit the changes
        connection.commit()
        
        close_db(connection)


