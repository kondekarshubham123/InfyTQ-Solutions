#PF-Assgn-57
def check_prime(number):
    factor = 2
    while factor * factor <= int(number):
        if int(number) % factor == 0:
            return False
        factor+=1
    return True
     #remove pass and write your logic here. if the number is prime return true, else return false

def rotations(num):
    answer = []
    final=[]
    rotation = str(num)
    while not rotation in answer:
        answer.append(rotation)
        rotation = rotation[1:] + rotation[0]
    for i in answer:
        final.append(int(i))
    return final

    #remove pass and write your logic here. It should return the list of different combinations of digits of the given number.
	#Rotation should be done in clockwise direction. For example, if the given number is 197, the list returned should be [197, 971, 719]

def get_circular_prime_count(limit):
    all_circulations = [2]
    ret = []
    for num in range(3, limit, 2):
        if check_prime(num):
            check = 0
            if rotations(num):
                circulations = rotations(num)
                for circulation in circulations:
                    if not check_prime(circulation):
                        check += 1
                if not check:
                    all_circulations.extend(circulations)
    final = sorted(list(set(all_circulations))) 
    for i in final:
        if i<=limit:
            ret.append(i)
    return len(ret)
    
    
    #remove pass and write your logic here.It should return the count of circular prime numbers below the given limit.

#Provide different values for limit and test your program
print(get_circular_prime_count(20))