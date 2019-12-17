#PF-Prac-15
def check_22(num_list):
    return '22' in ''.join(map(str,num_list))
print(check_22([3,2,5,1,2,1,2,2]))