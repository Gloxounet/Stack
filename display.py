# display.py
import tkinter as tk
import pygubu


class StackViewApp:
    
    def __init__(self):

        #1: Create a builder
        self.builder = builder = pygubu.Builder()

        #2: Load an ui file
        builder.add_from_file('stackviewapp.ui')

        #3: Create the mainwindow
        self.mainwindow = builder.get_object('mainwindow')

        #4: Get objects
        self.entry_task_name = builder.get_object('entry_task_name')
        
    def run(self):
        self.mainwindow.mainloop()

    def test(self) :
        self.entry_task_name['text'] == "Wow"
        print("done")


if __name__ == '__main__':
    app = StackViewApp()
    app.run()