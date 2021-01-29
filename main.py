#Class YazInterpreter
import os;

##Clase del Interprete: Acepta un comando 'x' con arguementos...
class Interpreter():
    ##Almacena un string en el interprete y hace una lista de esa string
    def getline(self, str):
        self.string = str
        self.splited = self.string.split()

    ##Para imprimir que tiene dentro la clase
    def print(self):
        print(self.string, self.splited, self.result)

    ##Da el resultado del comando utilizado
    def evalute(self):
        if(self.splited[0] == "CONVERT"):
            if(self.splited[2] == "F"):
                self.result = str(1.8 * float(self.splited[1]) + 32)
            elif(self.splited[2] == "C"):
                self.result = str((float(self.splited[1]) - 32) / 1.8)
        elif(self.splited[0] == "RANGE"):
            self.result = ''
            for num in range(int(self.splited[1]), int(self.splited[2]), int(self.splited[3])):
                self.result += str(num) + ' '
        elif(self.splited[0] == "REPEAT"):
            self.result = ''
            for rep in range(2, len(self.splited), 2):
                self.result += str(self.splited[rep - 1].replace('"', '').replace('_', ' ') * int(self.splited[rep]))
        elif(self.splited[0] == "END"):
            self.result = False
    
    ##Recibe un string y devuelve el resultado del comando (Hace las 2 funciones de arriba juntas)
    def evaluateString(self, str):
        self.getline(str)
        self.evalute()
        return self.result


class YazLang:
    def __init__(self):
        self.interpreter = Interpreter()
    def menu(self):
        print("Welcome to the YazInterpreter!")
        print("You may interpret a YazLang program and output")
        print("the results to a .txt file or enter console YazInteractions")
        print("mode to run single commands of YazLang.")
        print()
        while(True):
            self.select = input("(C)onsole YazInteractions, (I)nterpret .yzy program, (Q)uit? ")
            if(self.select == 'C' or self.select == 'c'):
                print("YazInteractions session. Type END to exit.")
                self.CLI()
            elif(self.select == 'I' or self.select == 'i'):
                self.fileconvertion()
            elif(self.select == 'Q' or self.select == 'q'):
                break
    def CLI(self):
        ##Ciclo infinito para leer, esto debe de ir en la clase Menu
        while True:
            self.string = input(">")
            self.a = self.interpreter.evaluateString(self.string)
            if(self.a == False):
                break
            print(self.a)

    def fileconvertion(self):
        archivo = File()
        archivo.convert()


class File(YazLang):
    def convert(self):
        self.f = input("Input file name: ")
        while not (os.path.exists(self.f)):
            self.f = input("File not found. Try again: ")
        
        self.file = open(self.f)
        self.f = input("Output file name: ")
        self.out = open(self.f, 'w')
        print("YazLang program interpreted and output to .txt file!\n")

        for command in self.file:
            self.a = self.interpreter.evaluateString(command)
            self.out.write(self.a + '\n')


mymenu = YazLang()
mymenu.menu()