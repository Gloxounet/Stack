#This file contain the classes that will be used in the Stack_It app

class Stack :

    def __init__(self) :
        self.stack = []
    
    def trier_stack(self):
        self.stack.sort()

class Task :

    def __init__(self,name:str,time:int):
        self.name = name
        self.time = time
    

    #Surcharge :
    def __eq__(self,other) :
        return self.time == other.time
    
    def __lt__(self,other) :
        return self.time < other.time
    
    def __gt__(self,other) :
        return self.time > other.time
