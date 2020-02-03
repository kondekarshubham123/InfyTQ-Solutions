#OOPR-Exer-7
#Start writing your code here
class Ticket:
    counter=0
    def __init__(self,passenger_name,source,destination):
        self.__passenger_name=passenger_name
        self.__ticket_id=None
        self.__source=source
        self.__destination=destination
        
    def validate_source_destination(self):
        return (self.__source).lower()=='delhi' and (self.__destination).lower() in ['mumbai', 'chennai', 'pune','kolkata']

    def generate_ticket(self):
        if self.validate_source_destination():
            Ticket.counter+=1
            if len('D'+(self.__destination[0]).upper()+str(Ticket.counter))==3:
                self.__ticket_id='D'+(self.__destination[0]).upper()+'0'+str(Ticket.counter)
            else:
                self.__ticket_id='D'+(self.__destination[0]).upper()+str(Ticket.counter)
    
    def get_ticket_id(self):
        return self.__ticket_id
    
    def get_passenger_name(self):
        return self.__passenger_name
        
    def get_source(self):
        return self.__source
        
    def get_destination(self):
        return self.__destination