# # 1.Use an if...else condition to decide the grade based on the average score.
# # (A:70-100),B:(60-69),C(50-59),D(40-49),E(0-39)
# # 2.A shop will give discount of 10% if the cost of quantity purchased quantity is more than 1000.
# # Task: Ask user for quantity
# # Suppose one unit will cost 100.Judge and print the total cost for the user.

# # this is just a guideline for the score range
# # A: 70-100
# # B: 60-69
# # C: 50-59
# # D: 40-49
# # E: 0-39

score= int(input("Avarage score::"))

# # implimenting use of if...else


if score == 0 or score <=39:
    print("Grade E")
elif score == 40 or score <= 49:
    print("Grade D")
elif score == 50 or score <=59:
    print("Grade C")
elif score == 60 or score <= 69:
    print("Grade B")
elif score == 70 or score <= 100:
    print("Grade A")
else:
    print("out of range!")
# # 2.A shop will give discount of 10% if the cost of quantity purchased quantity is more than 1000.

# # Task: Ask user for quantity

purchsed_quantity = int(input("enter quantity::"))
discount = 0.1 * purchsed_quantity
print(f"your discount is {discount}")



