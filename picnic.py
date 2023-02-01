from tkinter import *
import random
root = Tk()

root.title("Picnic Bag List")
root.geometry("600x600")

display_element = Label(root)
rand_num = Label(root)

list_pic = ["Bottle","Tiffin","ID Card","Chocolates","Chips","Tickets","Hankey"]
display_element["text"]="Listid Items: "+str(list_pic)


def generate():
    rand_num2=random.sample(range(0,7),1)
    rand_num["text"]="Put Item No. "+str(rand_num2)+" In The Bag"
    
btn = Button(root,text="Which item to put in the bag",command=generate)

display_element.place(relx=0.5,rely=0.5,anchor=CENTER)
btn.place(relx=0.5,rely=0.7,anchor=CENTER)
rand_num.place(relx=0.5,rely=0.9,anchor=CENTER)
root.mainloop()