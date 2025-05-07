'''
Author: Brennan Whiting
Date: 04/28/2025
Program: To-do List manager
'''

from breezypythongui import EasyFrame
import tkinter as tk
from tkinter import messagebox

class TodoApp(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="To-Do List", width=450, height=350)

        self["background"] = "#800000" # maroon background
        
        # Labels 
        self.addLabel("To-Do List Application", row=0, column=0, columnspan=3, sticky="NSEW", font=("Arial", 14),  background="#808080", foreground="#333333")
        self.addLabel("Enter Task:", row=2, column=0)
        self.addLabel("Task Status:", row=3, column=0)
        self.status_label = self.addLabel("Ready", row=3, column=1, columnspan=2)
        
        # Input and Buttons
        self.taskField = self.addTextField(text="", row=2, column=0, columnspan=2)
        
        # Buttons
        self.add_button = self.addButton("Add Task", row=2, column=2, command=self.add_task)
        self.clear_button = self.addButton("Clear All", row=4, column=0, command=self.clear_tasks)
        self.exit_button = self.addButton("Exit", row=4, column=2, command=self.confirm_exit)
        
        # Task List 
        self.taskList = self.addListbox(row=5, column=0, columnspan=3, width=50, height=10)
        
        # Event Bindings 
        self.taskList.bind("<Double-Button-1>", self.delete_task)
        self.taskList.bind("<Button-1>", self.toggle_task)
        
        # Track completed tasks
        self.completed_tasks = set()

    # Callback Functions
    def add_task(self):
        task = self.taskField.getText().strip()
    
        # Input validation with popup errors
        if not task:
            messagebox.showerror("Input Error", "Task cannot be empty!", parent=self)
            self.status_label["text"] = "Error: Empty task"
            self.taskField.focus()
            return
        elif len(task) > 100:
            messagebox.showerror("Input Error", "Task is too long (max 100 characters)!", parent=self)
            self.status_label["text"] = "Error: Task too long"
            self.taskField.focus()
            return
        
        # If validation passes
        self.taskList.insert(tk.END, task)
        self.taskField.setText("")
        self.status_label["text"] = f"Added: {task[:20]}..." if len(task) > 20 else f"Added: {task}"
        self.taskField.focus()

    def clear_tasks(self):
        """Clear all tasks callback function"""
        if self.taskList.size() > 0:
            if messagebox.askyesno("Confirm", "Clear all tasks?"):
                self.taskList.delete(0, tk.END)
                self.completed_tasks.clear()
                self.status_label["text"] = "All tasks cleared"
        else:
            self.status_label["text"] = "No tasks to clear"

    def confirm_exit(self):
        """Exit button callback function"""
        if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
            self.status_label["text"] = "Exiting application..."
            self.after(500, self.destroy)  # Small delay for status update

    def toggle_task(self, event):
        """Toggle task completion status"""
        index = self.taskList.curselection()
        if index:
            index = index[0]
            task = self.taskList.get(index)
            if index in self.completed_tasks:
                self.taskList.itemconfig(index, fg="black")
                self.completed_tasks.remove(index)
                self.status_label["text"] = f"Marked incomplete: {task[:20]}..."
            else:
                self.taskList.itemconfig(index, fg="green")
                self.completed_tasks.add(index)
                self.status_label["text"] = f"Completed: {task[:20]}..."

    def delete_task(self, event):
        """Delete a task"""
        index = self.taskList.curselection()
        if index:
            index = index[0]
            task = self.taskList.get(index)
            if messagebox.askyesno("Confirm", f"Delete '{task}'?"):
                self.taskList.delete(index)
                if index in self.completed_tasks:
                    self.completed_tasks.remove(index)
                self.status_label["text"] = f"Deleted: {task[:20]}..."

if __name__ == "__main__":
    TodoApp().mainloop()
