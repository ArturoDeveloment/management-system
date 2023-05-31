import tkinter as tk
from tkinter import ttk
from components.partials.layouts.dbs.global_config import ConfigInterface

class UpdateInterface(ConfigInterface):
    def __init__(self, last_root: tk.Toplevel, header, rows) -> None:
        super().__init__(last_root, "Actualizar Registro", "#A4EFE4")
        self.header = header
        self.rows = rows
        self.widgets()
    
    def widgets(self):
        # Crear tabla 
        table = ttk.Treeview(self.canvas)
        
        
        # definimos las columnas
        table['columns'] = self.header
        
        # se da una cabecera
        table.heading("#0", text='Fila n°')
        
        # tamaño de la columna
        table.column("#0", width=100)
        # Insertamos a la tabla columna por columna 
        for columna in table['columns']:
            table.heading(columna, text=columna)
            table.column(columna, width=100)

        # Insertar datos a la tabla 
        for indice, elemento in enumerate(self.rows):
            table.insert('', 'end', text=f'Fila {indice + 1}', values=elemento)

        button_select = ttk.Button(self.root, text="Seleccionar id", command=lambda: self.register_select())
        button_select.pack(padx=(0, 10), side="right")
        
        table.pack()
    
    def register_select(self):
        self.root.withdraw()
        id_list = [i + 1 for i in range(len(self.rows))]
        id_list.insert(0, "Elije opcion")
        root = tk.Tk()
        storage = tk.StringVar()
        storage.set(id_list[0])
        selector_table = ttk.OptionMenu(root, storage, *id_list)
        selector_table.pack()
        root.mainloop()