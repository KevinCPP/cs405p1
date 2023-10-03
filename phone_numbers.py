
# Importing required Python libraries for MySQL connection and file handling
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
            return connection
    except Error as e:
        print(f"Error: {e}")
        return None

def parse_phone_numbers(cursor, raw_addresses, logger):
    for raw_address in raw_addresses:
        lines = raw_address.split('\n')
        name = lines[2].split(": ")[1].strip()
        raw_phone_number = lines[7].split(": ")
        if len(raw_phone_number) > 1:
            phone_number = raw_phone_number[1].strip() 
        
        print(f"updating \"{name}\" with phone number: \"{phone_number}\"")
        update_query = f"UPDATE Addresses SET phone_numbers = %s WHERE EntityName = %s;"
        cursor.execute(update_query, (phone_number, name))
        if logger:
            logger.write(update_query)

# Function to read addresses from the file
def read_phone_numbers_from_file(file_path):
    with open(file_path, 'r') as f:
        return f.read().strip().split('\n\n')  # Assume each address is separated by a blank line

# Function to update the Addresses table and add phone numbers
def update_addresses_with_phone_numbers(connection, logger):
    cursor = connection.cursor()
    # Adding a new column for phone numbers in the Addresses table

    cursor.execute("SHOW COLUMNS FROM Addresses LIKE 'phone_numbers';")
    result = cursor.fetchone()
    if result is None:
        # Adding a new column for phone numbers in the Addresses table
        new_column_cmd = "ALTER TABLE Addresses ADD COLUMN phone_numbers TEXT;"
        cursor.execute(new_column_cmd)
        if logger:
            logger.write(new_column_cmd)

    raw_addresses = read_phone_numbers_from_file("phone_numbers.txt")

    # Parsing and updating the phone numbers
    parse_phone_numbers(cursor, raw_addresses, logger)

    print("Updated addresses with phone numbers")

    connection.commit()
    cursor.close()

def create_phone_numbers_column(sql_creds, logger):
    # Connect to the database
    connection = connect_to_db(sql_creds.host, sql_creds.username, sql_creds.password, sql_creds.database)
   
    if logger:
        logger.write("Begin Phone Numbers Commands:")

    if connection:
        # Update the Addresses table with phone numbers
        update_addresses_with_phone_numbers(connection, logger)
        connection.close()
