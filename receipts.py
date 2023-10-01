import mysql.connector

def connect_to_database(sql_creds):
    try:
        conn = mysql.connector.connect(host=sql_creds.host,
                                       user=sql_creds.username,
                                       password=sql_creds.password,
                                       database=sql_creds.database)
        print("Successfully connected to the database")
        return conn
    except mysql.connector.Error as err:
        print(f"Something went wrong: {err}")
        return None

def initialize_receipts_table(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Receipts (
        ID INT AUTO_INCREMENT PRIMARY KEY,
        Location VARCHAR(255),
        BusinessName VARCHAR(255),
        Date DATE,
        TotalSale FLOAT,
        NumberOfItemsSold INT
    )""")
    print("Receipts table created successfully")

def parse_and_insert_receipts(cursor, raw_receipts):
    for receipt in raw_receipts:
        lines = receipt.strip().split('\n')
        location = lines[0].split(": ")[1]
        business_name = lines[1].split(": ")[1]
        date = lines[2].split(": ")[1]
        total_sale = float(lines[3].split(": ")[1].replace("$", ""))

        num_items_sold = int(lines[4].split(": ")[1])

        cursor.execute("""
        INSERT INTO Receipts (Location, BusinessName, Date, TotalSale, NumberOfItemsSold)
        VALUES (%s, %s, %s, %s, %s)
        """, (location, business_name, date, total_sale, num_items_sold))

def create_receipts_table(sql_creds):
    conn = connect_to_database(sql_creds)

    if conn is not None:
        cursor = conn.cursor()

        # Create the Receipts table
        initialize_receipts_table(cursor)

        # Read raw receipts from a text file and parse them
        with open("receipts.txt", 'r') as f:
            raw_receipts = f.read().strip().split("\n\n")  # Assume each receipt is separated by two newlines
        parse_and_insert_receipts(cursor, raw_receipts)

        conn.commit()
        cursor.close()
        conn.close()

