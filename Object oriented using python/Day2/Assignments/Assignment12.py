#OOPR-Assgn-12
#Start writing your code here
class Bill:
    def __init__(self,bill_id,patient_name):
        self.__patient_name=patient_name
        self.__bill_id=bill_id
        self.__bill_amount=None
        
    def get_bill_amount(self):
        return self.__bill_amount
    
    def get_patient_name(self):
        return self.__patient_name
    
    def get_bill_id(self):
        return self.__bill_id
        
    def calculate_bill_amount(self,consultation_fees, quantity_list, price_list):
        total=0
        for i,x in enumerate(quantity_list):
            total=quantity_list[i]*price_list[i]+total
            
        self.__bill_amount=consultation_fees+total

#testing
