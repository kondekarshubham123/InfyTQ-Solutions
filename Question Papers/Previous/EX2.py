'''
A string which is a mixture of letter and integer and special char from which find the largest even 
number from the available digit after removing the duplicates. 
If an even number is not formed then return -1.

Ex : infosys@337
O/p : -1
 
Hello#81@21349
O/p :983412
'''
import re
n = 'Hello#81@21349'
num = ''.join(sorted(list(set(re.findall("[0-9]",n))),reverse=True))
x=-1
for i,s in enumerate(num[::-1]):
    if int(s)%2 == 0:
        x=s
        y=i
        break
if x!=-1:
    p = list(num)
    p.remove(x)
    print(int(''.join(p)+num[::-1][y]))
else:
    print(-1)