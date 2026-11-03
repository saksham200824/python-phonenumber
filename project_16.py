 #advance form of project 16

balance = 100000000000
pin = 2032
n = int(input("ENTER NUMBER OF EXPANCE CATEOGRY"))
expence_number =0
total_expance = 0

user_pin = int(input("ENTER YOUR PIN"))

if user_pin == pin :
    while expence_number < n:
        print("WELCOME TO YOUR EXPENCE WORLD")

        
        category = input("ENTER THE NAME OF EXPENCE :")
        category_expance =  int((input("enter total expance :")))
        date =  (input("enter date in dd/mm/yyyy formate :")
)
        expence_number += 1

        total_expance += category_expance

        balance -= category_expance
        print(f"total expance amount is : {total_expance}")
        print(f"total final balance is : {balance}")

else:
    print("INVALID PIN")


    

        