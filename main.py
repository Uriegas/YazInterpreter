#Class YazInterpreter
#Lexer --> String 2 Tokens
#Evaluate --> Tokens 2 Resultado

class Token:
    def __init__(self, a, b):
        self.id = a
        self.value = b
    def printToken(self):
        print(self.id, self.value)

class Lexer:
    def __init__(self):
        self.string
        self.splited
    def parse(self, str):
        self.string = str
        self.splited = self.string.splited()

mylexer = Lexer()
while True:
    string = input(">")
    mylexer.parse(string)