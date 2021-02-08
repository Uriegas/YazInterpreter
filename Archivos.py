from Interpreter import Interpreter

class Archivos():

    def __init__(self):
        self.interpreter = Interpreter()

    def definir_archivo(self, nombre, permiso):
        archivo=open(nombre, permiso)
        return archivo

    def lectura_archivo(self, archivo):
        contenido = archivo.read()
        return contenido

    def escritura_archivo(self, archivo, cadena):
        archivo.write(cadena) 

    def menu(self):

        nameEntrada = input("Teclee el nombre del archivo que desea abrir. [No se olvide de poner la extensión.] \n >>")

        nameSalida = input("Teclee el nombre del archivo en el que desea escrribir. [No se olvide de poner la extensión.] \n >>")

        with open(nameEntrada,"r") as f:
            lines = f.readlines()

        for s in lines:
            #print(s)
            c = self.interpreter.evaluateString(s)
            archivo2 = self.definir_archivo(nombreSalida,"a")
            c= c + "\n"
            self.escritura_archivo(archivo2,c)