# YazInterpreter
Proyecto Universidad Politécnica de Victora  
Profesor: Marco Aurelio Nuño Maganda  
Materia: Fundamentos de Programación Orientada a Objetos  
Basado en: [YazInterpreter](https://courses.cs.washington.edu/courses/cse142/20wi/homework/6/assign6.pdf)  
Reporte:
* [Ver](https://www.overleaf.com/read/ybxgbvpctzbg)   

**NOTA**: Se incluye el archivo [archivo.yzy](archivo.yzy) para realizar las pruebas de lectura de archivos.
## Funcionamiento  

### Interprete:  
Clase que recibe comandos y devuelve el resultado.

Tiene 3 atributos:
1. **string**. El comando que a evaluar en formato string (ej. CONVERT 80 F)
2. **splited**. Lista con las palabras separadas del string (ej.["CONVERT", "80", "F"])
3. **result**. Resultado despues de evaluar el comando ingresado (ej. 176)  

Tiene 4 métodos:
1. **getline**. Guarda una string y a la vez hace una lista con las palabras de esa string.
2. **print**. Imprime la string y la lista
3. **evalute**. Trabaja con la lista, tiene 5 ifs, donde evalua la primer palabra de la lista (CONVERT, RANGE REPEAT, END), en cada caso realiza las operaciones (converti temperatura, ciclo for, repetir palabras o salir del programa) y guarda el resultado de la operacion en la variable result.
4. **evaluateString**. Es solo la mezcla de getline y evaluate, literal, nada mas llama a las 2 y devuelve el valor en la variable result.  

Ejemplo:  
* Comando: `CONVERT 17 C`  
* Resultado: `-8.333`  

### Consola:  
Utiliza el interprete para recibir comandos y devolver resultados en tiempo real.  

### Interprete de archivos .yzy:  
Recibe un archivo de con extensión **".yzy"** y genera un archivo con extensión **".txt"**.  
El usuario tiene que ingresar el nombre del archivo de entrada y de salida.

### Menú:  
Clase que integra las 3 partes anteriores. Con opciones y un ciclo infinito.  
