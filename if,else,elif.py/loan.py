salary=int(input("Enter salary:"))
age=int(input("Enter Age:"))
if(salary>=20000 and age<=50 and age>=25):
    loan=int(input("Enter your loan amount:"))
    if(loan<=50000):
        print("You are eligible for loan!")
    else:
        print("Maximum loan amount is 50000")
else:
    print("You are not eligible")
