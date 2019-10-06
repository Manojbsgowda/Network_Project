from tkinter import *

def fConvert():
    mtext=data.get()
    mtextdata=data2.get()
    scrollbar=Scrollbar(root,orient=VERTICAL)
    scrollbar.grid(row=4,column=1,sticky=W)

    Disp=Text(root,wrap=WORD,height=5,width=57,yscrollcommand=scrollbar.set)
    Disp.grid(row=4,column=1,sticky=W)

    scrollbar.config(command=Disp.yview)
    EncData=list()
    DecData=list()
    if var.get()==1:
        print ("want to encrypt")
        for some in mtext:
            EncData.append(chr((ord(some)+int(mtextdata))%256))
        stringdata=''.join(EncData)
        #print stringdata
        Disp.insert(INSERT,stringdata)
    if var.get()==2:
        print ("want to Decrypt")
        for some in mtext:
            DecData.append(chr((ord(some)-int(mtextdata))%256))
        stringdata=''.join(DecData)
        #print stringdata
        Disp.insert(INSERT,stringdata)
    return

#create the window
root=Tk()
data=StringVar()        #some string variables
data1=StringVar()
data2=StringVar()
data3=StringVar()
var=IntVar()        #used for designing radio buttons
gFlag=0

#modify root window
root.title("Encrypt or Decrypt your Message")
#root.geometry("1000x200")

mRadio0=Radiobutton(root,text="Encrypt",variable=var,value=1).grid(row=0,column=0)
mRadio0=Radiobutton(root,text="Decrypt",variable=var,value=2).grid(row=0,column=1)

data1.set("Enter the number with which you want to Encrypt:")
mTextNumber=Label(root,textvariable=data1).grid(row=1,column=0,sticky=E)

mNumber=Entry(root,textvariable=data2,width=10).grid(row=1,column=1)

data3.set("Please write/paste your data in the box below, then hit CONVERT button")
mLabel2=Label(root,textvariable=data3,anchor=S,fg="red").grid(row=2,column=0)

mEntry=Entry(root,textvariable=data,width=50).grid(row=3,column=0)
mbutton=Button(root,text="CONVERT",command=fConvert).grid(row=3,column=1)

scrollbar=Scrollbar(root)
scrollbar.grid(row=4,column=1,sticky=W)

Disp=Text(root,wrap=WORD,height=5,width=57,yscrollcommand=scrollbar.set)
Disp.grid(row=4,column=0,sticky=W)

scrollbar.config(command=Disp.yview)
#kick off the main event loop
root.mainloop()

