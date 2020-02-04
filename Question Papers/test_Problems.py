from Practice import solutions
def test_problem1():
    assert solutions.Problem1(454)==True
    assert solutions.Problem1(9939)==False
    assert solutions.Problem1(1112111)==True

def test_problem2():
    assert solutions.Problem2("eDaBiT")==[1,3,5]
    assert solutions.Problem2("determine")==[]
    assert solutions.Problem2("STRIKE")==[0,1,2,3,4,5]

def test_problem3():
    assert solutions.Problem3("[50% Off!][Group Tours Included] 5-Day Trip to Onsen [Kyoto]")=="Kyoto"
    assert solutions.Problem3('Cheese Factory Tour [Portland]')=="Portland"
    assert solutions.Problem3('Last Day!] Beer Festival [Munich]')=='Munich'

def test_problem4():
    assert solutions.Problem4([1, 2, 3, 4], [4, 3, 2, 1] )==True
    assert solutions.Problem4([1, 2], [-1, -1])==False
    assert solutions.Problem4([9, 8, 7], [7, 8, 9, 10])==False

def test_problem5():
    assert solutions.Problem5([0, 0, 'I', 1, 1 ] )=='Right'
    assert solutions.Problem5([1,2, 5, 'I', 4, 1,0 ] )=='Left'
    assert solutions.Problem5([5, 5, 5, 0,'I', 10, 2, 2, 1 ])=='Balanced'

def test_problem6():
    assert solutions.Problem6([1, 2, 3, 4], 1)==[[1], [2], [3], [4]]
    assert solutions.Problem6([2,1, 4, 3], 2)==[[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
    assert solutions.Problem6([1, 2, 3, 4], 5)==[]
    assert solutions.Problem6([1, 2, 3, 4], 0)==[[]]

def test_problem7():
    assert solutions.Problem7({"cost_price": 32.67,  "sell_price": 45.00,  "inventory": 1200})==147968
    
def test_problem8():
    assert solutions.Problem8("abcde", "cab")==2
    assert solutions.Problem8("deafk", "kfeap")==2
    assert solutions.Problem8("acb", "ghi")==6

def test_problem9():
    assert solutions.Problem9([1, 2, 3], ["one", "two", "three"], False)=={ 1: "one", 2: "two", 3: "three" }
    assert solutions.Problem9([1, 2, 3], ["one", "two", "three"], True)=={ "one": 1, "two": 2, "three": 3 }
def test_problem10():
    assert solutions.Problem10([[8, 1, 6],[3, 5, 7],[4, 9, 2]])==True

def test_problem11():
    assert solutions.Problem11([10, 0, 0], [10, 10,10])==True
    assert solutions.Problem11([1, 0, 0], [1, 10, 10])==False


def test_problem12():
    assert solutions.Problem12(["####","#  #","#o #","####"])=="25%"
    assert solutions.Problem12([ "#######",  "#o oo #",  "#######"])=="60%"
    assert solutions.Problem12(["######","#ooo #,""#oo  #,""#    #,"  "#    #,"  "######"])=="31%"

def test_problem13():
    pass ## Try by yourself


def test_problem14():
    assert solutions.Problem14(25, 21, 125)==True
    assert solutions.Problem14(55, 226, 5190)==True
    assert solutions.Problem14(12, 215, 2142)==False

def test_problem15():
    assert solutions.Problem15(151)==[11, 22, 33, 44, 55,66, 77, 88, 99, 101, 111, 121, 131, 141, 151]
    assert solutions.Problem15(600)==[454, 464, 474, 484, 494,505, 515, 525, 535, 545,555, 565, 575, 585, 595]
    assert solutions.Problem15(999999)==[985589,  986689,  987789,  988889,  989989,990099,  991199, 992299, 993399, 994499, 995599, 996699, 997799, 998899, 999999]

def test_problem16():
    assert solutions.Problem16([3, 4, 1, 2])==3
    assert solutions.Problem16([10, 11, 12, 9, 10])==2
    assert solutions.Problem16([6, 5, 4, 3, 2, 9])==1
    assert solutions.Problem16([9,9])==0


def test_problem17():
    assert solutions.Problem17(6)==True
    assert solutions.Problem17(28)==True
    assert solutions.Problem17(24)==False

def test_problem18():
    assert solutions.Problem18(98140723568910)==True
    assert solutions.Problem18(90864523148909)==False
    assert solutions.Problem18(112233445566778899)==False

def test_problem19():
    pass
    #Test By Self

def test_problem20():
    assert solutions.Problem20([["A", "A", "A"],["A", "A", "A"],["A", "B", "A"]])==[3,2]
    assert solutions.Problem20([["c", "c", "c", "c"], ["c", "c", "c", "d"]])==[2,4]    
