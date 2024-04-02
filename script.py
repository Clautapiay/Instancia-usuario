import json

class Usuario():
    def __init__(self, nombre: str, apellido: str, email: str, genero: str) -> None:
        self.nombre = nombre
        self.apellidos = apellido
        self.email = email
        self.genero = genero

    def __str__(self):
        return f"Nombre:{self.nombre} , Apellido: {self.apellidos} , Email:{self.email} , Genero:{self.genero}"

instancias = [] 
# with open("usuarios_corregido.txt") as usuarios:
with open("usuarios.txt") as usuarios:
    linea = usuarios.readline()
    while linea:
        usuario = json.loads(linea) # dict
        instancias.append(Usuario(usuario.get("nombre"), usuario.get("apellido"), usuario.get("email"), usuario.get("genero")))
        

        linea = usuarios.readline() #next


for i in instancias:
    print(i)

    instancias = []
    # with open("usuarios_corregido.txt") as usuarios:
    with open("usuarios.txt") as usuarios:
        linea = usuarios.readline()   
        while linea:
            try:
                usuario = json.loads(linea) # dict
                instancias.append(Usuario(usuario.get("nombre"), usuario.get("apellido"), usuario.get("email"), usuario.get("genero")))
        
            except Exception as e:
                with open("usuarios_error.log", "a") as log:
                    log.write(f"ERROR: {e}")
            finally: 
                linea = usuarios.readline()
    
    with open("usuarios_error.log", "a") as log_file:
        errores = log_file.read()

print(errores)
