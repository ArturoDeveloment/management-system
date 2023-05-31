from pathlib import Path
import csv

class GenerateDBS:
    def __init__(self, name_table, columns : list):
        self.route = Path(Path.cwd().joinpath(f"database/tables/{name_table}.csv"))
        self.table = name_table
        self.columns = columns
        self.open_table()
    
    def open_table(self):
        with open(self.route, "a", encoding= "utf-8", newline="") as file:
            writer_header = csv.writer(file)
            writer_header.writerow(self.columns)