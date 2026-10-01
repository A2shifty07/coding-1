 # Function - simply put; a code block of 
# instrunctions for computers to follow.

# Built- in function - a code block of 
# instruction for a computer to follow 
# that was already written for us. 
# PRE-WRITTENcode instructions 

print('hello') 
year = input("what yaer is it?")
 print(year)  

# input() a built in function that allows a user to 
# type in data into the terminal. the data that is passed 
# in will always be trated as a string data type 

# print() a built in function that allows a user to 
# print data out in the terminal. 
 
name = "Good Morning" 
print(len(name)) 

# Data casting functions 
# these are built in (pre - written) functions 
# that change data types from one form into another 

year = 1906  

# str() - this datacasting function allows you to change 
# any data type into a string 

year = 1096 
print("This event took place in"+ str(year))

 # String concatenation- combining string data types 
 # with one another. We use the plus sign operator 
 # to combine strings together  

 print(3+3) # adding 2 integer  

# int() - Any data type passed into the brackets will 
# be converted into a integer(whole number)
 
price = 134.98 
print(int(price)) 

# float() - a function that will change any datatype 
# passed into it, into float/decimal number 

num2 = input("type in a number: ") 
# Input always returns a string 
print(9 + float(num2))