print('Welcome to "Ye Olde York Bar & Grille"')

age = int(input("How old are you? Be honest!!: "))

if age >= 18:
    # pass
    print("Come on in and have a seat!")

    drink = input("What style iced tea would you like?")

    if drink == "sweet":
        print("enjoy your sweet tea!!")

    elif drink == "long island":
        if age >= 21:
            print('enjoy your long island iced tea')
        else:
            print("sorry, you can't drink that")
            print("have a sweet tea instead")
    #################################################
    #### SAME LOGIC AS ABOVE USING AND OPERATOR #####
    #################################################
    # elif drink == "long island" and age >= 21:
    #     print('enjoy your long island iced tea')
    # elif drink == "long island" and age < 21:
    #     print("sorry, you can't drink that")
    #     print("have a sweet tea instead")
    #################################################
    
    else:
        print("Sorry we don't serve that here")
else:
    print("You gotta go!!")



# cool strategy for dealing with nested blocks
x = 0
if x > 5:
    pass
    pass
    pass
    pass
    if x < 10:
        pass
        pass
        pass
        # if x < 10
    pass
    pass
    pass
    pass
    pass
    # end if x > 5
