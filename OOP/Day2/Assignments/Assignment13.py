class Classroom:
    classroom_list=['G015', 'G066', 'L123', 'L135', 'L143', 'L13']
    
    @staticmethod
    def search_classroom(class_room):
        class_room=class_room.upper()
        f=0
        s="Found"
        ss=-1
        for i in Classroom.classroom_list:
            if ('L'==i[0] and class_room[0]=='L'):
                if class_room in i:
                    return s
                    f=1
                    break
        if(f==0):
            return ss
                    class Classroom:
    classroom_list=['G015', 'G066', 'L123', 'L135', 'L143', 'L13']
    
    @staticmethod
    def search_classroom(class_room):
        class_room=class_room.upper()
        f=0
        s="Found"
        ss=-1
        for i in Classroom.classroom_list:
            if ('L'==i[0] and class_room[0]=='L'):
                if class_room in i:
                    return s
                    f=1
                    break
        if(f==0):
            return ss
c=Classroom()
print(c.search_classroom('L135'))