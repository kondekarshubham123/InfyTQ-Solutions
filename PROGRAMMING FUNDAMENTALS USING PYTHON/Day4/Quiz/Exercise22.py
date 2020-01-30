#PF-Exer-22
#Something went we=rong

def generate_ticket(airline,source,destination,no_of_passengers):
    ticket_number_list=[]
    #Write your logic here
    for i in range(1,no_of_passengers+1):
        ticket_number_list.append(airline+':'+source[:3]+':'+destination[:3]+':'+str((100+i)))
        

    #Use the below return statement wherever applicable
    return ticket_number_list[-5:]

#Provide different values for airline,source,destination,no_of_passengers and test your program
print(generate_ticket("AI","Bangalore","London",7))
