#PF-Assgn-58
def validate_credit_card_number(card_number):
    card=str(card_number)
    l=[]
    if len(card)==16:
        for i in card[-2::-2]:
            n=int(i)*2
            if n>9:
                n1=n%10+n//10
                l.append(n1)
            else:
                l.append(n)
        return (sum(l)+sum(list(map(int,card[-1::-2]))))%10==0
    else:
        return False
    

card_number= 4539869650133101 #4539869650133101  #1456734512345698 # #5239512608615007
result=validate_credit_card_number(card_number)
if(result):
    print("credit card number is valid")
else:
    print("credit card number is invalid")