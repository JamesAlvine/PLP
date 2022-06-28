for i in range(4):
    for j in range(4):
        print("#",end="")
    print()
    
print("***********************")   
    
for i in range(4):
    for j in range(i+1):
        print("#",end="")
    print()

print("***********************")   


for i in range(4):
    for j in range(4-i):
        print("#",end="")
    print()
    
print("***********************")    
    
# Write a Python program to construct the following pattern, using a nested for loop.
n=5
for i in range(n):
    for j in range(i):
        print ('* ', end="")
    print('')

for i in range(n,0,-1):
    for j in range(i):
        print('* ', end="")
    print('')
    