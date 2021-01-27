# YazInterpreter
Proyecto Universidad Politécnica de Victora  
Profesor: Marco Aurelio Nuño Maganda  
Materia: Fundamentos de Programación Orientada a Objetos  
Basado en: [YazInterpreter](https://courses.cs.washington.edu/courses/cse142/20wi/homework/6/assign6.pdf)  
Reporte:  
* [Ver](https://www.overleaf.com/read/ybxgbvpctzbg)  
* [Editar](https://www.overleaf.com/3137935175qcthrzcqdjsc)  

## Funcionamiento  

### Interprete:  
Clase que recibe comandos y devuelve el resultado.  
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
