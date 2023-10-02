from addresses import create_addresses_table
from receipts import create_receipts_table
from phone_numbers import create_phone_numbers_column

class SQL_Credentials:
    def __init__(self):
        self.host = "mysql.cs.uky.edu"
        self.username = "knco259"
        self.password = "Papermario2001"
        self.database = self.username

def main():
    # create obj for sql credentials
    sql_creds = SQL_Credentials()

    # create addresses table
    create_addresses_table(sql_creds)
    
    # create receipts table:
    create_receipts_table(sql_creds)

    # add phone number column
    create_phone_numbers_column(sql_creds)

if __name__ == "__main__":
    main() 
