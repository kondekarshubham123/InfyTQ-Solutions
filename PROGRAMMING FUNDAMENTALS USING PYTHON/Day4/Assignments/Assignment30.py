#PF-Assgn-30

def encode(message):
    encode = message+"0"
    l=[]
    count = 1
    for index, value in enumerate(encode): 
        if value != "0":
            if value == encode[index+1]:
                count = count+1
            else:
                l.append(str(count))
                l.append(value)
                count=1    
    return "".join(l)
    
encoded_message=encode("ABBBBCCCCCCCCAB")
print(encoded_message)

'''
#PF-Assgn-30
from itertools import groupby
def encode(message):
    s=''
    for i,c in groupby(message):
        s+=str(len(list(c)))+i
    #Remove pass and write your logic here
    return s

#Provide different values for message and test your program
encoded_message=encode("ABBBBCCCCCCCCAB")
print(encoded_message)
'''