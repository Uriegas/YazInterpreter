from Archivos import Archivos
from Interpreter import Interpreter

class YazInterpreter:
    def __init__(self):
        self.interpreter = Interpreter()
        
    def menu(self):
        print("Welcome to the YazInterpreter!")
        print("You may interpret a YazLang program and output")
        print("the results to a .txt file or enter console YazInteractions")
        print("mode to run single commands of YazLang.")
        print()

        while(True):
          self.eleccion = input("\033[;37m" + "(C)onsole YazInteractions, (I)nterpret .yzy program, (Q)uit? ")
          if(self.eleccion == "I" or self.eleccion == "i"):
            self.archivos()
          elif(self.eleccion == 'C' or self.eleccion == 'c'):
            print("YazInteractions session. Type END to exit.")
            self.CLI()
          elif(self.eleccion == 'Q' or self.eleccion == 'q'):
            break

    def CLI(self):
        while True:
            self.string = input(">")
            self.a = self.interpreter.evaluateString(self.string)
            if(self.a == False):
                break
            print(self.a)
    def archivos(self):
      archivo = Archivos()
      archivo.menu()