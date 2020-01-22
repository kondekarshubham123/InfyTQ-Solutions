#DSA-Exer-1

def update_mark_list(mark_list, new_element, pos):
    mark_list.insert(pos,new_element)
    return mark_list

def find_mark(mark_list,pos1,pos2):
    '''Remove pass and write your logic here to return a list containing
    the marks at pos1 and pos2 respectively.'''
    return [mark_list[pos1],mark_list[pos2]]

#Provide different values for the variables and test your program
mark_list=[89,78,99,76,77,67,99,98,90]
new_element=78
pos=8
pos1=5
pos2=7
print(update_mark_list(mark_list, new_element, pos))
print(find_mark(mark_list, pos1, pos2))