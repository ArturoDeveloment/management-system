import tkinter as tk
from tkinter import filedialog, messagebox
from pathlib import Path
from tkinter import ttk
import json

class FolderAdd:
    # variable that apply control about route create folder
    route = None
    
    def __init__(self, root : tk.Toplevel, root_main : tk.Tk, menu_top : ttk.LabelFrame, fuction_put_menu):
        self.root = root
        # created frame contend widgets for add folder 
        self.contend_widgets = tk.LabelFrame(root, text="Agregar Carpeta")
        self.contend_widgets.place(x = 5, y = 5)
        
        # add widgets to main window 
        self.components()
        
        # this variables will help close this window and update the main root
        self.root_main = root_main
        self.menu_top = menu_top
        self.function = fuction_put_menu
        
    def components(self):
        # catch route selected 
        route_selected = ttk.Entry(self.contend_widgets)
        
        # button for open de explorar to selected folder 
        selected_button = ttk.Button(self.contend_widgets, text="Seleccionar Carpeta", command=lambda : FolderAdd.open_explorer(route_selected))
        
        # label for create directory
        name_directy = ttk.Label(self.contend_widgets, text = "Nombre Carpeta", font=("arial", 8))
        
        # entry space for a name bynew directory
        entry_directory = ttk.Entry(self.contend_widgets)
        
        # files adicionals
        name_file_aditionals = ttk.Label(self.contend_widgets, text="Archivos Adicionales\nPara el directorio", font=("arial", 8))
        
        # variables catch for the checkbox
        file_main = tk.IntVar()
        file_init = tk.IntVar()
        file_readme = tk.IntVar()
        
        #frame to storage the checkbox
        frame_checkbox = ttk.Frame(self.contend_widgets)
        
        # create the checkbox
        file_main_check = tk.Checkbutton(frame_checkbox, text="__main__.py", variable=file_main)
        file_init_check = tk.Checkbutton(frame_checkbox, text="__init__.py", variable=file_init)
        file_readme_check = tk.Checkbutton(frame_checkbox, text="README.md", variable=file_readme)
        
        # dict checkbox for verify in the same time 
        checkbox = {"__main__.py" : file_main, "__init__.py" : file_init, "README.md" : file_readme}
        
        # button send information
        send_information = ttk.Button(self.contend_widgets, text="Crear Carpeta", command= lambda: self.load_information_json(checkbox, entry_directory))
        
        # organice the widgets with grid 
        selected_button.grid( row = 0, column = 0, padx = 5, pady = 5 )
        route_selected.grid(row = 0, column= 1, padx = 5, pady = 5)
        name_directy.grid(row = 1, column = 0, padx=5, pady=5)
        entry_directory.grid(row=1, column=1, padx=5, pady=5)
        name_file_aditionals.grid(row=2, column= 0, padx=5, pady=5)
        frame_checkbox.grid(row=2, column=1, padx=5, pady=5)
        send_information.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
        file_main_check.grid(row=0, column=0, padx=5, pady=5)
        file_init_check.grid(row=1, column=0, padx=5, pady=5)
        file_readme_check.grid(row=2, column=0, padx=5, pady=5)
        
    # function is used for selector folder
    @classmethod
    def open_explorer(cls, text : ttk.Entry):
        # open the new window by explorer.exe
        # you can select a folder
        route = Path(filedialog.askdirectory(initialdir=Path.cwd(), title="Seleccionar direccíon"))
        route_root = Path.cwd()
        # if user selected directory out range root directory
        if str(route_root) not in str(route):   
            answer = messagebox.showerror("Error", "No selecciono ningún directorio") if str(route) == "." else messagebox.showerror("Error Directory", "out range root folder") 
            # configure the entry directory
            text.config(state="active")
            text.delete(0, "end")
            # out
            return None

        # modify the class variable 
        cls.route = route
        text.config(state="active")
        text.delete(0, "end")
        # update route -> design root/
        route_cut = "root/" + str(route).replace("\\", "/").split("/")[-1] + "/"
        text.insert(0, route_cut)
        text.config(state="disabled")
        
        # return root selected for user
        return route

    # this function generate the files json with information about generate the new diectories
    def load_information_json(self, checkbox : dict, name_directory : ttk.Entry) -> json:
        # load the route for create the directories
        route = FolderAdd.route
        # load files that user choise
        for i, j in checkbox.items():
            if j.get() == 1:
                checkbox[i] = j.get()
                continue
            checkbox[i] = None
        # load the name directory
        name_folder = name_directory.get()
        
        # load information
        information = [
            {
            "route" : str(route),
            "files" : str(checkbox),
            "name_folder" : name_folder,
            "create" : "directory"
            }
            ]
        
        # convert the list->dict to json
        information = json.dumps(information)
        
        messagebox.showinfo("Directorio", "Espere a verificación de información")
        
        
        # return json
        Path(Path.cwd().joinpath("files_statics/info.json")).write_text(information, encoding="utf-8")
        
        # create folder 
        importation = __import__("config_files.module_create_folders", fromlist=["module_create_folders.py"])
        importation.CreateFolder()
        
        #Import tools delete this window, update main window 
        importation = __import__("components.global_config", fromlist=["global_config.py"])
        objecto = importation.ConfigExternalWindow()
        objecto.close_window(self.root_main, self.menu_top, self.function, self.root)