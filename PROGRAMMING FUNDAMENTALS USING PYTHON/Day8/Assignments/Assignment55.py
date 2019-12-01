def find_passengers_flight(airline_name="AI"):
    #This function finds and returns the number of passengers travelling in the specified airline.
    count=0
    for i in ticket_list:
        string_list=i.split(":")
        if(string_list[0].startswith(airline_name)):
            count+=1
    return count

def find_passengers_destination(destination):
    count=0
    for i in ticket_list:
        string_list=i.split(":")
        if(string_list[2].startswith(destination)):
            count+=1
    return count
    #Write the logic to find and return the number of passengers traveling to the specified destination

    #Remove pass and write your logic here
def find_passengers_per_flight():
    '''Write the logic to find and return a list having number of passengers traveling per flight based on the details in the ticket_list
    In the list, details should be provided in the format:
    [flight_no:no_of_passengers, flight_no:no_of_passengers, etc.].'''
    airline=[]
    passengers_no=[]
    l=[]
    for i in ticket_list:
        s=i[:5]
        if s not in airline:
            airline.append(s)
    for i in airline:
        passengers_no.append(find_passengers_flight(i))
    for i in range(len(airline)):
        l.append(airline[i]+':'+str(passengers_no[i]))
    return l
    #Remove pass and write your logic here

def sort_passenger_list():
    P=[]
    S = []
    R=[]
    final=[]
    l1= find_passengers_per_flight()
    for i in l1:
        P.append(i.split(':'))
    for i in range(len(P)):
        S.append(P[i][::-1])
    H = sorted(S)
    for i in range(len(H)):
        R.append(H[i][::-1])
    for i in range(len(R)):
        final.append(':'.join(R[i]))
    return final[::-1]
