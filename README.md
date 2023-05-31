**** Storage Aplication ***

You must run file __main__ to main directory and configure in file __init__

The file __init__
this file contains some functions, it is the next functions 
1. generate directories 
2. generate main files __init__, __main__ in each directory generate with the last function
3. generate the tables at directory  database/tables 
4. the __init__ file contains 3 similar functions, about each function generate files on each principal directories these are called database, logic, ui

The file __main__
this file save the code execution principal
YOU MUST RUN THIS FILE
this file will call the others directories and all files of that directory
the all logic is called above this file (__main__.py)

**** will continue to explain the structured folders ****

folder part 1
    [components]
    This folder contains all graphics interfaces, it is divided into other folders, but before will explain this structured. components contain global layouts, such as add_dbs, add_floder and other module for gloabl configurations
    [partials]
    This folder contains aditionals design, such as crud and contain other folder, such as 
    [layouts]
    contain all specifict design, that it would use, in this case, contain layout for partial-crud_dbs, it have the next layouts folder with desigs or layouts specifc, and 1 file with a layout global for to receive the layouts most specific

folder part 2
    [config_files]