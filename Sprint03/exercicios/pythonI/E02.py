numeros =[]
for i in range(3):
    numeros.append(i)
for numero in numeros:
    if numero % 2 == 0:
        print("Par:", numero)
    else:
        print("Ímpar:",numero)