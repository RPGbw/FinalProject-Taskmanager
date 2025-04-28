'''
Author:Brennan Whiting
date:04/27/2025
Program: To Do list manager
'''

from breezypythongui import EasyFrame
import tkinter as tk

class TodoApp(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="To-Do List")
        
        # Add components
        self.addLabel("Enter Task:", row=0, column=0)
        self.taskField = self.addTextField(text="", row=0, column=1)
        self.add_button = self.addButton("Add", row=0, column=2, command=self.add_task)
        self.taskList = self.addListbox(row=1, column=0, columnspan=3)
        self.clear_button = self.addButton("Clear All", row=2, column=0, columnspan=3, command=self.clear_tasks)
        
        # Bind click event
        self.taskList.bind("<Button-1>", self.toggle_task)
    
    def add_task(self):
        task = self.taskField.getText()
        if task:
            self.taskList.insert(tk.END, task)
            self.taskField.setText("")
        else:
            self.messageBox("Warning", "Please enter a task.")
    
    def toggle_task(self, event):
        index = self.taskList.curselection()
        if index:
            index = index[0]
            current_fg = self.taskList.itemcget(index, "fg")
            if current_fg == "black":
                self.taskList.itemconfig(index, fg="gray", overstrike=1)
            else:
                self.taskList.itemconfig(index, fg="black", overstrike=0)
    
    def clear_tasks(self):
        if self.taskField("Confirm", "Clear all tasks?"):
            self.taskList.delete(0, tk.END)

if __name__ == "__main__":
    TodoApp().mainloop()
