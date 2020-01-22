#PF-Prac-47
import re
def list_rotate(uniquecode_list):
    rotated_list=[]
    for i in uniquecode_list:
        sp = i.split("-")
        #print(len(re.sub("[^A-Z]",'',sp[0])))
        if sum(c.isalpha() for c in sp[0]) == 1:
            rot = [sp[0][0:1],sp[1][1:4]+sp[1][0]]
        else:
            rot = [sp[0][0:2],sp[1][2:4]+sp[1][0:2]]
        #print(re.findall("[A-Z]+",sp[0]))
        rotated_list.append("".join(rot))
    return rotated_list

uniquecode_list=["AZ01-1234","R137-8714"]
rotated_list = list_rotate(uniquecode_list)
print(rotated_list)

"""
Using re
for checking lenght 
len(re.sub("[^A-Z]","",sp[0]))

for print String
re.findall("[A-Z]+",sp[0])
"""