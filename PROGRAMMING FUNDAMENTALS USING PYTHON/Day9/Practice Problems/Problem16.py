#PF-Prac-16
def rotate_list(input_list,n):
    #start writing your code here
    for i in range(n):
        input_list.insert(0,input_list.pop(-1))
    return input_list

input_list= [1,2,3,4,5,6]
output_list=rotate_list(input_list,4)
print(output_list)