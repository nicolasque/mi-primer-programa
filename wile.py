numero_inicia = 200
while numero_inicia > 0:
    numero_inicia -=1
    print(numero_inicia)
    if numero_inicia % 2 == 0:
        print("este numero es par")
    else:
        print("este numero es inpar")
print("he terminado")