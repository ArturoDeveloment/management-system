import tkinter as tk
from components.partials.layouts.dbs.global_config import ConfigInterface

class DeleteInterface(ConfigInterface):
    def __init__(self, last_root: tk.Toplevel) -> None:
        super().__init__(last_root, "Eliminar Registro", "#A4EFE4")
    
    def widgets(self):
        pass