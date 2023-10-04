
# Creating a Logger class that writes messages to an "output.txt" file
class Logger:
    def __init__(self, file_name="output.txt"):
        self.file_name = file_name

    def write(self, message):
        with open(self.file_name, "a") as f:
            f.write(f"{message}\n")

    
