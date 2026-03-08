#Python Banking Program

def show_balance():
    print(f"\nYour balance is ${balance:.2f}")

def deposit():
    try:
        amount = float(input("Enter an amount to deposit: "))
        if amount <= 0:
            print("Amount must be greater than 0.")
            return 0
        return amount
    except ValueError:
        print("Invalid input. Please enter a number.")
        return 0

def withdraw():
    try:
        amount = float(input("Enter amount to withdraw: "))
        if amount <= 0:
            print("Amount must be greater than 0.")
            return 0
        elif amount > balance:
            print("Insufficient funds.")
            return 0
        return amount
    except ValueError:
        print("Invalid input. Please enter a number.")
        return 0


balance = 0
is_running = True

while is_running:
    print("\n=== Banking Program ===")
    print("1. Show Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        show_balance()
    elif choice == '2':
        balance += deposit()
    elif choice == '3':
        balance -= withdraw()
    elif choice == '4':
        is_running = False
    else:
        print("That is not a valid choice.")

print("\nThank you! Have a nice day!")