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
    for linea in file:
        # Se comprueba si el usuario leido tiene un número de accesos mayor
        if linea[0:4] == "USR-":
            linea_spliteada = linea.split("\t")
            if first_usr_line:
                max_usr = linea_spliteada[0]
                max_usr_count = float(linea_spliteada[1])
                first_usr_line = False
            elif float(linea_spliteada[1]) > max_usr_count:
                max_usr = linea_spliteada[0]
                max_usr_count = float(linea_spliteada[1])
        # Se comprueba si la URL leida tiene un número de accesos mayor
        elif linea[0:4] == "URL-":
            linea_spliteada = linea.split("\t")
            if first_url_line:
                max_url = linea_spliteada[0]
                max_url_count = float(linea_spliteada[1])
                first_url_line = False
            elif float(linea_spliteada[1]) > max_url_count:
                max_url = linea_spliteada[0]
                max_url_count = float(linea_spliteada[1])

# Una vez los valores están calculados, se escriben en un fichero resultado
with open("Resultado.txt", "w") as resultado:
    resultado.write(max_usr[4:] + " " + str(int(max_usr_count)) + "\n")
    resultado.write(max_url[4:] + " " + str(int(max_url_count)))