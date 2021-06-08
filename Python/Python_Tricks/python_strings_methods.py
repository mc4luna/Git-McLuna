print('Hello World'.upper())
print('Hello World'.lower())
print('Hello World'.title())

print(' '.join(['Hello', 'World']))
print('Hello Horld'.replace('H', 'j', 1)) #Letra a remplazar, letra a cambiar, posicion del string
print('   Hello World   '.strip())

#División de strings
#1. Así se hace la division de un string por espacios
print('Hello World'.split())
#2. Así se hace la división por letra o caracter
print('Hello World'.split('o'))
#3. Así se hace la división por cada nueva línea
print('''Hello World'''.split('\n'))
#4. Así se hace la división por cada nueva tabulación
print('''Hello World'''.split('\n'))

#Unión de strings
hello = ['Hello', 'word']
hello_2 = ['Hola!','Mi nombre es manuela', 'Tengo 19 años' ]
#1. Así se hace para unir 2 strings con espacios y de una variable
print(' '.join(hello))
#2. Así se hace para unir 2 strings definiendolo en la funcion
print(' '.join('Hello','world'))
#3. Así se hace para unir 2 strings por tabulacion y que quede en ese formato
print('\n'.join(hello_2))
