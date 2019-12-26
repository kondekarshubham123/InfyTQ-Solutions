#PF-Prac-36
def find_target_positions(input_string, target_word):
    target_list=[]
    #idx = input_string.split(" ")
    idx = input_string
    for i,x in enumerate(idx):
        if x==target_word:
            target_list.append(i)
    return target_list



def find_inverted_index(input_string):
    target_dict={}
    #Start writing your code here
    tgtlst = input_string.split()
    for k in tgtlst:
        target_dict.update({k:find_target_positions(tgtlst,k)})
    return target_dict
    
    
input_string="we dont need no education we dont need no thought control no we dont"
result_dict=find_inverted_index(input_string)
print(result_dict)