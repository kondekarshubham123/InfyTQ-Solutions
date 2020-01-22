#PF-Prac-20
def ducci_sequence(test_list,n):
    for i in range(n+1):
        test_list = [abs(test_list[1]-test_list[0]),abs(test_list[2]-test_list[1]),abs(test_list[3]-test_list[2]),abs(test_list[0]-test_list[3])]
    
    return test_list

ducci_element=ducci_sequence([0, 653, 1854, 4063] , 1)
print(ducci_element)