student_name  = input("enter the name")
student_marks = int(input("enter the marks"))
if student_marks >=80:
    print("you have passed scholarship")
else:
    print("you have not eligible for scholarship")
family_income = int(input("enter your family income: "))    
if family_income <= 300000:
    print("you are passed in for full scholarship ")
elif family_income > 300000 and family_income <= 600000:
    print("you are eligible for half scholarship")
elif family_income > 600000:
    print("you are  eligible for quarter scholarship")
