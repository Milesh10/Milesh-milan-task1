while True:
    balance = 500

    print("ATM")
    print("1. Deposit\n2. Withdraw\n3. Balance\n4. Pin Setting\n5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        deposit_rs = int(input("Enter your deposit number: "))
        balance += deposit_rs
        print("Your balance now:", balance)

    elif choice == "2":
        withdraw_rs = int(input("Enter your withdraw number: "))

        if balance > withdraw_rs:
            print("You successfully withdraw")
            print("Your balance now:", balance - withdraw_rs)

        else:
            print("You failed. Actual balance is:", balance)

    elif choice == "3":
        print("Your balance now:", balance)

    elif choice == "4":
        print("Pin Setting")

    elif choice == "5":
        break

    else:
        print("Please enter valid choice")
