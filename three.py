print("WELCOME TO INDIAN OVERSEA BANK  ATM")
pin=3456
chances=3
balance=50000
while chances !=0:
    user_pin=int(input("please enter the four digital pin :"))
    if user_pin != pin:
        chances -= 1
        print("Wrong pin number")
        print(f"you have {chances} chances left"),
        
    else:
        user_choice =input("B:balance, D:Deposit, W:Withdraw ")
        if user_choice == "B":
            print(f"your total balance is Rs.{balance}")

        if user_choice == "D":
            deposit_user =int(input("Enter the amount of deposit : "))
            total_balance = deposit_user + balance
            print(f"You have deposited Rs.{total_balance}")
            print(f"your total balance is Rs.{total_balance}")

        if user_choice == "W":
            withdraw_user =int(input("Enter the amount of withdraw : "))
            total_balance =balance -withdraw_user
            print(f"You have withdrawn Rs.{total_balance}")
            print(f"Your total balance is Rs.{total_balance}")


        user_exit = input("Would you like to exit? Yes/No ")
        if user_exit == "Yes":
            print("Thankyou for using INDIAN OVERSEA BANK !!")
            break
        else:
            continue
                              
