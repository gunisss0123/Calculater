from tkinter import *
root = Tk()
root.title("เครื่องคิดเลข")

content = ""
txt_input = StringVar(value="0")

def btn(number):
    global content
    content = content+str(number)
    txt_input.set(content)

def equal():
    global content
    calculate = float(eval(content))
    txt_input.set(calculate)
    content = ""

def delete():
    global content
    content = ""
    txt_input.set("")
    display.insert(0,"0")
#แสดงผล 5 x 4 '
display = Entry(font=('arial',30,'bold'),fg='white',bg="black",textvariable=txt_input,justify="right")
display.grid(columnspan=4)


#รับค่าผ่านปุ่ม


#row1
btn7 = Button(fg="black",font=('arial',30,'bold'),text="7",command=lambda:btn(7),padx=30,pady=15).grid(row=1,column=0)
btn8 = Button(fg="black", font=('arial',30,'bold'),text="8",command=lambda:btn(8),padx=30,pady=15).grid(row=1,column=1)
btn9 = Button(fg="black",font=('arial',30,'bold'),text="9",command=lambda:btn(9),padx=30,pady=15).grid(row=1,column=2)
btnc = Button(bg="orange",fg="black",font=('arial',30,'bold'),command=delete,text="C",padx=30,pady=15).grid(row=1,column=3)

#row2
btn4 = Button(fg="black",font=('arial',30,'bold'),command=lambda:btn(4),text="4",padx=30,pady=15).grid(row=2,column=0)
btn5 = Button(fg="black",font=('arial',30,'bold'),command=lambda:btn(5),text="5",padx=30,pady=15).grid(row=2,column=1)
btn6 = Button(fg="black",font=('arial',30,'bold'),command=lambda:btn(6),text="6",padx=30,pady=15).grid(row=2,column=2)
btnplus = Button(bg="orange",fg="black",font=('arial',30,'bold'),command=lambda:btn("+"),text="+",padx=35,pady=15).grid(row=2,column=3)

#row3
btn1 = Button(fg="black",font=('arial',30,'bold'),command=lambda:btn(1),text="1",padx=30,pady=15).grid(row=3,column=0)
btn2 = Button(fg="black",font=('arial',30,'bold'),command=lambda:btn(2),text="2",padx=30,pady=15).grid(row=3,column=1)
btn3 = Button(fg="black",font=('arial',30,'bold'),command=lambda:btn(3),text="3",padx=30,pady=15).grid(row=3,column=2)
btnminus = Button(bg="orange",fg="black",font=('arial',30,'bold'),command=lambda:btn("-"),text="-",padx=40,pady=15).grid(row=3,column=3)

#row4
btndot = Button(fg="black",font=('arial',30,'bold'),command=lambda:btn("."),text=".",padx=35,pady=15).grid(row=4,column=0)
btn0 = Button(fg="black",font=('arial',30,'bold'),command=lambda:btn(0),text="0",padx=30,pady=15).grid(row=4,column=1)
btndivision = Button(bg="orange",fg="black",font=('arial',30,'bold'),command=lambda:btn("/"),text="/",padx=35,pady=15).grid(row=4,column=2)
btnmultiply = Button(bg="orange",fg="black",font=('arial',30,'bold'),command=lambda:btn("*"),text="x",padx=35,pady=15).grid(row=4,column=3)

#row5
btnequal = Button(bg="green",fg="black",font=('arial',30,'bold'),command=equal,text="=",padx=100,pady=15).grid(row=5,column=0,columnspan=2)
btnopen = Button(bg="orange",fg="black",font=('arial',30,'bold'),command=lambda:btn("("),text="(",padx=35,pady=15).grid(row=5,column=2)
btnopen = Button(bg="orange",fg="black",font=('arial',30,'bold'),command=lambda:btn(")"),text=")",padx=35,pady=15).grid(row=5,column=3)



root.mainloop()