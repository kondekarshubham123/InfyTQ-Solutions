#PF-Assgn-59
def check_perfect_number(number):
    sum=0
    for i in range(1,number):
        if number%i==0:
            sum+=i
    if sum==number and number!=0:
        return True
    else:
        return False
    
    

def check_perfectno_from_list(no_list):
    l=[]
    for i in no_list:
        check=check_perfect_number(i)
        if check:
            l.append(i)
    return l
        
    

perfectno_list=check_perfectno_from_list([18,6,4,2,1,28])
print(perfectno_list)