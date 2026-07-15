# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(input())

# Iterar sobre cada caso de prueba
for _ in range(t):
    s = input()
    
    # s[::2]toma los caracteres desde el indice 0, saltando de 2 en 2 (pares: 0, 2, 4....)
    pares = s[::2]
    
    # s[1::2] toma los caracteres enpezando desde el indice 1 saltando de 2 en 2 (impares: 1, 3 ,5...)
    impares = s[1::2]
    
    # imprimir ambos resultados separados por un espacio
    print(f"{pares} {impares}")    