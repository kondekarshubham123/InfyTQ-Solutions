#PF-Prac-39
def max_populated_state(cities_dict,state):
    #start writing your code here
    l,l1=[],[]
    for i in cities_dict:
        if i['State']== state:
            l.append(i)
    for i in l:
        l1.append(i['Population'])
    m=max(l1)
    if l1.count(m)==1:
        S=l1.index(m)
        max_populated_city=l[S]['Name']
    else:
        pass
    return max_populated_city
    
cities_dict = [
 {'Name':'Vancouver','State':'WA','Population':161791},
 {'Name':'Salem','State':'OR','Population':154637},
 {'Name':'Seattle','State':'WA','Population':80885},
 {'Name':'Bellingham','State':'WA','Population':608661},
 {'Name':'Spokane','State':'WA','Population':208916},
 {'Name':'Bellevue','State':'WA','Population':608660},
 {'Name':'Portland','State':'OR','Population':583776}
 ]
state="WA"
# print("The city details are:",cities_dict)
# print("State:",state)
output=max_populated_state(cities_dict,state)
print("The highest populated city in the given state is:",output)