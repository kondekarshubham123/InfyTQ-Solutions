#PF-Prac-11
def find_upper_and_lower(sentence):
    U,L=0,0
    for i in sentence:
        if i.isupper():
            U+=1
        elif i.islower():
            L+=1
    return [U,L]

sentence="Come Here"
print(find_upper_and_lower(sentence))