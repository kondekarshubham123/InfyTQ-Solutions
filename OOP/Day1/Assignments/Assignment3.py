
#OOPR-Assgn-3
class Customer:
    
    def __init__(self):
        self.customer_name="Shubham"
        self.bill_amount=0
        
    def pays_bill(self, amount):
        print(self.customer_name+" pays bill amount of Rs. "+ str(amount))
        
    def purchases(self,bill):
        self.bill_amount=bill
        pay_bill=self.bill_amount*0.95
        self.pays_bill(pay_bill)
        
    
c1 = Customer()
c1.purchases(200)