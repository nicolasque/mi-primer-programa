pokemon_elegido = input("contra que pokemon quieres combatir? (Squirtle / Charmander / Bulbasur):").upper()

vida_pikachu = 100
vida_enemigo = 0

if pokemon_elegido == "SQIRTLE":
    vida_enemigo = 90
    nombre_pokemon = "Squirtle"
    ataque_pokemon = 8

elif pokemon_elegido == "CHARMANDER":
    vida_enemigo = 80
    nombre_pokemon = "Charmander"
    ataque_pokemon = 7

elif pokemon_elegido == "BULBASUR":
    vida_enemigo = 100
    nombre_pokemon = "Bulbasur"
    ataque_pokemon = 10

while vida_pikachu > 0 and vida_enemigo >0:

    ataque_elegido = input("¿Que ataque vamos a usar ?(Chispazo/Bola voltio):").upper()
    if ataque_elegido == "CHISPAZO":
        vida_enemigo -= 10

    if ataque_elegido == "BOLA VOLTIO":
        vida_enemigo -= 12

    print("la vida del {} es {}".format(nombre_pokemon , vida_enemigo))

    print("{} hace un ataque de {} de daño".format(nombre_pokemon, ataque_pokemon))
    vida_pikachu -= ataque_pokemon

    print("la vida de tu pikachu es {}".format(vida_pikachu))

if vida_enemigo <= 0:
    print("Has ganado")
if vida_pikachu <= 0:
    print("has perdido")