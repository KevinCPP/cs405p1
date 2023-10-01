from addresses_generator import generate_text_file
from addresses import create_addresses_table

class sql_credentials:
    def __init__(self):
        username = "knco259"
        password = "<password>"
        database = username

if __name__ == "__main__":
    # generate addresses.txt
    generate_text_file()
    
    # create addresses table
    create_addresses_table(sql_credentials)
      
