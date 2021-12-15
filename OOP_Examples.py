class HumanBeing(object): # Class definition statement self refers to the current instance of the class
    def __init__(self, first_name, eye_colour): # special method called during instantiation
        self.first_name = first_name # first name attribute initialised with parameter value
        self.eye_colour = eye_colour # Eye colour attribute initialised with parameter value
        self.position = 0 # position initialised with 0
    def walk_steps(self, steps): # method definition for walking steps as parameter
        self.position += steps # Code that changes the position given the steps value

# Based on the class definition, a new Python object can be instantiated and used:

Alex = HumanBeing('Alex', 'blue') # The instantiation

print(Alex.first_name) # Accessing attribute values
print(Alex.position) # Accessing attribute values
Alex.walk_steps(10) # Calling Method
print(Alex.position) # Accessing Position value