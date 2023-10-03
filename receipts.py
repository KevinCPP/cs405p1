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

def initialize_receipts_table(cursor, logger):
    create_table_cmd = """
    CREATE TABLE IF NOT EXISTS Receipts (
        ID INT AUTO_INCREMENT PRIMARY KEY,
        Location VARCHAR(255),
        BusinessName VARCHAR(255),
        Date DATE,
        TotalSale FLOAT,
        NumberOfItemsSold INT,
        Highest FLOAT,
        Lowest FLOAT,
        BuyerName VARCHAR(255)
    )"""
    cursor.execute(create_table_cmd)
    if logger:
        logger.write(create_table_cmd)

def parse_and_insert_receipts(cursor, raw_receipts, logger):
    for receipt in raw_receipts:
        lines = receipt.strip().split('\n')
        
        print(lines)

        location = lines[0].split(": ")[1]
        business_name = lines[1].split(": ")[1]
        date = lines[2].split(": ")[1]
        total_sale = float(lines[3].split(": ")[1].replace("$", ""))

        num_items_sold = int(lines[4].split(": ")[1])
        
        highest = float(lines[5].split(": ")[1].replace("$", ""))
        lowest = float(lines[6].split(": ")[1].replace("$", ""))
        
        buyer_name = lines[7].split(": ")[1]
        
        insert_cmd = """
        INSERT INTO Receipts (Location, BusinessName, Date, TotalSale, NumberOfItemsSold, Highest, Lowest, BuyerName)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(insert_cmd, (location, business_name, date, total_sale, num_items_sold, highest, lowest, buyer_name))
        if logger:
            logger.write(insert_cmd)

def create_receipts_table(sql_creds, logger):
    conn = connect_to_database(sql_creds)
    if logger:
        logger.write("Begin Receipts Commands:")

    if conn is not None:
        cursor = conn.cursor()

        # Create the Receipts table
        initialize_receipts_table(cursor, logger)

        # Read raw receipts from a text file and parse them
        with open("receipts.txt", 'r') as f:
            raw_receipts = f.read().strip().split("\n\n")  # Assume each receipt is separated by two newlines
        parse_and_insert_receipts(cursor, raw_receipts, logger)

        conn.commit()
        cursor.close()
        conn.close()

