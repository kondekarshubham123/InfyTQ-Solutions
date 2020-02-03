"""
Write a python program that it should consist of special char, numbers and chars . 
if there are even numbers of special chars
Then 1) the series should start with even followed by odd
Input: t9@a42&516
Output: 492561
 
If there are odd numbers of special chars then the output will be starting with odd followed by even
Input:5u6@25g7#@
Output:56527
 
If there are any number of additional digits append them at last


import re
n = 't9@a42&516'
l=re.findall("[0-9]",n)
ln = len(re.sub("[\w]",'',n))
e = [c for c in l if int(c)%2==0]
o = [c for c in l if int(c)%2!=0]
print(e)
print(o)
if ln%2==0:
    pass
else:
    pass
24681357
"""
"""
#special chars count
s = input()
c=0
even = []
odd = []
for i in s:
	if i.isalnum():
		c+=1
	if i.isdigit():
		if int(i)%2==0:
			even.append(i)
		else:
			odd.append(i)
print(c)
print(even)
print(odd)
if c%2==0:
	if len(even) > len(odd):
		t = len(odd)
		out = even
	else:
		t=len(even)
		out=odd
	for i in range(t):
		print("{}{}".format(even[i],odd[i]),end="")
	for j in out[t:]:
		print(j,end="")
else:
	if len(even) > len(odd):
		t = len(odd)
		out = even
	else:
		t=len(even)
		out = odd
	for i in range(t):
		print("{}{}".format(odd[i],even[i]),end="")
	for j in out[t:]:
		print(j,end="")
"""
import re
n = '2468@$1357'
l=re.findall("[0-9]",n)
print(l)
sc = len(re.sub('[\w]+','',n))
p=[]
res=''
if len(l)%2==0:
    for i in range(0,len(l),2):
        p.append(l[i:i+2])
else:
    for i in range(0,len(l),2):
        p.append(l[i:i+2])


if sc%2==0:
    for i in p:
        if int(i[0]%2==0):
            res+=i[0]+i[1]
            