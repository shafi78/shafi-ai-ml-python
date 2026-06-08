# match case

color = input("Enter color: ")

match color:
    case "Green":
        print("Go")
    
    case "Red":
        print("Stop")

    case _:
        print("Default one!")