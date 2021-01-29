#Class YazInterpreter

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
#                self.result = print(num, end = " ")
#            print()
        elif(self.splited[0] == "REPEAT"):
            self.result = ''
            for rep in range(2, len(self.splited), 2):
                self.result += str(self.splited[rep - 1].replace('"', '').replace('_', ' ') * int(self.splited[rep]))
#                print(self.splited[rep - 1].replace('"', '').replace('_', ' ') * int(self.splited[rep]), end = '')
#            print()
        elif(self.splited[0] == "END"):
            self.result = False ##Aqui debe de regresar al menu
    
    ##Recibe un string y devuelve el resultado del comando (Hace las 2 funciones de arriba juntas)
    def evaluateString(self, str):
        self.getline(str)
        self.evalute()
        return self.result


class Menu:
    def __init__(self):
        self.interpreter = Interpreter()
    def menu(self):
        while(True):
            print("Este es el menu chicas")
            self.select = int(input("Elija (1)CLI, (2)TXT, 3(Salir)"))
            if(self.select == 1):
                self.CLI()
            elif(self.select == 2):
                self.TXT()
            elif(self.select == 3):
                break
    def CLI(self):
        ##Ciclo infinito para leer, esto debe de ir en la clase Menu
        
        while True:
            self.string = input(">")
            self.a = self.interpreter.evaluateString(self.string)
            if(self.a == False):
                break
            print(self.a)

    def TXT(self):
        print("Esto todavia no jala")

mymenu = Menu()
mymenu.menu()
##Funcionamiento mas detallado (se puede ocupar)
##    interpreter.getline(string)
##    interpreter.print()
##    interpreter.evalute()
    