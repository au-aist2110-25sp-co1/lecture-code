HASHED_PWD = -912547137229350376

pwd = input("Speak Friend and Enter: ")

if hash(pwd) == HASHED_PWD:
    print("Welcome to the Mines of Moria!!")
else:
    print("You shall not pass!!!")
