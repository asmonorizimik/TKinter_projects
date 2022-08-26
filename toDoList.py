# import tkinter
# from tkinter import END
# def add_to_list():
#       listbox.insert(END,entry.get())
#       entry.delete(0,END)


# def remove_from_list():
#       # print(listbox.curselection())
#       listbox.delete(listbox.curselection())

# tk=tkinter.Tk()
# tk.title("listbox")
# listbox=tkinter.Listbox(tk)
# listbox.pack()

# entry=tkinter.Entry(tk)
# entry.pack()

# button=tkinter.Button(tk,text="add item",command=add_to_list)
# button.pack()

# button=tkinter.Button(tk,text="remove",command=remove_from_list)
# button.pack()
# tk.mainloop()












import tkinter
from tkinter import ttk
import tkinter.messagebox
root = tkinter.Tk()
root.title("team list")
root.configure(bg="black")
root.geometry=("500*500")
root.resizable(width=True,height=True)

check_list=[]




def add_task():
    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(tkinter.END, task)
        entry_task.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="Warning!", message="You must enter a task.")


def delete_task():
    try:
        task_index = listbox_tasks.curselection()
        listbox_tasks.delete(task_index)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="You must select a task.")





frame_tasks = tkinter.Frame(root)
frame_tasks.pack()
listbox_tasks1=ttk.Label(frame_tasks,text="NAVGURUKUL BANGALORE CAMPUS TEAM LIST",font="normal 11 bold",background="pink",)
# listbox_tasks1 =tkinter.Listbox(frame_tasks,bg="pink",height=2,width=50)
listbox_tasks1.pack(side=tkinter.TOP)


listbox_tasks = tkinter.Listbox(frame_tasks,bg="darkseagreen", height=10, width=50)
listbox_tasks.pack(side=tkinter.LEFT)

scrollbar_tasks = tkinter.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tkinter.RIGHT, fill=tkinter.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task = tkinter.Entry(root, width=50)
entry_task.pack()

button_add_task = tkinter.Button(root, text="OK",bg="pink", width=20, command=add_task)
button_add_task.pack(side=tkinter.LEFT)

button_delete_task = tkinter.Button(root, text="Delete",bg="pink", width=20, command=delete_task)
button_delete_task.pack(side=tkinter.RIGHT)
root.mainloop()