

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror

# root window
root = tk.Tk()
root.title('Hackathon Group Wise')
root.geometry('500x600')
root.configure(bg="white")
root.resizable(True, True)


frame = ttk.Frame(root)


options = {'padx': 15, 'pady': 5}


# A1=Label(root,font=("arial",40,"bold"),text="PLAYER",bg="orange",fg="pink")
item_label1 = ttk.Label(frame, text='Item')
item_label1.grid()


item_label = ttk.Label(frame, text='Item')
item_label.grid(column=0, row=0, sticky='W', **options)

a= tk.StringVar() #temperature
items_entry = ttk.Entry(frame, textvariable=a) #temperature_entry
items_entry.grid(column=1, row=0, **options)
items_entry.focus()


todo_list = []
checked_list = {}


# def delete_task():
#     try:
#         task_index = todo_list.curselection()
#         todo_list.remove(task_index)
#     except:
#         tk.messagebox.showwarning(title="Warning!", message="You must select a task.")

def insert_sort(item):
    todo_list.append(item)
    todo_list.sort()

def delete_task():
    for box in checked_list:
        if box.var.get() == 1:
            todo_list.remove(checked_list[box])


def convert_button_clicked():
    try:
        item = a.get()
        insert_sort(item)

        Cbcolumn = 0
        Cbrow = 80
        

        
        for Checkbox in range(len(todo_list)): # to add in the list
            name = todo_list[Checkbox]
            current_var = tk.IntVar()
            current_box = tk.Checkbutton(root, text=name, variable=current_var)
            current_box.var = current_var



            
            current_box.grid(row=Cbrow, column=Cbcolumn)
            checked_list[current_box] = name  
            Cbrow += 20 
           
    
    
    except ValueError as error:
        showerror(title='Error', message=error)

convert_button = ttk.Button(frame, text='OK')
convert_button.grid(column=2, row=0, sticky='W', **options)
convert_button.configure(command=convert_button_clicked)

print_cbox_button = tk.Button(root, text='Remove Marked Element', command=delete_task())
print_cbox_button.grid(row=10, column=0, columnspan=3)

frame.grid(padx=10, pady=10)
root.mainloop()