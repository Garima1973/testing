def calculator():
    print("Simple Calculator: Addition and Subtraction")
    print("Enter '+' for addition or '-' for subtraction")
    operation = input("Choose operation (+ or -): ")

    if operation not in ['+', '-']:
        print("Invalid operation. Please try again.")
        return

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2

        print(f"The result is: {result}")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    calculator()