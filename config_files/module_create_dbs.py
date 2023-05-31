import json
from pathlib import Path
from tkinter import messagebox
import tkinter as tk

class GenerateDBS:
    def __init__(self, root_current : tk.Toplevel = None, root_last = None):
        self.json = json.loads(Path(Path.cwd().joinpath("files_statics/info.json")).read_text(encoding="utf-8"))
        self.root_current = root_current
        self.root_last = root_last
        self.validate_dbs()
        
    def validate_dbs(self):
        info = self.json[0]
        name_table = info.get('name_table')
        num_columns = info.get('num_columns')
        error = self.validate_name(name_table)
        
        #        In this step is needs a graphic interface for Register all columns for the user
        #        for that reason the program reuse the layouts from dbs "global_config" and inheit the class "ConfigInterface"
        #        just the program should do fill with columns and entrys for name colums
        # give the class for thhis module
        if error:
            messagebox.showerror("ERROR", "Vuelva a intentar")
            return None
        # open new interface and delete current interface 
        self.root_current.destroy()
        configInterface = __import__("components.partials.layouts.dbs.global_config", fromlist=["global_config.py"])
        
        # the program wait, if user clicked in exit windows, the program must sent back, i mean the principal interface 
        configInterface = configInterface.ConfigInterface(self.root_last, "Configuración de columnas", "#DE6D6D", 300, 300)

        # add components, first import package, it have components 
        # import components
        components = __import__("components.partials.layouts.dbs.components_add_columns", fromlist=["components_add_columns.py"])
        components = components.ComponentsAddColumns(name_table, num_columns, configInterface.canvas, configInterface.root, self.root_last)
        
        configInterface.root.geometry(f"{300}x{components.get_height()}")
        

    def validate_name(self, name : str):
        # validate characters for name table 
        # this character id permmited 
        """
        ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '_', '-', '']
        """
        characters = [chr(i) for i in range(97, 123)] + [chr(i) for i in range(65, 91)] + [chr(i) for i in range(48, 58)] + ["_", "-", ""]
        
        # it have to name maxium 15 characters
        error = False # this variable find error 
        
        if len(name) > 13:
            error = True
            messagebox.showerror("ERROR", "El nombre rebasa el máximo de caracteres permitidos")
            return error
        
        if name.strip() == "":
            error = True
            messagebox.showerror("ERROR", "El nombre está vacio")
            return error
        
        # apply iteration for string and verify that each character this one in the characters permmited 
        for i in name:
            if i not in characters:
                error = True
                messagebox.showerror("ERROR", f"El nombre tiene characteres no permitidos '{i}'")
                return error
        
        # verify if this name is not exist ride now
        # if this name is exist, return error
        route_tables = Path(Path.cwd().joinpath("database/tables")).iterdir()
        # delete .csv, this do it easier verify 
        route_tables = list(map(lambda route : route.name, route_tables))
        route_tables = [i.replace(".csv", "") for i in route_tables if ".csv" in i] # split .csv
        
        if name in route_tables:
            error = True
            messagebox.showerror("ERROR", f"La tabla {name} ya existe")
            return error
        return error
