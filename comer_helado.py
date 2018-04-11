

apetecer_helado = input("¿Te patece un helado? (si / no):").upper()
tiene_dinero = input("tines dinero para helado? (si / no):").upper()
esta_tu_tia = input("esta tu tia? (si/no:)").upper()
if apetecer_helado == "SI" and (tiene_dinero== "SI" or esta_tu_tia == "SI"):
    print("comete un helado")
else:
    print("pues nada")