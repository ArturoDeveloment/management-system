from pathlib import Path
import json
from tkinter import messagebox

class GenerateFolder:
    def __init__(self) -> None:
        # if user is creating a new directory update json 
        self.json_load = self.create_json()
        self.route = self.json_load[0].get("route")
        self.files = self.json_load[0].get("files")
        self.name_folder = str(self.json_load[0].get("name_folder"))
        self.reference = self.json_load[0].get("create")
    
    # This function have updated json
    @classmethod
    def create_json(cls):
        # return json 
        return json.loads(Path(Path.cwd().joinpath("files_statics/info.json")).read_text(encoding="utf-8"))
    
    # this function realize validationes about creation the folder 
    def validation(self):
        # variable for catch error's
        error = False
        
        # verify if user want create directory
        if self.reference != "directory":
            messagebox.showerror("ERROR", "Error al crear un directorio")
            error = True
        
        # create list for validation 
        letter_upper = [chr(i) for i in range(65, 91)]
        letter_lower = [chr(i) for i in range(97, 123)]
        numbers = [str(i) for i in range(10)]
        
        # these charact cant to be used for put name to directory
        validate_characters = [chr(i) for i in [33, 35, 36, 37, 38, 40, 41, 42, 43, 44, 45, 46, 47, 58, 59, 61, 63, 64, 92, 93, 95, 123, 124, 125]]
        
        # this fuction make iteration above string and validate a list elements and his output is a bool
        def validate(string, validate: list)-> bool:
            for i in string:
                # if it is sucess full, it will returning bool
                if i in validate:
                    return True
            return False
        
        # verify folder name, it can throw a error  
        # 1 condicion delete the spaces and check that dont have empty 
        # 2 condition check that dont have numbers 
        # 3 and 4 condicion check that name start with letter (it used the compress list with focus ASCII)
        # 5 condition check that name start with some character and the name could contain any elemnts
        
        if (
            (self.name_folder.strip() == "") or # is empty # start with numbers
            (validate(self.name_folder, validate_characters)) or # cotain special charcters
            not(
                (validate(self.name_folder, letter_lower)) or 
                (validate(self.name_folder, letter_upper)) or 
                (validate(self.name_folder, numbers))
            ) # contain any (letter upper or lower or number)
        ):
            messagebox.showerror("ERROR", "Nombre de la carpeta incorrecto")
            error = True
        
        # self.files only storage the files that could be creates
        files_to_create = {}
        # verify what files dont be create
        for i, j in eval(self.files).items():
            if j != None:
                files_to_create[i] = j
        self.files = files_to_create
        
        # if that directory exist, then it would not be created

        try:
            # test the exist path
            directorys = Path(self.route).iterdir() # verify the route
            
            # if the directory exist, it will throw a error
            for i  in directorys:
                if (i.name == self.name_folder.strip()): # delete white spaces, because throw errors
                    messagebox.showerror("ERROR", "Ese directorio ya existe")
                    error = True
        except Exception as e:
            messagebox.showerror("ERROR", "Ese directorio ya existe")
            error = True
                    
        return error
