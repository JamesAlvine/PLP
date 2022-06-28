# 1.Write a function to accept rate, principle and time to calculate,  simple_interest
# NB://The program should accepts three arguments and returns the simple interest accordingly  


def simple_interest(p,r,t):
    print("principal",p)
    print("time",t)
    print("rate",r)
    si = (p*r*t)/100
    
    print("Simple interest is",si)
    return si
simple_interest(3, 4, 10)

# 2.Write a Python program to sum  two given integers. However, if the sum is between 15 to 20 it will return 20 else it returns the actual sum
def addition(x,y):
    addition =(x+y)
    if addition in range(15,20):
        return 20
    else:
        return addition
print(addition(10, 5))
print(addition(20, 13))

# 3.Write a function to calculate area and perimeter of a rectangle.

l= int(input("enter lenght:"))
w =int(input("enter width:"))
area = l*w
perimeter = (l+l+w+w)
print(f"area = {area}, perimeter = {perimeter}")

