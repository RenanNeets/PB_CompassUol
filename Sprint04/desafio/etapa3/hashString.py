import hashlib
while True:
    frase = input("Diga alguma coisa: (ou escreve 'exit' para parar o código:)")
    if frase.lower() == 'exit':
        print("Fim do código.")
        break
    hashSha1 = hashlib.sha1(frase.encode())
    print("O que você escreveu está agora em hash (SHA-1):", hashSha1.hexdigest())