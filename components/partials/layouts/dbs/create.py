import tkinter as tk
from components.partials.layouts.dbs.global_config import ConfigInterface
from tkinter import ttk, messagebox

class CreateInterface(ConfigInterface):
    def __init__(self, last_root: tk.Toplevel, data : dict = None) -> None:
        self.data = data
        super().__init__(last_root, "Crear Registro", "#A4EFE4", 270, self.height_all())
        self.entries = self.widgets()
        self.columns = []
        

    # configuration height for the window root 
    def  height_all(self):
        columns = len(self.data.get('columns'))
        columns = columns * 30
        return 80 + columns + 50
    
    # components
    def widgets(self)-> dict:

        label_title = ttk.Label(self.canvas, text= f"Creación de nuevo registro \ntabla: {self.data.get('title table')[0:15] if self.data.get('title table') != None else None}", font=("arial", 14))
        label_title.grid(row=0, column=0, columnspan=3, padx= 10, pady=10)
        
        widgets = dict()
        
        grid = [0, 0]
        for i in self.data.get('columns'):
            label = ttk.Label(self.canvas, text = i[0:12], font=("arial", 8))
            entry = ttk.Entry(self.canvas, font=("arial", 8), justify= "right")
            if i == "id":
                # importamos el sacador de id de cada tabla 
                export = __import__("database.config_globals", fromlist= ["config_globals.py"]).ConfigGlobals().get_id_table(self.data.get('title table'))
                export = export if export != "id" else 1
                entry.insert(tk.END, export)
                entry.config(state="disabled")
            widgets[i] = entry # add widget for diccionary
            grid[0]+= 1
            grid_label = [grid[0], grid[1]]
            
            grid[1]+=1
            grid_entry = [grid[0], grid[1]]
            
            label.grid(row=grid_label[0], column=grid_label[1], padx=5, pady=5)
            entry.grid(row=grid_entry[0], column=grid_entry[1], padx=5, pady=5)

            grid[1]= 0
        
        button_enviar = ttk.Button(self.canvas, text= "Enviar dataset", command=lambda: self.validations())
        grid[0] += 1
        button_enviar.grid(row= grid[0], column=grid[1], columnspan=2, padx=5, pady=10)
        
        return widgets
    
    # this function validate if all columns is correct
    def validations(self):
        message_alert = ""
        # verify if spaces entries is empty
        for column, valor in self.entries.items():
            if valor.get().strip() == "":
                message_alert += f"La columna '{column}' está vacia\n"
            if "," in valor.get():
                messagebox.showwarning("Warning", f"La columna '{column}' tiene ',' se interpretara como vacio\n") 
                valor.delete(0, tk.END)
        else:
            message_alert += "Desea guardar cambios? "
        
        response = messagebox.askquestion("Guardar cambios", message_alert, icon="question")
        
        if response == "yes":
            for column, valor in self.entries.items():
                if valor.get().strip() == "":
                    valor.insert(tk.END, "null")
            self.columns = [j.get() for i, j in self.entries.items()]
            self.load_info_dbs()
            self.close()
        else:
            response = messagebox.askquestion("Salir", "Desea realizar los cambios", icon="question")
            if response == "no":
                self.close()
                
    def load_info_dbs(self):
        export_dbs = __import__("database.create_register", fromlist = ["create_register.py"])
        export_dbs.CreateRegister(self.data.get('title table'), self.columns)