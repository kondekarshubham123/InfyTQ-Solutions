def fun2(s):
    return [i for i,x in enumerate(s) if x.isupper()]
##OR##
funct2 = lambda s: [i for i,x in enumerate(s) if x.isupper()]
print(fun2('eDaBiT'))