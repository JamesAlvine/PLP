# 1.Write a python program to store three integers in x,y and z. Print their sum.
x = int (input("write any number:"))
y = int (input("enter any other value:"))
z = int (input("enter any other value:"))

sum = x + y + z
  
print(sum)

# 2.Write a python program to take two int values from the user and print the greatest among them.

a= input("enter numner:")
b = input("enter value:")

if a > b :
    print(f"{a} is greater than {b}")

elif b > a : 
    print(f"{b} is greater than {a}")