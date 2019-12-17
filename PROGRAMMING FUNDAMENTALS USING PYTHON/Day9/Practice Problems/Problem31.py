#PF-Prac-31
def sum_of_elements(num_list,number):
    l=[]
    for i,x in enumerate(num_list):
        if x==number:
                if i!=0:
                    l.append(num_list[i-1])
                if i!=len(num_list)-1:
                    l.append(num_list[i+1])
    print(sum(num_list))
    print(num_list.count(number))
    print(sum(l))
    result=sum(num_list) - num_list.count(number)*number - sum(l)
    if result>0:
        return result
    else:return 0
      
num_list=[1, 2, 3, 2, 4, 5, 7, 2]
number=2
print(sum_of_elements(num_list, number))