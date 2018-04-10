number_to_guess = 2

user_number = int(input("Adivina el numero"))

if number_to_guess == user_number:
    print("Has ganado")
else:
    print("vuelve a intentar")
    number_to_guess = 2

    user_number2 = int(input("Adivina el numero"))
    if number_to_guess == user_number2:
        print("Has ganado")
    else:
        print("vuelve a intentar")
        number_to_guess = 2

        user_number3 = int(input("Adivina el numero"))
        if number_to_guess == user_number3:
            print("Has ganado")

        else:
            print("vulve a intentarlo")
            number_to_guess = 2

            user_number4 = int(input("Adivina el numero"))
            if number_to_guess == user_number4:
                print("Has ganado")
            else:
                print("vuelve a intentar")
                number_to_guess = 2

                user_number5 = int(input("Adivina el numero"))
                if number_to_guess == user_number5:
                    print("Has ganado")
                else: print("has fallado")