from tkinter import *

root=Tk()
root.title("Simple Calculator")
e=Entry(root,width=35,borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
e.insert(0,"")


def button_click(number):
    current=e.get()
    e.delete(0,END)
    e.insert(0 ,str(current)+str(number))

def button_clearing():
    e.delete(0,END)

def button_adding():
    first_num=e.get()
    global f_num
    global math
    math="addition"
    f_num=int(first_num)
    e.delete(0,END)

def button_eql():
    second_number=e.get()
    e.delete(0,END)
    if math=="addition":
        e.insert(0,f_num+int(second_number))
    elif math=="multiplication":
        e.insert(0,f_num*int(second_number))
    elif math=="division":
        e.insert(0,f_num/int(second_number))
    elif math=="modulus":
        e.insert(0,f_num%int(second_number))

def button_multiplying():
    first_num = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_num)
    e.delete(0, END)

def button_dividing():
    first_num = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_num)
    e.delete(0, END)

def button_modulusing():
    first_num = e.get()
    global f_num
    global math
    math = "modulus"
    f_num = int(first_num)
    e.delete(0, END)

#define buttons
button_1=Button(root,text="1",padx=40,pady=20,command=lambda: button_click(1))
button_2=Button(root,text="2",padx=40,pady=20,command=lambda: button_click(2))
button_3=Button(root,text="3",padx=40,pady=20,command=lambda: button_click(3))
button_4=Button(root,text="4",padx=40,pady=20,command=lambda: button_click(4))
button_5=Button(root,text="5",padx=40,pady=20,command=lambda: button_click(5))
button_6=Button(root,text="6",padx=40,pady=20,command=lambda: button_click(6))
button_7=Button(root,text="7",padx=40,pady=20,command=lambda: button_click(7))
button_8=Button(root,text="8",padx=40,pady=20,command=lambda: button_click(8))
button_9=Button(root,text="9",padx=40,pady=20,command=lambda: button_click(9))
button_0=Button(root,text="0",padx=40,pady=20,command=lambda: button_click(0))
button_add=Button(root,text="+",padx=20,pady=20,command=button_adding,bg="#dea5a4")
button_equals=Button(root,text="=",padx=80,pady=20,command=button_eql)
button_clear=Button(root,text="C",padx=80,pady=20,command=lambda: button_clearing())
button_multiply=Button(root,text=" * ",padx=20,pady=20,command=button_multiplying,bg="#dea5a4")
button_divide=Button(root,text=" / ",padx=20,pady=20,command=button_dividing,bg="#dea5a4")
button_modulus=Button(root,text=" % ",padx=20,pady=20,command=button_modulusing,bg="#dea5a4")

#display buttons
button_1.grid(row=4 ,column= 0)
button_2.grid(row= 4,column= 1)
button_3.grid(row= 4,column= 2)

button_4.grid(row=3,column= 0)
button_5.grid(row= 3,column= 1)
button_6.grid(row= 3,column= 2)

button_7.grid(row= 2,column= 0)
button_8.grid(row= 2,column= 1)
button_9.grid(row= 2,column= 2)

button_0.grid(row= 5,column= 0)
button_equals.grid(row=5,column=1,columnspan=2)
button_add.grid(row=2,column=3)
button_multiply.grid(row=3,column=3)
button_divide.grid(row=4,column=3)
button_modulus.grid(row=5,column=3)

button_clear.grid(row=1,column=0,columnspan=2)

root.mainloop()