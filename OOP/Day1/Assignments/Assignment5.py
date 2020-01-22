class Vehicle:
    def __init__(self):
        self.__vehicle_id = None
        self.__vehicle_cost=None
        self.__vehicle_type= None
        self.__premium_amount=None
        
    def set_vehicle_id(self, vehicle_id):
            self.__vehicle_id = vehicle_id

    def get_vehicle_id(self):
        return self.__vehicle_id
        
    def set_vehicle_cost(self, vehicle_cost):
            self.__vehicle_cost = vehicle_cost

    def get_vehicle_cost(self):
        return self.__vehicle_cost
        
    def set_vehicle_type(self, vehicle_type):
            self.__vehicle_type = vehicle_type
            
    def get_premium_amount(self):
        return self.__premium_amount
            
    def set_premium_amount(self,premium_amount):
            self.__premium_amount = premium_amount

    def get_vehicle_type(self):
        return self.__vehicle_type
    
    def calculate_premium(self):
        if(self.__vehicle_type=="Two Wheeler"):
            self.__premium_amount=self.__vehicle_cost*2/100
        elif(self.__vehicle_type=="Four Wheeler"):
            self.__premium_amount=self.__vehicle_cost*6/100
            print(self.__premium_amount)
        else:
            print("vehicle type is invalid")
    
    def display_vehicle_details(self):
        print("Vehicle ID:",self.__vehicle_id)
        print("Vehicle Cost:",self.__vehicle_cost)
        print("Vehicle Type:",self.__vehicle_type)
        print("Premium Amount:",self.__premium_amount)
    

Car=Vehicle()
Car.set_vehicle_type("TwoWheeler")
Car.set_premium_amount(1000)
Car.set_vehicle_cost(100000)
Car.calculate_premium()
Car.set_vehicle_id(111)
Car.display_vehicle_details()
