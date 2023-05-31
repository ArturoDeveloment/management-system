from components.partials.layouts.dbs import (create,
                                            read,
                                            update,
                                            delete)
from tkinter import messagebox
from pathlib import Path
import csv


delete_ui = lambda root : delete.DeleteInterface(root)

# this fuction get all rows -> the information and header 
def layout_list_columns(tabla_select):
    if tabla_select.get() == "Elija opción":
        messagebox.showerror("ERROR", "No selecciono opción")
        return None
    
    # list colums from table 
    # first list tables 
    route = Path(Path().cwd().joinpath("database/tables"))
    tables = [Path(i) for i in route.iterdir() if ".csv" in str(i)] # list routes
    
    tables_comparation = [str(i.name).replace(".csv", "") for i in tables] # list name tables
    
    index = tables_comparation.index(tabla_select.get()) # get the absolute route 
    
    absolute_route = tables[index]
    # give columns table 
    
    with open(absolute_route, "r", encoding="utf-8", newline="") as file:
        reader = csv.reader(file) # get columns 
        reader = [i for i in reader] # convert iter rows, give the all rows
        
    # return columns
    return reader


def create_register(tabla_select, root):
    
    data_table = {
        "title table": tabla_select.get(),
        "columns": None
    }
    
    # the all rows from database
    reader_columns = layout_list_columns(tabla_select)
    
    data_table["columns"] = reader_columns[0] # give the header
        
    create.CreateInterface(root, data_table) # send data to create register
    
# component for generate the root read.py
def read_registers(tabla_select, root):
    
    data_table = {
        "title table": tabla_select.get(),
        "header": None, 
        "rows": None
    }
    
    reader_columns = layout_list_columns(tabla_select)
    
    if reader_columns != None:
        data_table = {
            "title table": tabla_select.get(),
            "header": reader_columns.pop(0), 
            "rows": reader_columns
        }
        
        read.ReadInterface(root, data_table.get("header"), data_table.get("rows"))
        
def update_register(tabla_select, root):
    
    data_table = {
        "title table": tabla_select.get(),
        "header": None, 
        "rows": None
    }
    
    reader_columns = layout_list_columns(tabla_select)
    
    if reader_columns != None:
        data_table = {
            "title table": tabla_select.get(),
            "header": reader_columns.pop(0), 
            "rows": reader_columns
        }
        
        update.UpdateInterface(root, data_table.get("header"), data_table.get("rows"))