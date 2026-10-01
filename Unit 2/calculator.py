# step 1: create a function that will add 
# 2 numbers together 

# Step 2: the numbers should be typed in by a user 

# Phase 1: function definition- actual code 
def calculate_add(): 
   print("program has started: please type 2 numbers to add: ") 
    num1 = int(input())
    num2 = int(input())
    print(num1+ num2) 
    print("program has ended")
# Phase 2: Function Call- Executing code  
calculate_add() 

# Subtraction function 
# Multiplication function 
# division function 
  
# subtraction function
def calculate_subtract(): 
   print("program has started: please type 2 numbers to subtract: ") 
    num1 = int(input())
    num2 = int(input())
    print(num1-num2) 
    print("program has ended")
    calculate_subtract() 

# Muiltiplication function

def calculate_multipy(): 
   print("program has started: please type 2 numbers to multiply") 
    num1 = int(input())
    num2 = int(input())
    print(num1 * num2) 
    print("program has ended")
    calculate_multipy() 


# Division function

def calculate_divide(): 
   print("program has started: please type 2 numbers to divide: ") 
    num1 = int(input())
    num2 = int(input())
    print(num1 / num2) 
    print("program has ended")
    calculate_divide() 