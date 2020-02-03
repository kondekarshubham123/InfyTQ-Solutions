def fun4(l1,l2):
    for i in list(zip(l1,l2)):
        print(sum(i))
l1,l2=[1, 2, 3, 4], [4, 3, 2, 1]
print(fun4(l1,l2))