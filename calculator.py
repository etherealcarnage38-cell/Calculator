def calculator():
    print("====================================")
    print("    Command Line Calculator Tool    ")
    print("====================================")
    
    while True:
        choice = input("\nSelect operation (+, -, *, /): ").strip()

        if choice not in ['+', '-', '*', '/']:
            print("Error: Invalid operation selected. Please choose from +, -, *, or /.")
            continue

        try:
            n1 = float(input("Enter first number: "))
            n2 = float(input("Enter second number: "))
        except ValueError:
            print("Error: Invalid input. Please enter valid numeric values.")
            continue

        if choice == "+":
            print(f"Result: {n1} + {n2} = {n1 + n2}")
        elif choice == "-":
            print(f"Result: {n1} - {n2} = {n1 - n2}")
        elif choice == "*":
            print(f"Result: {n1} * {n2} = {n1 * n2}")
        elif choice == "/":
            if n2 == 0:
                print("Error: Division by zero is not allowed.")
            else:
                print(f"Result: {n1} / {n2} = {n1 / n2}")

        ch = input("\nDo you want to perform another calculation? (y/n): ").strip().lower()
        if ch != 'y':
            print("\nThank you for using the calculator!")
            break

if __name__ == "__main__":
    calculator()
