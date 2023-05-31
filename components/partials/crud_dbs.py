import tkinter as tk 
from tkinter import ttk
from pathlib import Path
# import individual interfaces for CRUD
from components.partials.layouts.dbs.call_ui import (create_register,
                                                    read_registers, 
                                                    update_register)

class CRUD:
    # route databse 
    route_tables = Path(Path.cwd().joinpath("database/tables"))
    
    # constructor for window 
    def __init__(self, root : tk.Toplevel) -> None:
        # last window 
        self.root = root
        # window corrent 
        self.root_crud = self.window_crud()
        # config current window and hidden last root 
        CRUD.components(self.root_crud)
        CRUD.config(self.root, self.root_crud)
    
    # create current window 
    def window_crud(self):
        root_crud = tk.Toplevel(self.root)
        root_crud.title("CRUD")
        root_crud.config(background="Black")
        root_crud.resizable(1, 1)
        root_crud.geometry("235x135")
        return root_crud
    
    @classmethod
    def components(cls, root : tk.Toplevel):
        # widgets for current wundow 
        
        # contend for widgets
        contend_widgets = ttk.LabelFrame(root, text= "Configurar DBS")
        contend_widgets.place(x = 5, y = 5)
        
        # widgets specific in contend widgets 
        
        # label do it reference to select table 
        label_table = ttk.Label(contend_widgets, text = "Tabla: ")
        
        # selector tables 
        # The static fuction return tables (CRUD.list_tables())
        storage = tk.StringVar()
        storage.set(CRUD.list_tables()[0])
        selector_table = ttk.OptionMenu(contend_widgets, storage, *CRUD.list_tables())
        
        # botons for CRUD 
        btn_create = ttk.Button(contend_widgets, text = "Crear Registro", command= lambda : create_register(storage, root))
        btn_read = ttk.Button(contend_widgets, text = "Listar Registro", command= lambda : read_registers(storage, root))
        btn_update = ttk.Button(contend_widgets, text = "Cambiar Registro", command=lambda : update_register(storage, root))
        btn_delete = ttk.Button(contend_widgets, text = "Eliminar Registro")
        
        # organice the grid 
        label_table.grid(row = 0, column = 0, padx=5, pady=5)
        selector_table.grid(row = 0, column = 1, padx=5, pady=5)
        btn_create.grid(row=1, column=0, padx=5, pady=5)
        btn_read.grid(row=1, column=1, padx=5, pady=5)
        btn_update.grid(row=2, column=0, padx=5, pady=5)
        btn_delete.grid(row=2, column=1, padx=5, pady=5)
        
    # config current and last window 
    @classmethod
    def config(cls, root : tk.Toplevel, root_crud : tk.Toplevel):
        # if user touch close window 
        def close_window():
            # destroy and show last window 
            root_crud.destroy()
            root.deiconify()
        # hidden last window 
        root.withdraw()
        # touch close window 
        root_crud.protocol("WM_DELETE_WINDOW", close_window)
    
    # this fuction help for list tables (check)
    @staticmethod
    def list_tables()-> list:
        route = CRUD.route_tables
        tables = list()
        # if tables exist
        if (route.exists()):
            # return tables
            tables = list(filter(lambda table : Path(table) if Path(table).is_file and ".csv" in str(Path(table)) else None, route.iterdir()))
            # change format tables -> route to name -> cut route or apply reduce 
            tables = list(map(lambda 
                            route : str(Path(route).name).replace(".csv", "") 
                            if len(str(Path(route).name).replace(".csv", "")) <= 13 
                            else 
                            # if route very longer, reduce his lenght
                            str(Path(route).name).replace(".csv", "")[:15]+"...", tables))
        tables.insert(0, "Elija opción")
        return tables