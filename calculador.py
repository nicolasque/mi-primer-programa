
operacion_elegila = input("elege eperacion (suma/resta/multiplicacion/division/potencia/raiz):").upper()
primer_numero = int(input("elege el primer numero:"))
segundo_numero = int(input("elige el segundo numero:"))

if operacion_elegila == "SUMA":
    resulatado = primer_numero + segundo_numero

elif operacion_elegila == "RESTA":
    resulatado = primer_numero - segundo_numero

elif operacion_elegila == "MULTIPLICACION":
    resulatado = primer_numero * segundo_numero

elif operacion_elegila == "DIVISION":
    resulatado = primer_numero / segundo_numero

elif operacion_elegila == "POTENCIA":
    resulatado = primer_numero ** segundo_numero

elif operacion_elegila == "RAIZ":
    import math
    resulatado = math.sqrt(primer_numero)

print("el resultado de la {} es: {}".format(operacion_elegila,resulatado))