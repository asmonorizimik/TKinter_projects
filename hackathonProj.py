def add():
    listbox.insert(listbox.size(),entryBox.get())
    listbox.config(height=listbox.size())

import tkinter
root=tkinter.Tk()
root.title("WELCOME")

label=tkinter.Label(root,text="TEAM PROJECT",font=("Arial Bold",60),fg="Tomato").pack(pady=30,padx=30)
root.geometry("600x600")
# ImageTk,ImageSequence

def run_animation():
    while True:
        try:
            global photo
            global frame
            global label
            photo = tkinter.PhotoImage(
                # file = photo_path,
                format = "gif - {}".format(frame)
                )

            label.configure(image = "nextframe")

            frame = frame + 1

        except Exception:
            frame = 1
            break

# root = Tk()
# photo_path = "/home/dhanashri/Download/saiphoto.gif"

# photo = tkinter.PhotoImage(
#     file = photo_path,
#     )
# label = tkinter.Label(
#     image = photo
#     )
# animate = tkinter.Button(
#     root,
#     text = "animate",
#     command = run_animation
#     )

# label.pack(side=tkinter.LEFT)
# animate.pack(side=tkinter.LEFT)




def insert_sort(item):
    listbox.append(item)
    listbox.sort()

def submit():
    items=[]
    for index in listbox.curselection():
        items.insert(index,listbox.get(index))
    
    
    print("selection of item:")
    # print(listbox.get(listbox.curselection()))
    for index in items:
        print(index)

def delete():
    for index in reversed (listbox.curselection()):
        listbox.delete(index)
    
    listbox.config(height=listbox.size())
       
    

# b=tkinter.Button(root,text="click",font=("Arial BOLD",30),bg="pink",fg="blue").pack(pady=30,padx=30)
# r=tkinter.Radiobutton(root,text="Rose",value=1,font=("Arial Bold",20),bg="green",fg="pink").pack(pady=12,padx=12)
listbox=tkinter.Listbox(root,fg="blue",bg="Aquamarine",
                        font=("constantia",35),
                        width=12,
                        selectmode=tkinter.MULTIPLE)
listbox.pack(padx=34,pady=34)

listbox.insert(1,"Banana")
listbox.insert(2,"Apple")
listbox.insert(3,"Strawberry")
listbox.insert(4,"Grapes")
listbox.insert(5,"Oranges")

listbox.config(height=listbox.size())

entryBox=tkinter.Entry(root,bg="PaleVioletRed",font=("Arial BOLD",15),width=15)
entryBox.pack()

submitButton=tkinter.Button(root,text="submit",command=submit,bg="green",fg="pink",font=("Arial BOLD",30))
submitButton.pack(padx=38,pady=38)

addButton=tkinter.Button(root,text="add",command=add,font=("Arial BOLD",30),bg="SkyBlue",fg="red")
addButton.pack(padx=24,pady=24)

deleteButton=tkinter.Button(root,text="delete",command=delete,font=("Arial BOLD",30),bg="Crimson",fg="white")
deleteButton.pack(padx=24,pady=24)



root.mainloop()