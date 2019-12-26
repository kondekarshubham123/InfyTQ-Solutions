#PF-Prac-13
def close_number(num1,num2,num3):
    #start writing your code here
    if abs(num1-num2)<=1 or abs(num2-num3)<=1 or abs(num1-num3)<=1:
        if abs(num2-num1)>=2 or abs(num2-num3)>=2:
            return True
        return False
    return False
    
print(close_number(5,4,2))