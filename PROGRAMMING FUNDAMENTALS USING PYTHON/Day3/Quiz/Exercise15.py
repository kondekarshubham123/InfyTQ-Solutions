#PF-Exer-15
def find_sum_of_digits(number):
    sum_of_digits=0
    h=list(map(int,list(str(number))))
    for i in h:
        sum_of_digits+=i
    #Write your logic here
    return sum_of_digits

#Provide different values for number and test your program
sum_of_digits=find_sum_of_digits(123)
print("Sum of digits:",sum_of_digits)
                                          
                                          
'''
@Shiva Adsule
#PF-Exer-15
def find_sum_of_digits(number):
    sum_of_digits=0
    while number:sum_of_digits,number=sum_of_digits+number%10,number//10
    return sum_of_digits

#Provide different values for number and test your program
sum_of_digits=find_sum_of_digits(123)
print("Sum of digits:",sum_of_digits)
                                          
'''