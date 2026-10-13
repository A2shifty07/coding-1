# When we are building complex programs, we ned a 
# way to pass in data that is NOT always 
# from the user. 

#  Function Parameters This is placeholder data for a 
# a function varaiables inside the curly brackets.

#  Function Arguments amd parameters are ways to 
# pass in data to a function from possibly 
# another function. 

# Memory trick- Parameter and placeholder both 
#start with the letter P
def check_Water_Depth(depth): 
    print(depth) 
    print(depth > 10) # true if depth is greater than 10 feet 
    # return depth 


#Function arguements - This is the real data that we pass into the function
# memeory trick - if you make a real world arguement with a person 
# you need to come with real facts (data) 
check_Water_Depth(3) 

# return - this keyword allows us to pass data from inside a function 
# into another function 

def username(name): 
    print("This data is coming from another function...")
    return name 

