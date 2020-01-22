#OOPR-Assgn-9
#Implement Student class here
class Student:
    dic={1001:25575.0,1002:15500.0}
    def __init__(self):
        self.__student_id=None
        self.__marks=None
        self.__age=None
        self.__course_id=None
        self.__fees=None
        
    def choose_course(self,course_id):
        if course_id in self.dic.keys():
            self.__course_id=course_id
            self.__fees=self.dic[course_id]
            if self.__marks>85:
                self.__fees=self.dic[course_id]-self.dic[course_id]*25/100    
            return True
        else:
            return False
        
    def set_student_id(self,student_id):
        self.__student_id=student_id    
    def set_marks(self,marks):
        self.__marks=marks
    def set_age(self,age):
        self.__age=age
    
    def get_student_id(self):
        return self.__student_id
    def get_marks(self):
        return self.__marks
    def get_age(self):
        return self.__age
    def get_course_id(self):
        return self.__course_id
    def get_fees(self):
        return self.__fees

    def validate_age(self):
        return self.__age > 20
    def validate_marks(self):
        return 0<=self.__marks<=100
    def check_qualification(self):
        return self.validate_marks() and self.validate_age() and self.__marks>=65 




maddy=Student()
maddy.set_student_id(1001)
maddy.set_age(21)
maddy.set_marks(65)
if(maddy.check_qualification()):
    print("Student has qualified")
    if(maddy.choose_course(1002)):
        print("Course allocated")
    else:
        print("Invalid course id")
else:
    print("Student has not qualified")