
numero_tabla = int(input("de que numero quieres la tabla de multiplicar?:"))

numero_por_el_que_multiplicar =[10,9,8,7,6,5,4,3,2,1]

for multiplo in numero_por_el_que_multiplicar:
    print("{}x{} = {}".format(numero_tabla , multiplo, numero_tabla * multiplo))