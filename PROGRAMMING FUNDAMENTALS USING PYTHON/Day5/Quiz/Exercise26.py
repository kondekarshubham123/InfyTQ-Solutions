#PF-Exer-26
import math
def factorial(number):
    return math.factorial(number)

def find_strong_numbers(num_list):
    result=[]
    for num in num_list:
        i,s=num,0
        while i:
            l=i%10
            s+=factorial(l)
            i=i//10
        if s==num and num:
            result.append(num)
    return result
num_list=[145,375,0,100,2]
strong_num_list=find_strong_numbers(num_list)
print(strong_num_list)