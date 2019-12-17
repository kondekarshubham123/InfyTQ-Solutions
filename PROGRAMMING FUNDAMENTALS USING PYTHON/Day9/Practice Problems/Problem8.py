#PF-Prac-8
'''
import re
def calculate_net_amount(trans_list):
    W,D=[],[]
    for i,s in enumerate(trans_list):
        if re.search('^D',s) != None:D.append(trans_list[i][2:])
        else:W.append(trans_list[i][2:])
    return sum(map(int,D))-sum(map(int,W))

trans_list=["D:300","D:200","W:200","D:100"]
print(calculate_net_amount(trans_list))
'''
def calculate_net_amount(trans_list):
    W,D=0,0
    for i in trans_list:
        temp = i.split(":")
        if temp[0]=="D":
            D+=int(temp[1])
        else:
            W+=int(temp[1])
    return D-W

trans_list=["D:300","D:200","W:200","D:100"]
print(calculate_net_amount(trans_list))