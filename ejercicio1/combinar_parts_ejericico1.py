# Con configuración de varios parts, se abren y su resultado se escribe a un 
# fichero denominado intermedio
filenames = ['part-00000', 'part-00001']
with open('datos_combinados', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            outfile.write(infile.read())
# Una vez los resultados se halan en un fichero, se procede a ordenarlo por
# el valor de las claves, para luego quedarnos con el primer valor y el último,
# los cuales serán el valor máximo y el mínimo
with open('datos_combinados', 'r') as in_file:
  lines = sorted((l.split("\t") for l in in_file.readlines()), key=lambda l: float(l[0]))
  with open('datos_ordenados', 'w') as out_file:
    for line in lines:
       out_file.write("\t".join(line))
# Una vez los valores están ordenados, se recoje el primer y el último valor,
# los cuales serán los que nos interesan.
with open("datos_ordenados", "r") as file:
    first_line = file.readline()
    for last_line in file:
        pass
with open("Resultado.txt", "w") as resultado:
    resultado.write(first_line)
    resultado.write(last_line)