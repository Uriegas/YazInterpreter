class token:
    def __init__(self, a, b):
        self.id = a
        self.value = b
    def printToken(self):
        print(self.id, self.value)

mytoken = token(10, "RANGE")
print(token)
mytoken.printToken()