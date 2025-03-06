name1 = input("Enter your first name: ").strip()
name2 = input("Enter your last name: ").strip()


if not name1 or not name2:
    print("Error: Please enter both first and last names.")
else:
    name1 = name1.capitalize()
    name2 = name2.capitalize()
    print(f"Hello, {name1} {name2}! Welcome to the Python program.")