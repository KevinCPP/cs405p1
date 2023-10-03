from addresses import create_addresses_table
from receipts import create_receipts_table
from phone_numbers import create_phone_numbers_column
from logger import Logger

class SQL_Credentials:
    def __init__(self):
        self.host = "mysql.cs.uky.edu"
        self.username = "knco259"
        self.password = "<password>"
        self.database = self.username

def main():
    # create obj for sql credentials
    sql_creds = SQL_Credentials()
    logger = Logger()

    # create addresses table
    create_addresses_table(sql_creds, logger)
    
    # create receipts table:
    create_receipts_table(sql_creds, logger)

    # add phone number column
    create_phone_numbers_column(sql_creds, logger)

if __name__ == "__main__":
    main() 
