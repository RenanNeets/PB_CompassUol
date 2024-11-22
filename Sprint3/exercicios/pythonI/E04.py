numerosPrimos = []
for numero in range(1, 101):
    if numero == 2:
        print(numero)
        continue
    if numero <= 1 or numero % 2 == 0:
        continue
    primo = True

    for i in range(3, int(numero)):
        if numero % i == 0:
            primo = False
            break
    if primo:
        print(numero)