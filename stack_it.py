import pickle
import stack_classes as stck

if __name__ == "__main__":
    
    my_stack = stck.Stack()
    task1 = stck.create_task("DM de mathématiques",60)
    task2 = stck.create_task("Réviser le français",5)
    my_stack.add_task(task1)
    my_stack.add_task(task2)
    my_stack.show_stack_in_txt()