from tkinter import *
window=Tk()
#-------------------------Widgets---------------------------

img = PhotoImage(file="C:\\Users\\TROJAN\\Downloads\\minecraft.png")
imglbl1=Label(window,image=img)
label1=Label(window,relief="groove",width=8)
label2=Label(window,relief="groove",width=8)
label3=Label(window,relief="groove",width=8)
label4=Label(window,relief="groove",width=8)
label5=Label(window,relief="groove",width=8)
label6=Label(window,relief="groove",width=8)
getbtn=Button(window)
resbtn=Button(window)

#------------------------------------------------------------

#--------------------------geometry--------------------------

imglbl1.grid(row=1,column=1,rowspan=2)
label1.grid(row=1,column=2,padx=10)
label2.grid(row=1,column=3,padx=10)
label3.grid(row=1,column=4,padx=10)
label4.grid(row=1,column=5,padx=10)
label5.grid(row=1,column=6,padx=10)
label6.grid(row=1,column=7,padx=10)
getbtn.grid(row=2,column=2,columnspan=4)
resbtn.grid(row=2,column=6,columnspan=2)

#------------------------------------------------------------

#------------------------static-properties-------------------

window.title("LOTTO NUMBER PCIKER")
window.resizable(0,0)
getbtn.configure(text="Get My LUCKY NUMBER")
resbtn.configure(text="RESET")

#------------------------------------------------------------

#--------------------initial-properties----------------------

label1.configure(text="...")
label2.configure(text="...")
label3.configure(text="...")
label4.configure(text="...")
label5.configure(text="...")
label6.configure(text="...")
resbtn.configure(state=DISABLED)

#-------------------------------------------------------------

#--------------------dynamic-properties-----------------------

from random import sample


def pick():
    nums=sample(range(1,9),6)
    label1.configure(text=nums[0])
    label2.configure(text=nums[1])
    label3.configure(text=nums[2])
    label4.configure(text=nums[3])
    label5.configure(text=nums[4])    
    label6.configure(text=nums[5])
    getbtn.configure(state=DISABLED)
    resbtn.configure(state=NORMAL)


def reset():
    label1.configure(text="...")
    label2.configure(text="...")
    label3.configure(text="...")
    label4.configure(text="...")
    label5.configure(text="...")
    label6.configure(text="...")
    getbtn.configure(state=NORMAL)
    resbtn.configure(state=DISABLED)

getbtn.configure(command=pick)
resbtn.configure(command=reset)

#------------------------------------------------------------

window.mainloop()




