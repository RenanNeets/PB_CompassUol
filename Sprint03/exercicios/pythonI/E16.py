def soma(string):
    numeros = map(int, string.split(','))
    return sum(numeros)
string = "1,3,4,6,10,76"
print(soma(string))