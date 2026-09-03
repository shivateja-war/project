choose_option = int(input("Choose a option: "))
match choose_option:
    case 1:
        print("check balance")
    case 2:
        print("withdraw money")
    case 3:
        print("deposit money")
    case 4:
        print("exit")
    case _:
        print("invalid")