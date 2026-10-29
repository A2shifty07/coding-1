# PROBLEM #1 
# Create a Function that will take in 2 inputs and 
# compare them. 

# your inputs should be numbers. 

def compareNumbers():
    print("PROGRAM IS RUNNING: please type in a number")
    num1 = int(input()) 
    num2 = int(input()) 
    print(num1 < num2) 


def compareifastudenthashonorroll(): 
    print("Program is running: please typein your grade: ")
    grade = int(input("what is your grade: "))
    absences = int(input("how many days have you missed: "))
    print(" please type in absences: ")
    print(grade > 90 and absences < 5) 
compareifastudenthashonorroll()