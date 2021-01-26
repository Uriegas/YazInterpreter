#Class YazInterpreter
#Lexer --> String 2 Tokens
#Evaluate --> Tokens 2 Resultado

class Token:
    def __init__(self, a, b):
        self.id = a
        self.value = b
    def printToken(self):
        print(self.id, self.value)

class Lexer():
    def parse(self, str):
        self.string = str
        self.splited = string.split()
    def print(self):
        print(self.string, self.splited)
    def evalute(self):
        if(self.splited[0] == "CONVERT"):
            print("Its a convert")
            if(self.splited[2] == "F"):
                print( 1.8 * float(self.splited[1]) + 32 )
            elif(self.splited[2] == "C"):
                print( (float(self.splited[1]) - 32) / 1.8 )
        elif(self.splited[0] == "RANGE"):
            for num in range(int(self.splited[1]), int(self.splited[2]), int(self.splited[3])):
                print(num, end = " ")
            print()
            print("Its a Range")
        elif(self.splited[0] == "REPEAT"):
            for rep in range(int(self.splited[2]), len(self.splited), 2):
                print(self.splited[rep - 1].replace('"', '').replace('_', ' ') * int(self.splited[rep]), end = '')
            print()
            print("Its a repeat")
        elif(self.splited[0] == "END"):
            exit(self)

mylexer = Lexer()
while True:
    string = input(">")
    mylexer.parse(string)
    mylexer.print()
    mylexer.evalute()