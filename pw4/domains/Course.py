class Course:
    def __init__(self, id, name):
        self.__name = name
        self.__id = id
    
    def get_id(self):
        return self.__id
    
    def __repr__(self):
        return f"Course's id: {self.__id}, course's name: {self.__name}"'\n' 
    
