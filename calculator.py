# -------------------------------------------------------------
# SIMPLE CALCULATOR PROGRAM WITH HISTORY FEATURE
# Description: A CLI-based calculator using functions, loops, and conditionals.
# -------------------------------------------------------------

# --- Functions for each arithmetic operation ---
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    # Prevent division by zero
    if b == 0:
        return "Error: Division by zero!"
    return a / b


# --- Function to display the calculator menu ---
def show_menu():
    print("\n" + "-" * 40)
    print("          SIMPLE CALCULATOR          ")
    print("-" * 40)
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")
    print("6. View Calculation History")
    print("-" * 40)


# ------------------ MAIN PROGRAM -----------------------------

history = []  # Store past calculations

while True:
    show_menu()
    choice = input("Enter your choice (1-6): ").strip()

    # Validate menu input before continuing
    if choice not in ('1', '2', '3', '4', '5', '6'):
        print(" Invalid choice! Please select a number between 1 and 6.")
        continue

    # Exit the program
    if choice == '5':
        print("Exiting the calculator... Goodbye!")
        break

    # View history
    if choice == '6':
        print("\n--- Calculation History ---")
        if not history:
            print("No calculation history yet.")
        else:
            for record in history:
                print(record)
        continue

    # Perform arithmetic operation
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input! Please enter valid numbers only.")
        continue

    # Choose operation
    if choice == '1':
        result = add(num1, num2)
        symbol = '+'
    elif choice == '2':
        result = sub(num1, num2)
        symbol = '-'
    elif choice == '3':
        result = mul(num1, num2)
        symbol = '*'
    elif choice == '4':
        result = div(num1, num2)
        symbol = '/'

    # Display and save result
    output = f"{num1} {symbol} {num2} = {result}"
    print(f"\n Result: {output}")
    history.append(output)