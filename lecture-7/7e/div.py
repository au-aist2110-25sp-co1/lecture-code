from i_am_human import format_float
from valid_num import get_number

def i_am_a_cool_function():
    ...

def main():
    num1 = get_number()
    num2 = get_number()

    div = num1 / num2
    div_str = format_float(div, 2)
    print(f"{num1} / {num2} = {div_str}")

if __name__ == "__main__":
    main()
