import csv 
from pathlib import Path

class CreateRegister:
    def __init__(self, name_table, data : list):
        self.route = Path().cwd().joinpath(f"database/tables/{name_table}.csv")
        self.data = data
        self.registration_unique()
        
    def registration_unique(self):
        with open(self.route, "a", encoding = "utf-8", newline = "") as file:
            writer = csv.writer(file)
            writer.writerow(self.data)
            