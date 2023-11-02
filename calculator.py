from tkinter import *

def click(event):
    text = event.widget.cget('text')
    if text == '=':
        try:
            result = str(eval(value.get()))
            value.set(result)
        except Exception as e:
            value.set('Error')
    elif text == 'C':
        value.set('')
    else:
        value.set(value.get() + text)
root=Tk()
root.geometry('300x500')
root.title("Calculator")

value=StringVar()
value.set('')
screen=Entry(root,textvariable=value,font='lucida 30 bold',relief=SUNKEN)
screen.pack(fill=X)

f=Frame(root, bg='grey')
b1=Button(f,text='9',font='lucida 25 bold',command=click)
b1.pack(side=LEFT,padx=5,pady=5)
b1.bind('<Button-1>',click)

b1=Button(f,text='8',font='lucida 25 bold',command=click)
b1.pack(side=LEFT,padx=5,pady=5)
b1.bind('<Button-1>',click)

b1=Button(f,text='7',font='lucida 25 bold',command=click)
b1.pack(side=LEFT,padx=5,pady=5)
b1.bind('<Button-1>',click)

b1=Button(f,text='+',font='lucida 25 bold',command=click)
b1.pack(side=LEFT,padx=5,pady=5)
b1.bind('<Button-1>',click)

f.pack(padx=10,pady=10)


f=Frame(root, bg='grey')


b1=Button(f,text='6',font='lucida 25 bold',command=click)
b1.pack(side=LEFT,padx=5,pady=5)
b1.bind('<Button-1>',click)

b1=Button(f,text='5',font='lucida 25 bold',command=click)
b1.pack(side=LEFT,padx=5,pady=5)
b1.bind('<Button-1>',click)

b1=Button(f,text='4',font='lucida 25 bold',command=click)
b1.pack(side=LEFT,padx=5,pady=5)
b1.bind('<Button-1>',click)

b1=Button(f,text='-',font='lucida 25 bold',command=click)
b1.pack(side=LEFT,padx=5,pady=5)
b1.bind('<Button-1>',click)


f.pack(padx=10,pady=10)

f=Frame(root, bg='grey')

b1=Button(f,text='3',font='lucida 25 bold',command=click)
b1.pack(side=LEFT,padx=5,pady=5)
b1.bind('<Button-1>',click)

b1=Button(f,text='2',font='lucida 25 bold',command=click)
b1.pack(side=LEFT,padx=5,pady=5)
b1.bind('<Button-1>',click)

b1=Button(f,text='1',font='lucida 25 bold',command=click)
b1.pack(side=LEFT,padx=5,pady=5)
b1.bind('<Button-1>',click)

b1=Button(f,text='*',font='lucida 25 bold',command=click)
b1.pack(side=LEFT,padx=5,pady=5)
b1.bind('<Button-1>',click)


f.pack(padx=10,pady=10)

f=Frame(root, bg='grey')

b1=Button(f,text='C',font='lucida 25 bold',command=click)
b1.pack(side=LEFT,padx=5,pady=5)
b1.bind('<Button-1>',click)

b1=Button(f,text='0',font='lucida 25 bold',command=click)
b1.pack(side=LEFT,padx=5,pady=5)
b1.bind('<Button-1>',click)

b1=Button(f,text='=',font='lucida 25 bold',command=click)
b1.pack(side=LEFT,padx=5,pady=5)
b1.bind('<Button-1>',click)

b1=Button(f,text='/',font='lucida 25 bold',command=click)
b1.pack(side=LEFT,padx=5,pady=5)
b1.bind('<Button-1>',click)


f.pack(padx=10,pady=10)

root.mainloop()