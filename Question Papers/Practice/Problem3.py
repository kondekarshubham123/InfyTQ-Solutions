s="[50% Off!][Group Tours Included] 5-Day Trip to Onsen [Kyoto]"
s2='Cheese Factory Tour [Portland]'
s3='Last Day!] Beer Festival [Munich]'
#print(s.split('[')[::-1])
def fun3(s):
    for i in s.split('[')[::-1]:
        if ']'in i:
            return i[:-1]
            break
print(fun3(s3))