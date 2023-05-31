import tkinter as tk
from components.window_add_folder import FolderAdd
from tkinter import ttk, Tk
import json
from pathlib import Path

class DBSadd(FolderAdd):
    # inherit add folder its the same atributes 
    def __init__(self, root: tk.Toplevel, root_main: Tk, menu_top: ttk.LabelFrame, fuction_put_menu):
        super().__init__(root, root_main, menu_top, fuction_put_menu)
        self.contend_widgets = tk.LabelFrame(self.root, text="Agregar Base de datos")
        self.contend_widgets.place(x = 5, y = 5)
        self.components()
        
    def components(self):
        # add widgets to interface add dbs 
        label_name_table = ttk.Label(self.contend_widgets, text= "Nombre tabla")
        # name table
        name_table = ttk.Entry(self.contend_widgets)
        # label for column number
        label_column_number = ttk.Label(self.contend_widgets, text= "Número de columnas")
        # number columns 
        catch_number = tk.IntVar()
        column_number = tk.Scale(self.contend_widgets, variable = catch_number, from_ = 1, to = 15, orient = tk.HORIZONTAL)
        
        # button send information 
        button_send = ttk.Button(self.contend_widgets, text = "Enviar", command= lambda : DBSadd.load_json(name_table, catch_number, self.root_main,self.root))
        
        # config other DBS with CRUD
        button_config = ttk.Button(self.contend_widgets, text = "CRUD", command= lambda : DBSadd.open_window_crud(self.root))
        
        # config grid
        label_name_table.grid(row = 0, column= 0, padx = 5, pady = 5)
        name_table.grid(row = 0, column = 1, padx = 5, pady = 5)
        label_column_number.grid(row = 1, column = 0, padx = 5, pady = 5)
        column_number.grid(row = 1, column = 1, padx = 5, pady = 5)
        button_send.grid(row = 2, column = 1, padx = 5, pady = 5)
        button_config.grid(row = 2, column = 0, padx = 0, pady = 0)

    
    @staticmethod
    def open_window_crud(root):
        # open window crud
        window = __import__("components.partials.crud_dbs", fromlist=["crud_dbs.py"])
        window.CRUD(root)
    
    @staticmethod
    def load_json(name_table : ttk.Entry, num_columns : tk.Scale, root_last, root_current):
        
        
        info = [{
            "name_table": name_table.get(),
            "num_columns": num_columns.get()
        }]
        
        name_table.delete(0, tk.END)
        num_columns.set(1)
        
        info = json.dumps(info)
        
        Path(Path.cwd().joinpath("files_statics/info.json")).write_text(info, encoding="utf-8")
        
        export = __import__("config_files.module_create_dbs", fromlist=["module_create_dbs.py"])
        export.GenerateDBS(root_current, root_last)