from pathlib import Path

def generate_directories():
    directorios = ["database", 
                   "database/tables"]
    archivos = ["__main__.py", "__init__.py", "README.md"]
    for i in directorios:
        if not(Path.exists(Path.cwd().joinpath(i))):
            Path.mkdir(i)
            for j in archivos:
                route = Path.cwd().joinpath(f"{i}/{j}")
                with open(route, "a+")as file:
                    pass


def generate_databse():
    tablas = ["users"]
    for i in tablas:
        route = Path.cwd().joinpath("database/tables")
        if not(Path.exists(route.joinpath(f"{i}.csv"))):
            with open(f"{route}/{i}.csv", "w", encoding="utf-8", newline="")as file:
                pass


def database_files():
    files = ["create", 
             "update", 
             "delete", 
             "read"]
    for i in files:
        route = Path.cwd().joinpath(f"database/{i}.py")
        with open(route, "a+", encoding="utf8") as file:
            pass

def logic_files():
    files = [""]
    for i in files:
        route = Path.cwd().joinpath(f"logic/{i}.py")
        with open(route, "a+", encoding="utf8") as file:
            pass

def ui_files():
    files = []
    for i in files:
        route = Path.cwd().joinpath(f"ui/{i}.py")
        with open(route, "a+", encoding="utf8") as file:
            pass

print("I must run file called __main__.py")
print(Path.cwd().joinpath("__main__.py"))

if __name__ == "__main__":
    generate_directories()
    generate_databse()