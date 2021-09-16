import os

### VARIABLES ###

SEGUNDO_BACHILLER = ["Historia_de_Espana", "Lengua_Castellana_Literatura", "Matemáticas II", "Matematicas_Sociales_II", "Biologia", "Dibujo_Tecnico_II", "Fisica", "Geologia", "Quimica", "Geografia"]
PRIMERO_BACHILLER = ["Matematicas I", "Filosofia", "Matematicas_Sociales I", "Lengua", "Biologia_Geologia", "Dibujo_Tecnico I", "Fisica y Quimica", "Economia"]
CUARTO_ESO = ["Historia", "Lengua_Castellana_Literatura", "Matematicas_A", "Matematicas_B", "Biologia_Geologia", "Fisica_Quimica", "Informatica"]

cursos = {"SEGUNDO_BACHILLER":SEGUNDO_BACHILLER, "PRIMERO_BACHILLER": PRIMERO_BACHILLER, "CUARTO_ESO":CUARTO_ESO}

### Script ###

def CrearArbol(path):

    for nombre, curso in cursos.items():

        for asignatura in curso:

            try:
                os.makedirs(path + "PDF/" + nombre + "/" + asignatura + "/temas")
                os.makedirs(path + "PDF/" + nombre + "/" + asignatura + "/notas")

            except FileExistsError:
                pass
            
            path_temas = path + "PDF/" + nombre + "/" + asignatura + "/temas"
            if any(os.scandir(path_temas)):
                list = os.listdir(path_temas)

                print(list)

                for dir in list:
                    try:
                        os.makedirs(path_temas + "/" + str(dir) + "/videos")
                        os.makedirs(path_temas + "/" + str(dir) + "/apuntes")
                        os.makedirs(path_temas + "/" + str(dir) + "/notas")
                    except FileExistsError:
                        pass