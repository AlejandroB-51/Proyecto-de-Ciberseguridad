#numeros = [10, 20, 30, 40, 50]
#print(numeros[4])

numeros = [3, 8, 15, 22, 7, 14, 9, 6]
for numeros_operacion in numeros:
   resultado = numeros_operacion % 2
   if resultado == 0:
        print(numeros_operacion)
   else: print("")
