from config_files.module_validation_folder import GenerateFolder
from pathlib import Path
from tkinter import messagebox

class CreateFolder(GenerateFolder):
    def __init__(self) -> None:
        super().__init__()
        # apply a negation because found error if it is True
        self.create = not(self.validation())
        # call the function to create folder 
        self.create_folder()
        
    def create_folder(self):
        # validate if it has alredy passed the restriction 
        if self.create:
            # create the folder
            # identify the route and join the name folder
            route = Path(self.route).joinpath(self.name_folder.strip())
            route.mkdir()
            CreateFolder.generate_files(route, self.files)
        # it didnt pass the restriction
        else: 
            
            messagebox.showwarning("Warning", "No es posible crear la carpeta")
    
    @classmethod
    def generate_files(cls, route, files: dict):
        for i, j in files.items():
            file_route = Path(route).joinpath(f"{i}")
            with open(file_route, "a+", encoding="utf-8"):
                pass