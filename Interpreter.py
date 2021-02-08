class Interpreter():
    ##Almacena un string en el interprete y hace una lista de esa string
    def getline(self, str):
        self.string = str
        self.splited = self.string.split()

    ##Para imprimir que tiene dentro la clase
    def print(self):
        print(self.string, self.splited, self.result)

    ##Da el resultado del comando utilizado
    def evaluate(self):
        if(self.splited[0] == "CONVERT"):
            if(self.splited[2].upper() == "F"):
                self.result = str(1.8 * float(self.splited[1]) + 32)
            elif(self.splited[2].upper() == "C"):
                self.result = str((float(self.splited[1]) - 32) / 1.8)
        elif(self.splited[0] == "RANGE"):
            self.result = ''
            for num in range(int(self.splited[1]), int(self.splited[2]), int(self.splited[3])):
                self.result += str(num) + ' '
        elif(self.splited[0] == "REPEAT"):
            self.result = ''
            for rep in range(2, len(self.splited), 2):
                self.result += str(self.splited[rep - 1].replace('"', '').replace('_', ' ') * int(self.splited[rep]))
        elif(self.splited[0].upper() == "END"):
            self.result = False
        else:
            self.result = ''
    
    ##Recibe un string y devuelve el resultado del comando (Hace las 2 funciones de arriba juntas)
    def evaluateString(self, str):
        self.getline(str)
        self.evaluate()
        return self.result