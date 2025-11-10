# function is code reusability method

# def sum(a,b):
#     print("Sum of a & b: ",a+b)

# a=int(input("Enter Your Number: "))
# b=int(input("Enter Your Number: "))
# sum(a,b)

def sum(a,b):
    print(a+b)
def sub(a,b):
    print(a-b)
def multi(a,b):
    print(a*b)
def div(a,b):
    print(a/b)

num = int(input("Enter Your Case: "))
match num:
    case 1:
        x=int(input("Enter x: "))
        y=int(input("Enter y: "))
        sum(x,y)
    case 2:
        x=int(input("Enter x: "))
        y=int(input("Enter y: "))
        sub(x,y)
    case 3:
        x=int(input("Enter x: "))
        y=int(input("Enter y: "))
        multi(x,y)
    case 4:
        x=int(input("Enter x: "))
        y=int(input("Enter y: "))
        div(x,y)