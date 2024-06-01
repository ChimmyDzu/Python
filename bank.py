GREEN = "\033[32m"
RESET = "\033[0m"

name = input(f"{GREEN}Please write your name: {RESET}")
print(f"{GREEN}Hello there {name}, welcome to the Python bank!{RESET}")

def bank_account():
    balance = 0
    
    while True:
        print("\nCurrent balance:", balance)
        user_input = input("What would you like to do? 1. Deposit money 2. Withdraw money 3. Check balance 4. Exit: ")
        
        if user_input == '4':
            print("Exiting the program. Final balance:", balance)
            break
        elif user_input == '1':
            try:
                money = input("How much would you like to deposit? ")
                deposit = int(money)
                if deposit > 0:
                    balance += deposit
                    print("Deposited:", deposit)
                else:
                    print("Please enter a positive amount.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif user_input == '2':
            try:
                amount = input("How much money would you like to withdraw? ")
                withdrawal = int(amount)
                if withdrawal > 0:
                    if withdrawal <= balance:
                        balance -= withdrawal
                        print("Withdrew:", withdrawal)
                    else:
                        print("Insufficient funds.")
                else:
                    print("Please enter a positive amount.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif user_input == '3':
            print("Checking balance. Your balance is:", balance)
        else:
            print("Invalid option. Please choose 1, 2, 3, or 4.")

# Run the bank account program
bank_account()
