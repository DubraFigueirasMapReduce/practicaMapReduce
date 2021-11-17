from typing import List

max_usr = "None"
max_usr_count = "None"
first_usr_line = True
max_url = "None"
max_url_count = "None"
first_url_line = True
List = list()

# Se crea una lista con todas las lineas de todos los archivos part.
filenames = ['part-00000', 'part-00001']
with open('datos_combinados', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            outfile.write(infile.read())
# Una vez los resultados se halan en un fichero, se procede a crear una lista
with open("datos_combinados", "r") as file:
    with open("Resultado.txt", "w") as resultado:
        for linea in file:
            resultado.write(linea)
