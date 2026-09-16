# Este proyecto llamado 1002 estara solo para estudiantes del grado...
# Empezaremos aprendiendo python, primero miraremos que son las variables y que tipo de datos hay:

nombre = input("¿Cuál es tu nombre? ")
edad = int(input("¿Cuál es tu edad? "))
peso = float(input("¿Cuál es tu peso? "))

# En este caso las variables son "nombre"," "edad" y "peso", porque su respuesta puede variar segun el resultado de el "input"
# El comando "input" significa entrada, osea que sera una entrada de información según el texto puesto por nosotros
# En mi caso fueron preguntadas relacionadas con el nombre de la variable
# Despues de colocar "input" se coloca "()" y dentro de los "()" se coloca ""
# Dentro de los "" Se coloca solo texto
# Despues del "=" se coloca que tipo de datos quiere recibir, en este caso hay 3:
# "int" para solo numeros naturales, osea nada de decimales
# "float" para numeros con decimales
# Y no se coloca nada antes del input si solo se quiere texto

# Ahora para mostrar algo en la terminal se utiliza el comando "print":

print("Hola mundo")

# Aqui despues del "print" se pone "()", y dentro el texto. Así que muestra solo la frase "Hola mundo" en la terminal
# Ahora al "print" le colocaremos variables y hay dos formas de hacerlo:

print("Hola", nombre, "tu tienes", str(edad), "años", "y pesas", str(peso))
print(f"Hola {nombre}, tu tienes {edad} años, y pesas {peso}")

# En el primero las variables estan afuera de las "" pero dentro de los "()", y a las variables de numero tienen "str"
# Despues de poner unas "" o una variable y vas a seguir poniendo mas cosas tenes que poner ","
# En el segundo se puso la "f" antes de las comillas y se utilizo "{}" para poner las variables dentro de las ""
# Para poder mirar los ejemplos darle click derecho y seleccionar "Run Python" y despues "Run Python File In Terminal"
# Así lo miran en la terminal, como primer ejercicio tendran que crear una encuesta donde se pregunte: nombre, edad, peso, y genero
# Para al final mostrar en la terminal los datos obtenidos asi como yo lo hice en el ejemplo
# La entrega de la tarea porfavor hacerla en el repositorio tarea 1, ponen el nombre y que tarea es, en este caso se llamaría tarea inicio
