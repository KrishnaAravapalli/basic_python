try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    add = num1 + num2
    sub = num1 - num2
    mult = num1 * num2

    if num2 != 0:
        div = num1 / num2
    else:
        div = "Number cannot be divided by zero"

    def format(n):
        if isinstance(n, str):
            return n
        if n.is_integer():
            return int(n)
        return n

    print(f"\nAddition: {format(add)}")
    print(f"Subtraction: {format(sub)}") 
    print(f"Multiplication: {format(mult)}")
    print(f"Division: {format(div)}")

except ValueError:
    print("Please enter valid numbers")