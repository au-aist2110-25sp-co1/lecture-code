def get_number():
    """Gets a number from the user and returns it as an int."""
    response = input("Enter a number: ")

    try:
        num = int(response)
        return num
    except:
        return None

if __name__ == "__main__":
    # I'm running valid_num.py directly from the terminal
    num = get_number()
    if num is None:
        print("INVALID INPUT")
        exit()

    print(f"You entered {num}")
