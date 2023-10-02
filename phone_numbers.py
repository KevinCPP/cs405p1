
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

# Function to update the Addresses table and add phone numbers
def update_addresses_with_phone_numbers(connection):
    cursor = connection.cursor()
    # Adding a new column for phone numbers in the Addresses table

    cursor.execute("SHOW COLUMNS FROM Addresses LIKE 'phone_numbers';")
    result = cursor.fetchone()
    if result is None:
        # Adding a new column for phone numbers in the Addresses table
        cursor.execute("ALTER TABLE Addresses ADD COLUMN phone_numbers TEXT;")

    # Reading phone numbers from phone_numbers.txt
    with open('phone_numbers.txt', 'r') as file:
        lines = file.readlines()

    # Parsing and updating the phone numbers
    for line in lines:
        name, phone_data = line.strip().split(": ")
        phones = phone_data.split(',')
        phone_str = ', '.join(phones)

        # Update the Addresses table
        update_query = f"UPDATE Addresses SET phone_numbers = %s WHERE EntityName = %s;"
        cursor.execute(update_query, (phone_str, name))

    print("Updated addresses with phone numbers")

    connection.commit()
    cursor.close()

def create_phone_numbers_column(sql_creds):
    # Connect to the database
    connection = connect_to_db(sql_creds.host, sql_creds.username, sql_creds.password, sql_creds.database)
    
    if connection:
        # Update the Addresses table with phone numbers
        update_addresses_with_phone_numbers(connection)
        connection.close()
