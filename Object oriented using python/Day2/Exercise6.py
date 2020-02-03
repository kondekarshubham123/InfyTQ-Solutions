#OOPR-Exer-6
#Start writing your code here
                                                
class Vehicle():
    def __init__(self):
        self.mileage=None
        self.fuel_left=None
        
    def identify_distance_that_can_be_travelled(self):
        if self.fuel_left<=5:
            return 0
        else:    
            return (self.fuel_left-5) * self.mileage
        
    def identify_distance_travelled(self,initial_fuel):
        return self.mileage*(initial_fuel-self.fuel_left)