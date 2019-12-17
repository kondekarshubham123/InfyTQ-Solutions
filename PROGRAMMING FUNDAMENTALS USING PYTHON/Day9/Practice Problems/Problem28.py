#PF-Tryout
def sing_99_bottles():
   for i in range(99,-1,-1):
       print(str(i)+' '+'bottles of beer on the wall, '+str(i)+' bottles of beer.')
       print('Take one down, pass it around, '+str((i-1))+' bottles of beer on the wall.')
   
sing_99_bottles()