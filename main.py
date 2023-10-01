from addresses import create_addresses_table
from receipts import create_receipts_table

class SQL_Credentials:
    def __init__(self):
        self.host = "mysql.cs.uky.edu"
        self.username = "knco259"
        self.password = "<password>"
        self.database = self.username

def main():
    # create obj for sql credentials
    sql_creds = SQL_Credentials()

    # create addresses table
    create_addresses_table(sql_creds)
    
    # create receipts table:
    create_receipts_table(sql_creds)

if __name__ == "__main__":
    main() 
