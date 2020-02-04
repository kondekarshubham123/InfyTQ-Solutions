# Problem1
Problem1 = lambda x:str(x)==str(x)[::-1]
# Problem2
Problem2 = lambda s: [i for i,x in enumerate(s) if x.isupper()]
# Problem3
def Problem3(s):
    for i in s.split('[')[::-1]:
        if ']'in i:
            return i[:-1]
            

# Problem4
def Problem4(l1,l2):
    for i in list(zip(l1,l2)):
        print(sum(i))
# Problem5
def Problem5(l1):
    pass
def Problem6(l,i):
    pass
def Problem7(d):
    pass
def Problem8(s1,s2):
    pass
def Problem9(l1,l2,c):
    pass
def Problem10(l1):
    pass
def Problem11(l1,l2):
    pass
def Problem12(l1):
    pass
def Problem13(l1):
    pass
def Problem14(x,y,z):
    pass
def Problem15(x):
    pass
def Problem16(l):
    pass
def Problem17(n):
    pass
def Problem18(n):
    pass
def Problem19(l1):
    pass
def Problem20(l):
    pass
