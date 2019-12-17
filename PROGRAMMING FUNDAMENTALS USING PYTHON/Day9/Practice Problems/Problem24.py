#PF-Prac-24
def find_gcd(num1,num2):
    return max([i for i in range(1,min(num1,num2)+1) if num1%i==0 and num2%i==0])


num1=45
num2=9
print(find_gcd(num1,num2))