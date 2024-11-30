def calculator():
    print("Welcome to the Simple Calculator!")
    print("Select an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    # Get user input for operation
    choice = input("Enter the number corresponding to your choice (1/2/3/4): ")
    
    # Validate choice
    if choice not in ['1', '2', '3', '4']:
        print("Invalid choice! Please select a valid operation.")
        return
    
    # Get user input for numbers
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return
    
    # Perform the operation
    if choice == '1':
        result = num1 + num2
        operation = '+'
    elif choice == '2':
        result = num1 - num2
        operation = '-'
    elif choice == '3':
        result = num1 * num2
        operation = '*'
    elif choice == '4':
        if num2 == 0:
            print("Division by zero is not allowed!")
            return
        result = num1 / num2
        operation = '/'
    
    # Display the result
    print(f"The result of {num1} {operation} {num2} = {result}")

# Run the calculator
if __name__ == "_main_":
    calculator()
    
