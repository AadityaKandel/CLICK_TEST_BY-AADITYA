from tkinter import *
import time
import tkinter.messagebox as tmsg
import os

try:
	os.mkdir('Score')
except:
	pass

try:
	f = open('Score/score.txt','r+')
	f.close()
except:
	tmsg.showwarning('Error','Score File Is Not Found [ Press Okay To Repair The Program ]')
	f = open('Score/score.txt','a+')
	f.close()
	tmsg.showinfo('Success','Success, Program Repaired. Please Close And Open Program Again')
	quit()

root = Tk()

root.title('Mouse Click Test')

def clicksme():
	numvalv.set((numvalv.get())+1)
	root.update()

def worksdone():
	b1.config(command=clickme)
	l4.config(state=NORMAL)
	l6.config(state=NORMAL)
	l7.config(state=NORMAL)
	tmsg.showinfo('WOW',f'WOW {(name.get())}, You Clicked {(numvalv.get())} Times Within {(urclicks.get())} Seconds.')
	

	f = open('Score/score.txt','a+')
	f.write(f'\n{(name.get())}: {(numvalv.get())} Clicks On {(urclicks.get())} Seconds')
	f.close()
	
	numvalv.set(0)
def ses():
	os.startfile('Score\\score.txt')

def clickme():
	if (urclicks.get())>100:
		tmsg.showwarning('Warning','Higher Than 100 Seconds Is Not Allowed')
	elif (urclicks.get())<1:
		tmsg.showwarning('Warning','Lower Than 1 Second Is Not Allowed')
	elif (name.get())=="":
		tmsg.showwarning('Warning','Name Is Empty')
	else:
		l4.config(state=DISABLED)
		l6.config(state=DISABLED)
		l7.config(state=DISABLED)
		b1.config(command=clicksme)
		clicksme()
		root.after((urclicks.get())*1000,worksdone)

def plus():
	urclicks.set((urclicks.get())+1)

def minus():
	urclicks.set((urclicks.get())-1)

numvalv = IntVar()
urclicks = IntVar()
name = StringVar()

f1 = Frame(borderwidth = 10,bg="black")

l1 = Label(f1,text = "Clicks: ",bg="black",fg="red",font="comicsansms 14 bold")
l1.pack(side=LEFT)

l2 = Label(f1,textvariable = numvalv,bg="black",fg="white",font="comicsansms 14 bold")
l2.pack(side=LEFT)

l3 = Label(f1,text = "                    Timer: ",bg="black",fg="red",font="comicsansms 14 bold")
l3.pack(side=LEFT)

l4 = Entry(f1,textvariable=urclicks,bg="white",fg="black",state=NORMAL,font="comicsansms 12 bold",width=3)
l4.pack(side=LEFT)

l5 = Label(f1,text = "s",bg="black",fg="white",font="comicsansms 14 bold")
l5.pack(side=LEFT)

l6 = Button(f1,text = "  +  ",bg="black",fg="white",font="comicsansms 14 bold",borderwidth=0,command=plus)
l6.pack(side=LEFT)

l7 = Button(f1,text = "-",bg="black",fg="white",font="comicsansms 14 bold",borderwidth=0,command=minus)
l7.pack(side=LEFT)

l8 = Label(f1,text = "   Name: ",bg="black",fg="red",font="comicsansms 14 bold")
l8.pack(side=LEFT)

l9 = Entry(f1,textvariable=name,bg="white",fg="black",state=NORMAL,font="comicsansms 12 bold")
l9.pack(side=LEFT)

Label(f1,text = "       ",bg="black",fg="red",state=NORMAL,font="comicsansms 16 bold").pack(side=LEFT)

l10 = Button(f1,text = "See My Score",bg="black",fg="red",state=NORMAL,font="comicsansms 16 bold",command=ses)
l10.pack(side=LEFT)

f1.pack(anchor="w")

b1 = Button(text="CLICK ME",pady=200,padx=380,bg="black",fg="white",borderwidth=10,relief=SUNKEN,font="impact 20 italic",command=clickme)
b1.pack()

root.config(bg="black")
root.mainloop()