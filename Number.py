from tkinter import*
import random
root=Tk()

root.title("Lucky Friend")
root.geometry("400x400")
root.configure(background="light green")

List1=["A","S","R","K","B","L","N","M","O"]
print(List1)

def Alphabate():
    randomnumb=random.randint(0,5)
    print(randomnumb)
    randomname=List1[randomnumb]
    print(randomname)


btn=Button(root,text="Genarate random words",command=Alphabate)
btn.place(relx=0.5,rely=0.5,anchor=CENTER)


root.mainloop()