def einstein():
    # Takes in a users input
    user_input = int(input("Enter a number to be calculated: "))
    
    mass = user_input
    c = 300000000
    energy = mass * (c ** 2)
    print(energy)
einstein()