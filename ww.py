select_category = int(input("Please select a category: "))
match select_category:
    case 1:
        print("you have selected briyani")
    case 2:
        print("you have selected pizza")
    case 3:
        print("you have selected burger")
    case 4:
        print("done")
    case _:
        print("invalid")