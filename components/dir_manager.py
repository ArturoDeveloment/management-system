import tkinter as tk 
from tkinter import Tk, ttk
from pathlib import Path

class Window:
    
    options = None
    
    def __init__(self):
        # generate and configure the window main tkinter 
        self.root = Tk()
        self.root.title("Manager Directory")
        self.root.resizable(0, 0)
        self.root.config(background="black")
        self.root.geometry("445x165")
        # add funcionalities to the manager window
        
        # component that contain all widgets
        self.menu_top = None
        
        # call widgets to main window
        self.menu_options()
        
        # run the window 
        self.root.mainloop()
        
    def menu_options(self):
        # label_frame for container widgets, manager directories
        self.menu_top = ttk.LabelFrame(self.root, text="Configuracion", padding=5, borderwidth=10)
        self.menu_top.place(x=5, y=5)
        
        # labels to reference 
        directorys_reference = ttk.Label(self.menu_top, text="Seleccione Directorio", font=("arial", 9), background="gray")
        files_reference = ttk.Label(self.menu_top, text="Escriba nombre archivo", font=("arial", 9), background="gray")
        others_options = ttk.Label(self.menu_top, text="Otras opcciones", font=("arial", 9), background="gray")
        
        # widgets to interact
        
        # put the component select option
        self.options = self.put_menu_options(self.menu_top)
        
        # entry space for file name
        file_name = ttk.Entry(self.menu_top, font=("arial",9), justify="right")
        
        # buttons send and create table
        module_create_files = __import__("config_files.module_create_file", fromlist=["module_create_file.py"])
        send_form = ttk.Button(self.menu_top, text="Enviar",takefocus=None, command= lambda : module_create_files.GenerateFiles(self.options[1], file_name))
        generate_directories = ttk.Button(self.menu_top, text="Generar carpeta",takefocus=None, command=lambda: self.create_directories())
        generate_table = ttk.Button(self.menu_top, text = "DataBase",takefocus = None, command = lambda: self.create_to_tables())
        
        # organice grid 
        directorys_reference.grid(row = 0, column = 0, padx=5, pady=5)
        files_reference.grid(row = 1, column = 0, padx=5, pady=5) 
        file_name.grid(row = 1, column =1, padx=5, pady=10)
        send_form.grid(row= 0, column=2, padx=5, pady=5, rowspan=2)
        generate_directories.grid(row= 3, column=2, padx=5, pady=5)
        generate_table.grid(row=3 , column=1, padx=5, pady=5)
        others_options.grid(row=3 , column= 0, padx=5, pady=5)

    # function supported for to use generate relation model
    def create_to_tables(self):
        def close(window):
            # show again the main window 
            self.root.deiconify()
            window.destroy()
        
        # disabled main window 
        self.root.withdraw()
        
        # import directly in a variable for access short
        class_widgets = __import__("components.window_add_dbs", fromlist=["window_add_dbs.py"])
        
        window = tk.Toplevel(self.root)
        window.title("Create tables")
        window.resizable(0, 0)
        window.config(background="black")
        window.geometry("279x149")
        window.protocol("WM_DELETE_WINDOW", lambda:close(window))

        class_widgets.DBSadd(window, self.root, self.menu_top, self.put_menu_options)
    
    # this function create directories 
    def create_directories(self):
        def close(window):
            # show again de main window 
            self.root.deiconify()
            # this variable update menu option by main window 
            self.options[0].destroy()
            self.options = self.put_menu_options(self.menu_top)
            #self.menu_options = self.put_menu_options(self.menu_top)
            window.destroy()
        
        # destroy menu options bt main window
        # the program wait new folders 
        self.options[0].destroy()
        
        # disabled main window 
        self.root.withdraw()
        
        # import directly in a variable for access short
        class_widgets = __import__("components.window_add_folder", fromlist=["window_add_folder.py"])
        
        # initials confurations window
        window = tk.Toplevel(self.root)
        window.title("Create directories")
        window.resizable(0, 0)
        window.config(background="black")
        window.geometry("275x245")
        
        # if close windows catch that action
        window.protocol("WM_DELETE_WINDOW", lambda:close(window))   
        
        # add widgets created in other module 
        class_widgets.FolderAdd(window, self.root, self.menu_top, self.put_menu_options)
    
    # this function is used for give directories now 
    
    def put_menu_options(self, menu_top):
        #used class method for give update directories 
        # the next constructor of list contain
        # the function map for change routes absolutes for only folder name 
        #  used class method and after give the all routes absolutes for just folders
        directorys = list(map(lambda dir : 
            Path(dir).name 
            if len(str(Path(dir).name)) <= 15 
            else 
            str(Path(dir).name)[:14] +"...", Window.directories_now())) 
        # give the title menu option 
        directorys.insert(0, "-- Elija opción --")
        
        # menu is the storage for options to select
        menu = tk.StringVar()
        menu.set(directorys[0])
        
        #options to select the user
        # create the options menu for if exist new directory
        configure_options = lambda directorys, menu :ttk.OptionMenu(menu_top, menu,*directorys) 
        options = configure_options(directorys, menu)
        options.grid(row = 0, column = 1, padx=5, pady=5 )
        
        # return 2 things 
        # 1. the widget (options)
        # 2. menu for get selection
        return (options, menu)
    
    @classmethod
    def directories_now(cls)-> Path:
        # apply filter over main route 
        # get just if is directory
        directories = list(
            filter(lambda route : route
            #validate directoies and apply exception over env and __pycache__
            if route.is_dir() and 
            # apply restrictions some folders
            route.name != "env" and 
            route.name != "__pycache__"  and 
            route.name != "components" and 
            route.name != "files_statics" and 
            route.name != "config_files"
            
            # drop if not directory
            else None, 
            # fill a list with all the files of the main path, and to that we apply the filter
            [i for i in Path.cwd().iterdir()]
        ))
        
        return directories
    
    