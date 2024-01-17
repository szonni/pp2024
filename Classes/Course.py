class Course:
    def __init__(self, id, name):
        self.__name = name
        self.__id = id
    
    def get_id(self):
        return self.__id
    
    def __repr__(self):
        return f"{self.__id}, {self.__name}"
    
