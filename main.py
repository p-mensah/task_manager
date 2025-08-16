#age = input("Enter your age: \n ")
#if int(age) >= 18 and int(age) <= 45:
#    print("You can have access.")
#else:
#    print("You are not allowed here")

# ask user to input a number
# determine the modulo of the interger
#  if module is equal to 2 print even 
# else print odd

 #number = input("Enter a number: \n")
#if int(number) % 2 == 0:
 #   print("Even")
#else:
#    print("Odd")

# ask user to input a number their score as a number
# if score is btween 90 to 100 (inclusive) print "grade A"
# if score is between 80 to 89 print "Grade B"
# if score is between 70 to 79 print "grade C"
# if score is between 60 to 69 print "grade D"
# if score is between 0 to 59 print "grade E"  

# grade = input("Enter your score: \n")
# if int(grade) >= 90 and int(grade) <= 100:
#    print("Grade A")
# #   print("Grade A")
#if int(grade) >= 80 and int(grade) < 90:
#    print("Grade B") 
#if int(grade) >= 70 and int(grade) < 80:
#    print("Grade C")
#if int(grade) >= 60 and int(grade) < 70:
#    print("Grade D")    
#if int(grade) >= 0 and int(grade) < 60:
#    print("Grade F")


# ask the user to input their purchase as float
# if the purchase is GHC100 or more apply 20% discount and print amout to pay
# if the purchase is between GHC50 to GHC99 apply 10% discount and print amount to pay
# if the purchase is less than GHC50 , apply no discount and print amount to pay discount.

#purchase = input("Enter your purchase amount: \n")
#if float(purchase) >= 100:    
 #   print("Amount to pay is GHC", float(purchase) * 0.8)

#if float(purchase) >= 50 and float(purchase) < 100:
#    print("Amount to pay is GHC", float(purchase) * 0.9)

#if float(purchase) < 50:
#    print("Amount to pay is GHC", float(purchase))

#amount = float(input("Enter your purchase amount: \n"))
#discount = amount * 20/100
#total_amount = float(amount) - discount

#discount_1= amount * 10/100
#total_amount_1 = float(amount) - discount_1


#if float(amount) >= 100:    
#   print("Amount to pay is GHC", float(total_amount))
#if float(amount) >= 50 and float(amount) < 100:
#    print("Amount to pay is GHC", float(total_amount_1))
#if float(amount) < 50:
#    print("Amount to pay is GHC", float(amount))

# name = input("Enter your name: \n ")
# age = int(input("Enter your age: \n "))

# Num_1 = int(input("Enter first number: \n"))
# Num_2 = int(input("Enter second number: \n"))
# average = (Num_1 + Num_2) / 2

# if age < 18 and average  == 20:
#     print(f'{name}, you are not allowed vote.')
# if age >= 18 and average == 20:
#     print(f'{name}, you can allow to vote')

# if age >= 18 and average == 10:
#     print(f"Hello {name}, you are allowed to have vote.")

# print(f"Hello {name}, you are not allowed to vote.")
   # print(f"{name}")

    #print(f"The average of {Num_1} and {Num_2} is: {average}")


# print(f'The average of {Num_1} and {Num_2} is: {average}')


#print("the average number is : ", average)

# purchase_amount = float(input("how much did you pay: \n"))
# if purchase_amount >= 100:
#     discount =  purchase_amount * 0.2
#     amount_to_pay = purchase_amount - discount
#     print(f"Amount to pay is GHC {amount_to_pay}")

# elif purchase_amount >= 50:
#     discount = purchase_amount * 0.1
#     amount_to_pay = purchase_amount - discount
#     print(f"Amount to pay is GHC {amount_to_pay}")
    
# else:
#     print(f"Amount to pay is GHC {purchase_amount}")

# x = float(input("enter the first side  :"))
# y = float(input("enter the second side :"))
# z = float(input("enter the third side  :"))

# # if all are side equal, print equilateral
# if x == y and y == z:
#     print("The triangle is equilateral.")
# elif x == y or y == z or x == z:
#     print("The triangle is isosceles.")
# else:
#     print("The triangle is scalene.")   



# functions 

# def calculate_sum(number 1, number2):
    

# # define a registered user function

# def register_user(name, email, password):
#     # check if user does not already exist
#     # harsh your password
#     # validate input
# #     # check if user is not a robot
#     # Return response
#     return "User registered successfully"

# # call the function to register a user
# response = register_user("John Doe", "ing.mensah@gmail.com", "password123")


import add
import show
import Update   
import delete

add_task_response = add.add_task("sleep")
print(add_task_response)

show_tasks_response = show.show_tasks()
print(show_tasks_response)

update_add_task_response = Update.update_task("sleep", "wake up")
print(update_add_task_response)

delete_task_response = delete.delete_task("wake up")
print(delete_task_response) 

