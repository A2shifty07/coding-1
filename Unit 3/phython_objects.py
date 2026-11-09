# Phython objects are digital representations of real-world entities. They are used to model and manipulate data in a structured way. In Python, objects are instances of classes, which define the properties and behaviors of the objects. 

# objects are cpllections of data that we use to 
# charcterize things  

# example - a car is a "thing" 
# charcteristics of a car - engine,tires,battery,seating,color, make, model, year, mileage, etc. 


# WE ALWAYS STAT WITH A CODE BELOW 
# THIS FUNCTION IS USED TO DESCRIBE THE CHARCTERISTICS OF 
# OBJECTS EX . SELF 
class Car:
    def __init__(self, make, model, year, color, pushtostart, engine):
        self.pushtostart = True
        self.make = "ferrari"
        self.model = "enzo"
        self.year = 2027
        self.color = "red" 
        self.engine = "v12" 

        # methods - are functions("that exist inside of an object") 

        # theseare functions exclusively work within the object 
        # things the car actually does - drive, start, stop, accelerate, brake, honk, etc. 

        def start(): 
            # if the key is present when push to start is clicked/pressed, 
            # start the engine and vechile is ready to drive.
            if self.pushtostart == True: 
                # start the engine
                print("Engine started, ready to drive!")

                
        def accelerate(): 
            # if the engine is running, increase the speed of the vechile. 
            if self.engine == "running": 
                print("Accelerating...") 


        def brake(): 
            # if the vechile is moving, decrease the speed of the vechile. 
            if self.engine == "running": 
                print("Braking...")