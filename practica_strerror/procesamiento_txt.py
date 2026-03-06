from os import strerror

try:
    caracter_contador = line_contador = 0
    stream = open('practica_strerror/Simple_Text.txt','rt')
    my_text = stream.readline()
    while my_text != '':
        line_contador += 1
        for letter in my_text:
            print(letter, end ='')
            caracter_contador += 1
        my_text = stream.readline()
    stream.close()
    print("\n\nCaracteres en el archivo:", caracter_contador)
    print("Líneas en el archivo:     ", line_contador)
except IOError as e:
    print("Se produjo un error de E/S:", strerror(e.errno))
