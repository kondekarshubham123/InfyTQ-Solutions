#DSA-Assgn-1

def merge_list(list1, list2):
    merged_data=""
    cre=list(zip(list1,list2[::-1]))
    for i in cre:
        if None in i:
            merged_data+=''.join([x for x in i if x is not None])
            merged_data+=' '
        else:
            merged_data+=''.join(i)
            merged_data+=' '
    return merged_data[:-1]

#Provide different values for the variables and test your program
list1=['A', 'app','a', 'd', 'ke', 'th', 'doc', 'awa']
list2=['y','tor','e','eps','ay',None,'le','n']
merged_data=merge_list(list1,list2)
print(merged_data)