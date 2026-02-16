#Here we'll work on logical operators. 
# These are used to combine multiple conditions together. 
# The most common logical operators are "and", "or", and "not".

#and operator: returns True if both conditions are true
#The example problem we will solve is this imagine getting into a concert were we will have to sastify to conditions
#Condition 1: You need to be 18 or above to enter the concert
#Condition 2: You need to have a ticket to enter the concert

#setting the variables
age=18
has_ticket=True

#check the logic or the condition
if age >= 18 and has_ticket:
    print("You can enter the concert.")
else:    print("You cannot enter the concert.")

#or operator: returns True if at least one condition is true
#The example problem we will solve is this imagine getting into a concert were we will have to satisfy at least one condition
#Condition 1: You need to be 18 or above to enter the concert
#Condition 2: You need to have a ticket to enter the concert

#setting the variables
age=18
has_ticket=False

#check the logic or the condition
if age >= 18 or has_ticket:
    print("You can enter the concert.")
else:    print("You cannot enter the concert.")

#not operator: returns True if the condition is false
#The example problem we will solve is this imagine getting into a concert were we will have to satisfy the condition of not being under 18 to enter the concert
#Condition: You need to not be under 18 to enter the concert
#setting the variable

age=18

#check the logic or the condition
if not age < 18:
    print("You can enter the concert.")
else:    print("You cannot enter the concert.")

#Real world scenario with multiple logical opreators
#ATM machine example
#Condition 1: You need to have enough balance to withdraw money
#Condition 2: You need to have the correct pin to withdraw money
#Condition 3: You need to be an admin where you dont need the pin nor balance check

#setting the variables
balance = 500
withdrawal_amount = 100
pin_correct = True
is_admin = False

#check the logic or the condition
if (balance >= withdrawal_amount and pin_correct) or is_admin:
    print("You can withdraw money.")
else:    print("You cannot withdraw money.")