nombre = input('¿Nombre?: ')

edad_str = input('¿Edad?: ')
edad = int(edad_str)  # Como input guarda la variable como cadena, hay que 'castearla' (convertir su tipo) a entero, con la funcion int() (int=integer=entero)
                    # ¿Que pasa si el usuario introduce una palabra en vez de un numero?

peso_str = input('PESO?: ')
peso = float(peso_str)

altura_str = input('ALTURA?: ')
altura = float(altura_str)

IMC = peso / (altura**2)

print('Hola', nombre, 'A continuacion voy a mostrarte el resultado al calculo sobre tu INDICE DE MASA CORPORAL.')
print('Un IMC normal se encuentra entre 18.5 y 24.9 kg/m^2. Un IMC menor a 18.5 kg/m^2 se considera bajo peso, mientras que un IMC mayor a 25 kg/m^2 se considera sobrepeso. Un IMC mayor a 30 kg/m^2 se considera obesidad. Sin embargo, estos valores son solo una guía y no son válidos para todas las personas, especialmente aquellas con una gran cantidad de músculo o deportistas.')
print('Para tu altura de ', altura, 'tu IMC es de ', IMC )