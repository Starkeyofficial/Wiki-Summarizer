import wikipedia
def search():
    data=wikipedia.summary(thing.get(),10)
    with open("search_result.txt","w") as file:
        file.write(data)
import os
def Open():
    os.system("search_result.txt")
from tkinter import *
master=Tk()
master.title("Wiki searcher")
label1=Label(master,text="Wikipedia Search",font=("Arial",16,"bold")).grid(row=0,column=0)
label2=Label(master,text="Enter something to search",font=("Arial",8,"italic")).grid(row=1,column=0)
thing=Entry(master)
button1=Button(master,text="Search and Save",padx=15,pady=8,command=search).grid(row=3,column=0)
button2=Button(master,text="Open",padx=15,pady=8,command=Open).grid(row=4,column=0)
thing.grid(row=2,column=0,ipadx=20,ipady=10)
master.mainloop()