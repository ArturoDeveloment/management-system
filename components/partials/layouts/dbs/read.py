import tkinter as tk
from components.partials.layouts.dbs.global_config import ConfigInterface
from tkinter import ttk
from pathlib import Path

class ReadInterface(ConfigInterface):
    def __init__(self, last_root: tk.Toplevel, header, rows) -> None:
        super().__init__(last_root, "Leer Registro", "#A4EFE4")
        self.header = header
        self.rows = rows
        self.widgets()
    
    def widgets(self):
        # Crear tabla 
        table = ttk.Treeview(self.canvas)
        table.pack()
        
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