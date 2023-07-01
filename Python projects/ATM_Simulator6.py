from tkinter import *
import time

root =Tk()
root.geometry("900x150")
root.title("ATM Simulator")
root.configure(bg="grey")

Tops=Frame(root,bg="black",width=800,height=50,relief="sunken")
Tops.pack(side=TOP)

f1=Frame(root,bg="black",width=300,height=700,relief="sunken")
f1.pack(side=LEFT)

f2=Frame(root,bg="black",width=400,height=700,relief="sunken")
f2.pack(side=RIGHT)

localtime =time.asctime(time.localtime(time.time()))

label1 =Label(Tops,font=("Times New Roman",30,'bold') ,text="ATM Simulator", fg="powder blue",bg="grey",bd=10)
label1.grid(row=0,column=0)

label1=Label(Tops,font=("Times New Roman",30,'bold'), text=localtime,fg="powder blue",bg="grey",bd=10)
label1.grid(row=1,column=0)

number = StringVar()
amount = StringVar()
withdraw = StringVar()
acca = " "

def bank():
    global acca
    accno = ["3456","4545","0056"]
    account = number.get()
    if account in accno :
        label.config(text="Registered User")
        bank = {"3456":10000,"4545":1459,"0056":6700}
        balance=bank[account]
        acca = balance
    else:
        label.config(text="unregistered User")

def deposit():
    global acca
    amo = float(amount.get())
    bal = acca+amo
    label3.config(text=("Net Balance",str(bal)))

def withdrawn():
    global acca
    wd=float(withdraw.get())
    if acca>=wd:
        ace=acca-wd
        label4.configure(text=("Net Balance",str(ace)))
    else:
        label4.config(text="insufficient balance")

def reset():
    number.set("")
    amount.set("")
    withdraw.set("")
    label.config(text="")
    label3.config(text="")
    label4.config(text="")
    label5.config(text="")

def bal():
    global acca
    label5.config(text=("Net balance",str(acca)))


lb1=Label(f1, font=("Times New Roman",15,'bold'),text="enter account number:    ",fg="powder blue",bg="grey",bd=10)
lb1.grid(row=0,column=3)
text=Entry(f1,font=("Times New Roman",15,'bold'),bg="grey",bd=6,textvariable=number,insertwidth=4,justify="right")
text.grid(row=0,column=4)
label=Label(f1,font=("Times New Roman",15,'bold'),bg="grey",fg="white")
label.grid(row=1,column=4)
btnsubmit=Button(f2,padx=16,pady=4,bd=10,fg="black",font=("Times New Roman",15,'bold'),width=7,text="Submit",bg="powder blue",command=bank)
btnsubmit.grid(row=0,column=4)

lblTotal=Label(f1,text="                  ",fg="white",bg="black")
lblTotal.grid(row=3,columnspan=10)

lb1=Label(f1, font=("Times New Roman",15,'bold'),text="enter the amount to deposit:    ",fg="powder blue",bg="grey",bd=10)
lb1.grid(row=4,column=3)
text=Entry(f1,font=("Times New Roman",15,'bold'),bg="grey",bd=6,textvariable=amount,insertwidth=4,justify="right")
text.grid(row=4,column=4)
label3=Label(f1,font=("Times New Roman",15,'bold'),bg="grey",fg="white")
label3.grid(row=5,column=4)
btndeposit=Button(f2,padx=16,pady=4,bd=10,fg="black",font=("Times New Roman",15,'bold'),width=7,text="Deposit",bg="powder blue",command=deposit)
btndeposit.grid(row=4,column=4)

lblTotal=Label(f1,text="                  ",fg="white",bg="black")
lblTotal.grid(row=7,columnspan=10)

lb1=Label(f1, font=("Times New Roman",15,'bold'),text="enter the amount to Withdraw:    ",fg="powder blue",bg="grey",bd=10)
lb1.grid(row=8,column=3)
text=Entry(f1,font=("Times New Roman",15,'bold'),bg="grey",bd=6,textvariable=withdraw,insertwidth=4,justify="right")
text.grid(row=8,column=4)
label4=Label(f1,font=("Times New Roman",15,'bold'),bg="grey",fg="white")
label4.grid(row=9,column=4)
label5=Label(f1,font=("Times New Roman",15,'bold'),bg="grey",fg="white")
label5.grid(row=10,column=4)

btnwithd=Button(f2,padx=16,pady=4,bd=10,fg="black",font=("Times New Roman",15,'bold'),width=7,text="Withdrawl",bg="powder blue",command=withdrawn)
btnwithd.grid(row=8,column=4)
btnbal=Button(f2,padx=16,pady=4,bd=10,fg="black",font=("Times New Roman",15,'bold'),width=7,text="Balance",bg="powder blue",command=bal)
btnbal.grid(row=10,column=4)
btnreset=Button(f2,padx=16,pady=4,bd=10,fg="black",font=("Times New Roman",15,'bold'),width=7,text="Reset",bg="powder blue",command=reset)
btnreset.grid(row=11,column=4)
btnexit=Button(f2,padx=16,pady=4,bd=10,fg="black",font=("Times New Roman",15,'bold'),width=7,text="Exit",bg="powder blue",command=root.destroy)
btnexit.grid(row=12,column=4)

root.mainloop()