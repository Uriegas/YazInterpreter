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
            print("Its a range")
            if(self.splited[2] == "F"):
                print( 1.8 * float(self.splited[1]) + 32 )
            elif(self.splited[2] == "C"):
                print( (float(self.splited[1]) - 32) / 1.8 )
        elif(self.splited[0] == "RANGE"):
            print("Its a convert")
        elif(self.splited[0] == "REPEAT"):
            print("Its a repeat")
        elif(self.splited[0] == "END"):
            return 0

mylexer = Lexer()
while True:
    string = input(">")
    mylexer.parse(string)
    mylexer.print()
    mylexer.evalute()