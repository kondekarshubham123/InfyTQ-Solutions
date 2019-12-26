#PF-Prac-32
import math
def check_squares(number):
    # for i in range(1,round(math.sqrt(number))):
    #     for j in range(j,round(math.sqrt(number))):
    #         if (i*i+j*j == number):
    #             return True
    # return False
    return any([i*i+j*j == number for i in range(1,round(math.sqrt(number))) for j in range(i,round(math.sqrt(number)))])
    

number=68
print(check_squares(number))