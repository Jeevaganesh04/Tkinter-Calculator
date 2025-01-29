from tkinter import *
import math

root=Tk()
root.title('Calculator App')

def btn_click(value):
    global data
    data=data+str(value)
    input_text.set(data)

def btn_equal():
    global data
    result=str(eval(data))
    input_text.set(result)

def btn_clear():
    global data
    data=" "
    input_text.set(' ')
    
def btn_erase():
    global data
    if data:
        data=data[:-1]
        input_text.set(data)
    else:
        input_text.set(' ')

def btn_sqr():
    global data
    global val
    val=eval(data)
    result=val*val
    input_text.set(result)

def btn_sqrt():
    global data
    global val
    val=eval(data)
    result=math.sqrt(val)
    input_text.set(result)

        
val=""   
data=" "
input_text=StringVar()

input_frame=Frame(root,width=300,height=20,highlightbackground='black',highlightthickness=1)
input_frame.pack(side=TOP)

input_field=Entry(input_frame,bg='#eef',textvariable=input_text,width=23,highlightthickness=4,justify=RIGHT,font=('times',20,'bold'))
input_field.grid(row=0,column=0)
input_field.pack(ipady=10)

btn_frame=Frame(root,width=300,height=220,bg='black')
btn_frame.pack()


#First Row
clear=Button(btn_frame,text='C',command=lambda:btn_clear(),highlightthickness=0,bd=0,width=35,height=4).grid(row=0,column=0,columnspan=3,padx=1,pady=1)
divide=Button(btn_frame,text='/',command=lambda:btn_click('/'),bd=0,highlightthickness=0,width=11,height=4).grid(row=0,column=3,columnspan=1,padx=1,pady=1)
erase=Button(btn_frame,text='<-',command=lambda:btn_erase(),bd=0,highlightthickness=0,width=11,height=4).grid(row=0,column=4,columnspan=1,padx=1,pady=1)


#second Row
seven=Button(btn_frame,text='7',command=lambda:btn_click(7),bd=0,highlightthickness=4,width=10,height=3).grid(row=1,column=0,columnspan=1,padx=1,pady=1)
eight=Button(btn_frame,text='8',command=lambda:btn_click(8),bd=0,highlightthickness=4,width=10,height=3).grid(row=1,column=1,columnspan=1,padx=1,pady=1)
nine=Button(btn_frame,text='9',command=lambda:btn_click(9),bd=0,highlightthickness=4,width=10,height=3).grid(row=1,column=2,columnspan=1,padx=1,pady=1)
multiple=Button(btn_frame,text='x',command=lambda:btn_click('*'),bd=0,highlightthickness=4,width=10,height=3).grid(row=1,column=3,columnspan=1,padx=1,pady=1)
sqr=Button(btn_frame,text='**',command=lambda:btn_sqr(),bd=0,highlightthickness=4,width=10,height=7).grid(row=1,column=4,columnspan=1,rowspan=2,padx=1,pady=1)

#Third Row
six=Button(btn_frame,text='6',command=lambda:btn_click(6),bd=0,highlightthickness=4,width=10,height=3).grid(row=2,column=0,columnspan=1,padx=1,pady=1)
five=Button(btn_frame,text='5',command=lambda:btn_click(5),bd=0,highlightthickness=4,width=10,height=3).grid(row=2,column=1,columnspan=1,padx=1,pady=1)
four=Button(btn_frame,text='4',command=lambda:btn_click(4),bd=0,highlightthickness=4,width=10,height=3).grid(row=2,column=2,columnspan=1,padx=1,pady=1)
plus=Button(btn_frame,text='+',command=lambda:btn_click('+'),highlightthickness=4,bd=0,width=10,height=3).grid(row=2,column=3,columnspan=1,padx=1,pady=1)
sqrt=Button(btn_frame,text='SQRT',command=lambda:btn_sqrt(),bd=0,highlightthickness=4,width=10,height=7).grid(row=3,column=4,columnspan=1,rowspan=2,padx=1,pady=1)

#Fourth Row
three=Button(btn_frame,text='3',command=lambda:btn_click(3),bd=0,highlightthickness=4,width=10,height=3).grid(row=3,column=0,columnspan=1,padx=1,pady=1)
two=Button(btn_frame,text='2',command=lambda:btn_click(2),bd=0,highlightthickness=4,width=10,height=3).grid(row=3,column=1,columnspan=1,padx=1,pady=1)
one=Button(btn_frame,text='1',command=lambda:btn_click(1),bd=0,highlightthickness=4,width=10,height=3).grid(row=3,column=2,columnspan=1,padx=1,pady=1)
minus=Button(btn_frame,text='-',command=lambda:btn_click('-'),bd=0,highlightthickness=4,width=10,height=3).grid(row=3,column=3,columnspan=1,padx=1,pady=1)

#Fifth Row
zero=Button(btn_frame,text='0',bd=0,highlightthickness=4,width=22,command=lambda:btn_click(0),height=3).grid(row=4,column=0,columnspan=2,padx=1,pady=1)
dot=Button(btn_frame,text='.',bd=0,highlightthickness=4,width=10,height=3,command=lambda:btn_click('.')).grid(row=4,column=2,padx=1,pady=1)
equal=Button(btn_frame,text='=',highlightthickness=4,command=lambda:btn_equal(),bd=0,width=10,height=3).grid(row=4,column=3,padx=1,pady=1)


root.mainloop()


#Weather Application:
