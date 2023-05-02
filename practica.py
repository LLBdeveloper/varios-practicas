#SEMANA 3
    

# Ejercicio  2 

# string = input('Ingrese la palabra a traducir en Jeringoso: ')
# cadenaPa = ''
# for i in string :

#     if i == 'a' :
#         cadenaPa = cadenaPa + i + 'pa'


#     elif i == 'e' :
#         cadenaPa = cadenaPa + i + 'pe'


#     elif i == 'i' :
#         cadenaPa = cadenaPa + i + 'pi'


#     elif i == 'o' :
#         cadenaPa = cadenaPa + i + 'po'


#     elif i == 'u' :
#         cadenaPa = cadenaPa + i + 'pu'

#     else :
#         cadenaPa = cadenaPa + i 

# print(cadenaPa)


#Ejercicio 3 

# mes = int(input('Ingrese el numero de mes: '))

# if mes == 1 :
#     print('El mes tiene 31 dias.')
# elif mes == 2 :
#     print('El mes tiene 28 dias.')
# elif mes == 3 :
#     print('El mes tiene 31 dias.')
# elif mes == 4 :
#     print('El mes tiene 30 dias.')
# elif mes == 5 :
#     print('El mes tiene 31 dias.')
# elif mes == 6 :
#     print('El mes tiene 30 dias.')
# elif mes == 7 :
#     print('El mes tiene 31 dias.')
# elif mes == 8 :
#     print('El mes tiene 31 dias.')
# elif mes == 9 :
#     print('El mes tiene 30 dias.')
# elif mes == 10 :
#     print('El mes tiene 31 dias.')
# elif mes == 11 :
#     print('El mes tiene 30 dias.')
# elif mes == 12 :
#     print('El mes tiene 31 dias.')
# else :
#     print('Ingrese un numero del 1 al 12.')


#Ejercicio 4

# poblaA = 75000
# tasaA = 4

# poblaB = 230000
# tasaB = 1.2

# anos = 0

# porcentajeA = 0
# porcentajeB = 0


# while poblaA < poblaB :
#     porcentajeA = (poblaA * 4) / 100
#     poblaA = poblaA + porcentajeA
#     porcentajeB = (poblaB * 1.2) / 100
#     poblaB = poblaB + porcentajeA
#     anos = anos + 1
#     print('Al ano ', anos, ' la poblacion seria de ', poblaA )

# print ('La cantidad de anos para que el paisA supere al paisB es de: ', anos)

#ejercicio 5

# Notas. Las notas obtenidas en por el alumno A durante su cursada fueron: 8, 7, 7, 6, 9, 10, 8, 9. El alumno B obtuvo las siguientes notas: 9, 8, 8, 9, 5, 8, 9, 7. Realizar un programa que calcule la nota media y que muestre quien sacó la nota mayor y quien sacó la nota menor.
# alumnoA = [8, 7, 7, 6, 9, 10, 8, 9]
# calculoA = 0
# for i in alumnoA:
#     calculoA = calculoA + i
#     resultadoA = calculoA / len(alumnoA)
# print('El promedio de alumno A es: ', resultadoA)

# alumnoB = [9, 8, 8, 9, 5, 8, 9, 7]
# calculoB = 0
# for i in alumnoB:
#     calculoB = calculoB + i
#     resultadoB = calculoB / len(alumnoB)
# print('El promedio de alumno B es: ', resultadoB)

# if resultadoA > resultadoB:
#     print('Alumno A saco la mayor nota. Alumno B saco la menor nota.')
# else :
#     print('Alumno B saco la mayor nota. Alumno A saco la menor nota. ')



# ### Ejercicio 6

# 1.   Crea una lista con los números del 1 al 10.
# 2.   Imprime los elementos en las posiciones 3, 4 y 5 utilizando slices.
# 3.   Imprime los elementos en las posiciones 2, 4, 6 y 8 utilizando slices.
# 4.   Crea una nueva lista que contenga los elementos de la lista original en orden inverso utilizando slices.
# 5.   Reemplaza los elementos en las posiciones 2, 3 y 4 con los números 20, 30 y 40 utilizando slices.

# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(numeros[2:5])

# print(numeros[1:2])
# print(numeros[3:4])
# print(numeros[5:6])
# print(numeros[7:8])
# #mismo ej pero con el slice aca abajo
# nueva = sorted(numeros)
# nueva.sort(reverse=True)
# print(nueva[:10])


# numeros[1] = 20
# numeros[2] = 30
# numeros[3] = 40

# print(numeros)

### Ejercicio 7 - (opcional)

# Supongamos que tenemos una lista de números enteros, y queremos encontrar todas las subsecuencias de la lista que sumen un número objetivo dado. Para hacerlo, vamos a crear una función que tome como argumentos la lista de números y el número objetivo, y devuelva una lista con todas las subsecuencias que suman el número objetivo. 

# *Ayuda:* Por ejemplo, si le damos a tu programa la lista de números [1, 2, 3, 4, 5] y queremos encontrar todas las subsecuencias que suman `7` (número objetivo dado), la función debería devolver las siguientes listas [2, 5], [3, 4], [1, 2, 4].
