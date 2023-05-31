from tkinter import ttk, messagebox
import tkinter as tk
import json
from pathlib import Path


class ComponentsAddColumns:
    def __init__(self, name_table, num_columns, canvas, root, last_root : tk.Tk) -> None:
        # Constructor de la clase ComponentsAddColumns
        self.last_root = last_root
        self.root = root
        self.number_columns = num_columns
        self.canvas = canvas
        self.name_table = name_table
        self.widgets = self.components()  # Es un diccionario con todas las columnas

    def components(self):
        # Crea y muestra los componentes de la interfaz gráfica
        title = ttk.Label(self.canvas, text=f"Sección para agregar columnas\nTabla: {self.name_table}",
                        font=("arial", 14))
        title.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        # Este diccionario guarda las entradas (nombres de las columnas)
        dict_columns = {}

        grid = [0, 0]

        for i in range(self.number_columns):
            label = ttk.Label(self.canvas, text=f"Columna {i+1}", font=("arial", 8))
            entry = ttk.Entry(self.canvas, font=("arial", 8), justify="right")
            if i == 0:
                # Configura la primera columna como "id" y la deshabilita
                entry.insert(tk.END, "id")
                entry.config(state="disabled")

            dict_columns[i] = entry

            grid[0] += 1
            grid_label = [grid[0], grid[1]]

            grid[1] += 1
            grid_entry = [grid[0], grid[1]]

            label.grid(row=grid_label[0], column=grid_label[1], padx=5, pady=5)
            entry.grid(row=grid_entry[0], column=grid_entry[1], padx=5, pady=5)

            grid[1] = 0

        button_enviar = ttk.Button(self.canvas, text="Generar columna", command=self.validations_colums)
        grid[0] += 1
        button_enviar.grid(row=grid[0], column=grid[1], columnspan=2, padx=5, pady=10)

        return dict_columns

    def get_height(self):
        # Calcula la altura necesaria para mostrar todos los componentes en la interfaz gráfica
        height = 80
        additional_height = 30 * self.number_columns
        button_height = 50
        return height + additional_height + button_height

    def validations_colums(self):
        # Realiza validaciones en los nombres de las columnas ingresados
        dict_data = []
        for key in self.widgets:
            # Itera sobre las claves del diccionario de widgets
            column_name = self.widgets.get(key).get()
            error = self.validate_name(column_name)
            if error:
                # Si hay un error de validación en el nombre de la columna:
                # - Borra el contenido de la entrada correspondiente
                self.widgets.get(key).delete(0, tk.END)
                # - Muestra un mensaje de error con el número de columna afectada
                messagebox.showerror("ERROR", f"Ese error corresponde a la columna {key+1}")
                continue
            
            elif column_name in dict_data:
                error = True
                # si la columna no existe 
                messagebox.showerror("ERROR", "Hay una columna repetida")
                self.widgets.get(key).delete(0, tk.END)
                messagebox.showerror("ERROR", f"Ese error corresponde a la columna {key+1}")
                continue
            
            dict_data.append(column_name)
        if not(error):
            # Si no hay errores en ninguna columna:
            self.root.destroy()
            self.last_root.deiconify()
            
            # importamos la generadora de la base de datos y cargamos los datos 
            generate_table = __import__("database.generate_table", fromlist = ["generate_table.py"])
            generate_table.GenerateDBS(self.name_table, dict_data)

    def validate_name(self, name : str):
        # validate characters for name table 
        # this character id permmited 
        """
        ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '_', '-', '']
        """
        characters = [chr(i) for i in range(97, 123)] + [chr(i) for i in range(65, 91)] + [chr(i) for i in range(48, 58)] + ["_", "-", ""]
        
        # it have to name maxium 15 characters
        error = False # this variable find error 
        
        if len(name) > 15:
            error = True
            messagebox.showerror("ERROR", "El nombre rebasa el máximo de caracteres permitidos")
            return error
        
        if name.strip() == "":
            error = True
            messagebox.showerror("ERROR", "El campo está vacio")
            return error
        
        # apply iteration for string and verify that each character this one in the characters permmited 
        for i in name:
            if i not in characters:
                error = True
                messagebox.showerror("ERROR", f"El nombre tiene characteres no permitidos '{i}'")
                return error
        
        return error

    # cargamos un json con las columnas definidas 