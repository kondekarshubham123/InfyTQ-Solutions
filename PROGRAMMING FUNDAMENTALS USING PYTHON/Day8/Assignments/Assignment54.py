#PF-Assgn-54
import re
def check_anagram(data1,data2):
    if len(data1)==data2:
        for i,s in enumerate(data1):
            if data1[i].lower()!=data2[i].lower() and (re.search(s.lower(),data2.lower())!=None) and (re.search(data2[i].lower(),data1.lower())!=None) :
                status = True
            else:
                status = False
                break
    else:
        status = False
    return 
print(check_anagram("eat","tea"))