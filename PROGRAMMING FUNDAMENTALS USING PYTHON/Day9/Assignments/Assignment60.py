#PF-Assgn-60
def remove_duplicates(value):
    rmvdp = []
    list1=list(value)
    for i in list1:
        if i not in rmvdp:
            rmvdp.append(i)
    return "".join(rmvdp)
    
    #start writing your code here

print(remove_duplicates("11223445566666ababzzz@@@123#*#*"))