#PF-Exer-18
def get_count(num_list):
    count=0
    for i in range(len(num_list)-1):
        count+=int(num_list[i]==num_list[i+1])
    # Write your logic here

    return count

#provide different values in list and test your program
num_list=[1,1,5,100,-20,-20,6,0,0]
print(get_count(num_list))