from tkinter import ttk
import tkinter as tk

class GenerateFiles:
    def __init__(self, route : tk.StringVar = None, name_file : ttk.Entry = None) -> None:
        self.route = route
        self.name_file = name_file
        self.get_data()
    def get_data(self):
        files = None
        route = None
        try:
            route = self.route.get()
            if route == "-- Elija opción --":
                route = None
                return {"folder_name": route, "name file": files}
            files = self.name_file.get()
            self.name_file.delete(0, tk.END)
        except Exception as e:
            print(e)
        
        return {"folder_name": route, "name file": files}