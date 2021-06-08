#--------- Funciones básicas de strings --------------------------------------------------------------------------
#1. Vuelve los strings en mayúscula
print('Hello World'.upper())
#2. Vuelve los strings en minúscula
print('Hello World'.lower())
#3. Vuelve los strings en capital
print('Hello World'.title())
#4. Remplaza las letras del string, contiene 3 posiciones en el cual
  #4.1 La letra que se quiere cambiar
  #4.2 La letra por la que se quiere cambiar
  #4.1 La posicion donde se encuentra el string
print('Hello Horld'.replace('H', 'j', 1))
#5. Encuentra la posición de un caractér o palabra en específico
print('smooth'.find('t'))

#--------- División de strings --------------------------------------------------------------------------
#1. Así se hace la division de un string por espacios
print('Hello World'.split())
#2. Así se hace la división por letra o caracter
print('Hello World'.split('o'))
#3. Así se hace la división por cada nueva línea
print('''Hello World'''.split('\n'))
#4. Así se hace la división por cada nueva tabulación
print('''Hello World'''.split('\n'))

#--------- Unión de strings  ---------------------------------------------------------------------------
hello = ['Hello', 'word']
hello_2 = ['Hola!','Mi nombre es manuela', 'Tengo 19 años' ]
#1. Así se hace para unir 2 strings con espacios y de una variable
print(' '.join(hello))
#2. Así se hace para unir 2 strings definiendolo en la funcion
print(' '.join('Hello','world'))
#3. Así se hace para unir 2 strings por tabulacion y que quede en ese formato
print('\n'.join(hello_2))

#--------- Eliminar partes del string  ------------------------------------------------------------------
hello_3 = "   !!!Hola Manuela!!!     "
#1. Así se hace para eliminar el espacio al principio y al final del string
print(hello_3.strip())
#. Así se hace para eliminar un caractér del string
print(hello_3.strip('!'))

#--------- Usar partes de una cadena para poner un string ------------------------------------------------
#¿Por qué es mejor este método? La respuesta es legibilidad y reutilización. 
#Es mucho más fácil imaginar el resultado final .format () que imaginar el resultado final 
#de la concatenación de cadenas y la legibilidad lo es todo. También puede reutilizar la misma 
#cadena base con diferentes variables, lo que le permite reducir el código innecesario 
#y difícil de interpretar.
nombre = 'Manuela '
apellido = 'Moreno '
Saludo =  'Hola!, mi nombre es {} y mi apellido {}'.format(nombre, apellido)

#Esta es otra forma de realizar esta misma función
