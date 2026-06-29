trai_seat = input("choose seat type: general, sleeper, luxury: ").lower()

match trai_seat:
    case "general":
        print("You have selected a general seat.")
    case "sleeper":
        print("You have selected a sleeper seat.")
    case "luxury":
        print("You have selected a luxury seat.")
    case _:
        print("Invalid seat type.")
        