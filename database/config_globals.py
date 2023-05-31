from pathlib import Path
import csv

class ConfigGlobals:
    def get_id_table(self, name_table):
        id = 1
        route = Path(Path.cwd().joinpath(f"database/tables/{name_table}.csv"))
        if route.exists():
            with open(route, "r", encoding="utf-8", newline = "") as file:
                reader = csv.reader(file)
                for i in reader:
                    column = i[0]
                    id = column if column.isdigit() else 0
        return int(id) + 1