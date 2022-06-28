# A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years. Ask the user for their salary 
# and year of service and print the net bonus amount. Write a python code to implement this scenario.

# lets calculate bonus
bonus = (0.05)
name = input("what is your name::")
salary = int(input("your current salary::"))
years_of_service = int(input("Your year of service::"))
net_bonus = bonus * salary

print(net_bonus)


if years_of_service > 5:
    print(f"Dear {name}, your net bonus amount is {net_bonus} !!")
    
elif years_of_service <= 5:
    print(f"Dear {name}, your salary is {salary}, Earn bonus by working for 5 yrs")