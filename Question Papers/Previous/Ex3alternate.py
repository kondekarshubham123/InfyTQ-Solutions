'''
Write a python program that it should consist of special char, numbers and chars . 
if there are even numbers of special chars
Then 1) the series should start with even followed by odd
Input: t9@a42&516
Output: 492561
 
If there are odd numbers of special chars then the output will be starting with odd followed by even
Input:5u6@25g7#@
Output:56527
 
If there are any number of additional digits append them at last
'''
import re
l=[]
st='t9@a42&516'
n=list(map(int,re.findall('[0-9]',st)))
e=list(filter(lambda x: x%2==0,n))
o=list(filter(lambda x: x%2!=0,n))

if len(re.sub('[\w]','',st))%2==0:
    for i in list(zip(e,o)):
        l.extend(list(i))
else:
    for i in list(zip(o,e)):
        l.extend(list(i))
print(''.join(map(str,l)))