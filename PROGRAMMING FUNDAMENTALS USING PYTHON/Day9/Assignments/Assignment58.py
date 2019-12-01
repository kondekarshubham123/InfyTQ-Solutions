#PF-Assgn-58
def validate_credit_card_number(card_number):
    cn = str(card_number)
    il = []
    if len(cn)==16:
        A = cn[::-1][1::2]
        for i in A:
            if 2*int(i) > 9:
                temp = str(2*int(i))
                il.append(int(str(temp[0]))+int(str(temp[1])))
            else:
                il.append(2*int(i))
        print(sum(il)+sum(map(int,list(cn[::-1][::2]))))
        if (int(sum(il)+sum(map(int,list(cn[::-1][::2]))))%10==0):
            return 1
        else:
            return 0
    else: return False
    #start writing your code here

card_number= 4539869650133101 #4539869650133101  #1456734512345698 # #5239512608615007
result=validate_credit_card_number(card_number)
if(result):
    print("credit card number is valid")
else:
    print("credit card number is invalid")