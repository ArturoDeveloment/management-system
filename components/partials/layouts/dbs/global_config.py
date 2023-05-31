import tkinter as tk
from tkinter import ttk

class ConfigInterface:
    def __init__(self, last_root : tk.Toplevel, title : str, color : str, width : int = None, height : int = None) -> None:
        self.last_root = last_root
        self.last_root.withdraw()
        self.root = tk.Toplevel(self.last_root)
        self.root.title(title)
        self.root.resizable(0, 0)
        if width != None and height != None:
            self.root.geometry(f"{width}x{height}")
        self.root.configure(bg =color)
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        self.canvas = tk.Canvas(self.root)
        self.canvas.pack(side = tk.LEFT, fill= tk.Y, padx= 5, pady= 5)

        
    def close(self):
        
        self.root.destroy()
        
        self.last_root.deiconify()