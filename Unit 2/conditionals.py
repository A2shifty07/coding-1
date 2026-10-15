# Conditional logic - these are keywords that instruct you
# program to do specific instructions based on specific data
# or conditions

# conditional syntax (how it is written)
bill_amount = int(input("please type a bill tender (1, 5, 10, 20): "))

# if usually indicates that something is a possible option
if bill_amount == 1:
    print("here are 4 quarters")
elif bill_amount == 5:
    print("here are 20 quarters")
elif bill_amount == 10:
    print("here are 50 quarters")
elif bill_amount == 20:
    print("sorry can't accept your money, here's your money back")
else:
    print("sorry amount entered is not correct")


def college():
    grade = int(input("please type in your grade: "))
    if grade > 90:
        print("You are eligible for the program.")
    else:
        print("Please try again.")


def calculate_add():
    print("program has started: please type in 2 numbers to add")
    num1 = int(input())
    num2 = int(input())
    print(num1 + num2)
    print("program has ended.")


calculate_add()


def calculate_subtract():
    print("program has started: please type in 2 numbers to subtract")
    num1 = int(input())
    num2 = int(input())
    print(num1 - num2)
    print("program has ended.")


calculate_subtract()


def calculate_multiplication():
    print("program has started: please type in 2 numbers to multiply")
    num1 = int(input())
    num2 = int(input())
    print(num1 * num2)
    print("program has ended.")


calculate_multiplication()


def calculate_division():
    print("program has started: please type in 2 numbers to divide")
    num1 = int(input())
    num2 = int(input())
    print(num1 / num2)
    print("program has ended.")


calculate_division()


def movieTicket(age):
    if age < 7:
        print("the ticket price = 8.00.")
    elif age >= 61:
        print("Your ticket is free.")
    elif 8 <= age <= 20:
        print("Your ticket price is $12.00.")
    else:
        print("sorry there was an error in the program.")

