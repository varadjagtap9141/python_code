# Example 1: Print numbers from 0 to 99 that are divisible by 6
# for i in range(100):
#     if i%6==0:
#         print(i)

# ex 2 : print numbers divided by 10
# for i in range(1,100):
#     if i%10==0:
#         print("Number is: ",i)
#         print("Squre is: ",i**2)

#ex 3: print number with addition of 30
# for i in range(1,30):
#     print(i)
#     i+=30
#     print("After Addition: ",i)

# ex 4:get one number,traverse loop uptil that number and find divisible numbers
# num=int(input("Enter a number: "))
# for i in range(1,num):
#     if num%i==0:
#         print(i)

#ex 5:
num=int(input("Enter a number: "))
count=0
for i in range(2,num):
    if num%i==0:
        count+=i
print(count)
if count==0:
    print(num,"is prime no")
else:
    print(num,"is not prime no")
