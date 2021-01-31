import stack_classes as stck
import saving
import atexit

# Exemples :

def add_exemples(my_stack:stck.Stack) :
    task1 = stck.create_task("DM de mathématiques",60)
    task2 = stck.create_task("Réviser le français",5)
    my_stack.add_task(task1)
    my_stack.add_task(task2)

# Initialisation :

try :
    my_stack = saving.get_save()
except :
    my_stack = stck.Stack()


















# Fermeture du programme

def cleanup():
    saving.save(my_stack)

atexit.register(cleanup)