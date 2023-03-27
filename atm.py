from cardHolder import cardHolder


def print_menu():
    # Print options to the user
    print("Please choose from one of the following options...")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")


def deposit(cardHolder):
    try:
        deposit = float(input("How much money would you like to deposit: "))
        cardHolder.set_balance(cardHolder.get_balance() + deposit)
        print("Thank you. Your new balance is: ",
              str(cardHolder.get_balance()))
    except:
        print("Invalid input")


def withdraw(cardHolder):
    try:
        withdrawal = float(
            input("How much money would you like to withdraw: "))
        # Check balance
        if (cardHolder.get_balance() < withdrawal):
            print("Insufficient Funds")
        else:
            cardHolder.set_balance(cardHolder.get_balance() - withdrawal)
            print("Thank you. Your new balance is: ",
                  str(cardHolder.get_balance()))
    except:
        print("Invalid input")


def check_balance(cardHolder):
    print("Your current balance is: ", cardHolder.get_balance())


if __name__ == "__main__":
    current_user = cardHolder("", "", "", "", "")

    # Create a repository of cardholders
    list_of_cardHolders = []
    list_of_cardHolders.append(cardHolder(
        "1234567", 1234, "John", "Doe", 150.31))
    list_of_cardHolders.append(cardHolder(
        "1234568", 4321, "Barack", "Obama", 1672.03))
    list_of_cardHolders.append(cardHolder(
        "1234569", 9999, "Peter", "Griffin", 421.57))
    list_of_cardHolders.append(cardHolder(
        "1234560", 2468, "Barney", "Dinosaur", 15.99))
    list_of_cardHolders.append(cardHolder(
        "1234561", 4826, "Jesus", "Garcia", 879.64))

    # Prompt user for card number
    debitCardNum = ""
    while True:
        try:
            debitCardNum = input("please enter your debit card number: ")
            # Check against the repository
            debitMatch = [
                holder for holder in list_of_cardHolders if holder.cardNum == debitCardNum]
            if (len(debitMatch) > 0):
                current_user = debitMatch[0]
                break
            else:
                print("Card number not recognized. Please try again.")
        except:
            print("Card number not recognized. Please try again.")

    # Prompt for PIN
    while True:
        try:
            userPin = int(input("Please enter your pin: ").strip())
            if (current_user.get_pin() == userPin):
                break
            else:
                print("Invalid PIN. Please try again.")
        except:
            print("Invalid PIN. Please try again.")

    # Print options
    print("Welcome ", current_user.get_firstName())
    option = 0
    while (True):
        print_menu()
        try:
            option = int(input())
        except:
            print("Invalid input. Please try again.")

        if (option == 1):
            deposit(current_user)
        elif (option == 2):
            withdraw(current_user)
        elif (option == 3):
            check_balance(current_user)
        elif (option == 4):
            break
        else:
            option = 0

    print("Thank you. Have a nice day!")
