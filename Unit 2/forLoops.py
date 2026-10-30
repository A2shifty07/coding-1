# a loop is a code that repeats 

# while loops is a block of code that repeats itself until the triggering 
# condition is no longer TRUE. CAN BE INFINITE.


# For loops = a type of loop( code block that repeats itself) but it only repeats itself 
# up to a certain amount of times IT IS FINITE 

# FOR LOOP SYNTAX 
# I stand for literator programmers decied make this the universal 
# symbol for a placeholder for counting.
for number in range(1,500): 
    print(number / 2) 

# list a data colllection type that acts as a container for multiple data types a way to 
# list multiple pieces of data in 1 place.

grocerylist = ["apples", "oranges", "water", "chips"] 

fooditem_1 = "apple"

print(grocerylist) 

for i in grocerylist: 
    print(" I need to buy" + i) 

grades = [100,98,75,77,89,80] 

for grade in grades: 
    # show me the grades lower than 85 
    if grade < 85: 
        print(grade) 


book_1 = "math" 

book_2 = "science" 

book_for_school = book_2, book_1 

# list are collection types for us to store multiple pieces of data in a collection

# one benefit of using lists is that they can be manipulated. 
# (change/mutable) 

# we use lisyt methods to modify 

inventory = ["weapons", "healing potion", "shield", "armor"] 

# when we want to add a something to the end of list append() method 
inventory.append("spell book") 
print(inventory)  

# ex: sandwiches = ["turkey", "ham", "italian"] 

#  list are index based - we can search and find values in a list 
# because its structured 

# to pull as specfic value from a list, use a list index position 
# list always start from 0. 
print(inventory[0]) 

inventory.remove("healing potion")
inventory.pop(1) 
print(inventory)  

# how do we add the healing potion back to our inventory 
# list- specfically t index 3
inventory.insert(3,"healing potion")

