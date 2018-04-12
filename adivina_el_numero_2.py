numero_para_adivinar = int(input("Que numero hay que adivinar?: "))

numero_intentado = int(input("numero para adivinar:"))
while numero_para_adivinar != numero_intentado:
   numero_intentado = int(input("numero para adivinar:"))
if numero_para_adivinar ==numero_intentado:
    print("Has ganado")