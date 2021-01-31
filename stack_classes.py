# This file contain the classes that will be used in the Stack_It app

class Stack :
    

    def __init__(self) :
        self.stack = []

    def add_task(self,task) :
        self.stack.append(task)

    def find_closest_time(self,time) :
        if self.stack == [] :
            raise EOFError("Empty Stack")
        else :
            minimum = self.stack[0]
            for task in self.stack :
                minimum = min(minimum,task)
        return minimum

    def sort_stack(self):
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

def create_task(name:str,time:int):
    created_task = Task(name,time)
    return created_task



















# Module description :

if __name__ == "__main__":
    print("This is the stack_classes module that is used to build stacks")