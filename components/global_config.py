import tkinter as tk
from tkinter import ttk

class ConfigExternalWindow:
    def close_window(self, root : tk.Tk, menu_top, put_menu_options, root_current):
        
        root_current.destroy()
        
        put_menu_options(menu_top)
        
        root.deiconify()