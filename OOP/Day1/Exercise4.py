class Athlete:
    def __init__(self,name,gender):
        self.__name=name
        self.__gender=gender
    
    def set_name(self,name):
        self.__name=name
    
    def get_name(self):
        return self.__name
        
    def set_gender(self,gender):
        self.__gender=gender
    
    def get_gender(self):
        return self.__gender
        
    def running(self):
        if(self.__gender=="girl"):
            print("150mtr running")
        else:
            print("200mtr running")
player=Athlete("Maria","girl")
player.set_gender("girl")
player.set_name("Maria")
player.running()