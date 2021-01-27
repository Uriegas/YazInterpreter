#Class YazInterpreter

##Clase del Interprete: Acepta un comando 'x' con arguementos...
class Interpreter():
    ##Almacena un string en el interprete y hace una lista de esa string
    def getline(self, str):
        self.string = str
        self.splited = string.split()

    ##Para imprimir que tiene dentro la clase
    def print(self):
        print(self.string, self.splited)

    ##Da el resultado del comando utilizado
    def evalute(self):
        if(self.splited[0] == "CONVERT"):
            if(self.splited[2] == "F"):
                print( 1.8 * float(self.splited[1]) + 32 )
            elif(self.splited[2] == "C"):
                print( (float(self.splited[1]) - 32) / 1.8 )
        elif(self.splited[0] == "RANGE"):
            for num in range(int(self.splited[1]), int(self.splited[2]), int(self.splited[3])):
                print(num, end = " ")
            print()
        elif(self.splited[0] == "REPEAT"):
            for rep in range(2, len(self.splited), 2):
                print(self.splited[rep - 1].replace('"', '').replace('_', ' ') * int(self.splited[rep]), end = '')
            print()
        elif(self.splited[0] == "END"):
            exit(self) ##Aqui debe de regresar al menu
    
    ##Recibe un string y devuelve el resultado del comando (Hace las 2 funciones de arriba juntas)
    def evaluateString(self, str):
        self.getline(str)
        self.evalute()


##Este es como el main()
##Crea el interprete de la clase interprete
interpreter = Interpreter()

##Ciclo infinito para leer, esto debe de ir en la clase Menu
while True:
    string = input(">")
    interpreter.evaluateString(string)

##Funcionamiento mas detallado (se puede ocupar)
##    interpreter.getline(string)
##    interpreter.print()
##    interpreter.evalute()
    