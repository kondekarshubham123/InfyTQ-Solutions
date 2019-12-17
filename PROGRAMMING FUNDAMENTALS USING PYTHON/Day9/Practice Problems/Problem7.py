#PF-Prac-7
"""
import numpy
def seed_no(number,ref_no):
    return number*numpy.prod(list(map(int,list(str(number))))) == ref_no
    
number=123
ref_no=738
print(seed_no(number,ref_no))
"""
def seed_no(number,ref_no):
    m = 1
    for i in str(number):
        m*=int(i)
    return number*m == ref_no
    
number=123
ref_no=738
print(seed_no(number,ref_no))