a=10
if(a>15):
    print("10 is greater than 15")
else:
    print("10 is less than 15")

# Exmaple 2
num1=200
num2=150
num3=300

if(num1>num2) and (num1>num3):
    print("num1 is big")
if(num2>num1) and (num2>num3):
    print("num2 is big")
if(num3>num1) and (num3>num2):
    print("num3 is big")
else:
    print("default")

# Exmaple 3 //input function always take string value to convert this into int us typecasting
user_name=input("Enter User Name: ")
user_pass=int(input("Enter Password: "))
if(user_name=="admin" and user_pass==1234):
    print("successfully")
else:
    print("invalid")