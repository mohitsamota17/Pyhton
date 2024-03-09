def calculator():
    history = []

    while True:
        print("\nCalculator Menu:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. View history")
        print("6. Quit")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            result = a + b
            history.append(f"{a} + {b} = {result}")
            print(f"Result: {result}")

        elif choice == 2:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            result = a - b
            history.append(f"{a} - {b} = {result}")
            print(f"Result: {result}")

        elif choice == 3:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            result = a * b
            history.append(f"{a} * {b} = {result}")
            print(f"Result: {result}")

        elif choice == 4:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            if b == 0:
                raise ValueError("Division by zero is not allowed")
            result = a / b
            history.append(f"{a} / {b} = {result}")
            print(f"Result: {result}")

        elif choice == 5:
            for i in history:
                print(i)

        elif choice == 6:
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

calculator()
