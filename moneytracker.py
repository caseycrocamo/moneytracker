import os
import tkinter
from tkinter import *

class Frames(object):

    def __init__(self):
        self.fname = StringVar()
        self.itemcount = 0
        self.date = StringVar()
        self.arr = None
        self.catlist = ['snack',
                        'bread',
                        'fruit',
                        'pre-prepared',
                        'drink',
                        'dairy',
                        'protein',
                        'non-food',
                        'vegetable',
                        'seasoning',
                        'cereal']

    def quit(self):
        self.root.destroy()
        sys.exit()

    def first_frame(self, root):
        self.firstframe = Frame(root)
        self.firstframe.grid(row = 0, column = 0)
        root.title('MoneyTracker v2.0')
        root.iconbitmap(default = 'sif.ico')
        #widgets
        #labels
        Label(self.firstframe, text = 'filename (omit filetype)').grid(row = 0, column = 0, pady = 5, sticky = N)
        datelabel = Label(self.firstframe, text = 'date (DD MM YYYY)').grid(row = 1, column = 0, pady = 5, sticky = N)
        #text fields
        Entry(self.firstframe, textvariable = self.fname).grid(row = 0, column = 1, pady = 5, sticky = N)
        Entry(self.firstframe, textvariable = self.date).grid(row = 1, column = 1, pady = 5, sticky = N)
        #buttons
        Button(self.firstframe, text = 'Add Items', command = lambda: self.moveOn(root)).grid(row = 2, column = 0, pady = 5, sticky = N)
        Button(self.firstframe, text = 'Price List', command = lambda: self.skip(root)).grid(row = 2, column = 1, pady = 5, sticky = N)

    def item_frame(self, root):
        self.itemframe = Frame(root)
        #frames
        checkframe = Frame(self.itemframe)
        self.itemframe.grid(row = 0, column = 0)
        #labels
        catlabel = Label(self.itemframe, text = 'Select Category')
        pricelabel = Label(self.itemframe, text = 'Enter Price')
        splitlabel = Label(self.itemframe, text = "Who's in?")
        #listboxes
        self.catbox = Listbox(self.itemframe, selectmode = SINGLE)
        #populate listbox
        for i in self.catlist:
            self.catbox.insert(END, i)
        #entry fields
        self.priceentry = StringVar()
        pricefield = Entry(self.itemframe, textvariable = self.priceentry)
        #checkbox
        self.yardenIn = IntVar()
        self.caseyIn = IntVar()
        self.nateIn = IntVar()
        self.loliIn = IntVar()
        self.otherIn = IntVar()
        ybox = Checkbutton(checkframe, text = "Yarden", variable = self.yardenIn)
        cbox = Checkbutton(checkframe, text = "Casey", variable = self.caseyIn)
        nbox = Checkbutton(checkframe, text = "Nate", variable = self.nateIn)
        lbox = Checkbutton(checkframe, text = "Loli", variable = self.loliIn)
        obox = Checkbutton(checkframe, text = "Other", variable = self.otherIn)
        #buttons
        nextbutt = Button(self.itemframe, text = 'Next Item --->', command = lambda: self.nextFunc(root))
        donebutt = Button(self.itemframe, text = 'Done with List', command = lambda: self.doneFunc(root))
        #grid
        self.itemframe.grid(row = 0, column = 0)
        catlabel.grid(row = 0, column = 0, pady = 5, sticky = N)
        pricelabel.grid(row = 0, column = 1, pady = 5, sticky = N)
        splitlabel.grid(row = 0, column = 2, pady = 5, sticky = N)
        self.catbox.grid(row = 1, column = 0, pady = 5, sticky = N)
        pricefield.grid(row = 1, column = 1, pady = 5, sticky = N)
        checkframe.grid(row = 1, column = 2, pady = 5, sticky = N)
        ybox.grid(row = 0, column = 0, pady = 5, sticky = N)
        cbox.grid(row = 0, column = 1, pady = 5, sticky = N)
        nbox.grid(row = 0, column = 2, pady = 5, sticky = N)
        lbox.grid(row = 0, column = 3, pady = 5, sticky = N)
        nextbutt.grid(row = 2, column = 0, pady = 5, sticky = N)
        donebutt.grid(row = 2, column = 1, pady = 5, sticky = N)

    def price_frame(self, root):
        self.priceframe = Frame(root)
        self.priceframe.grid(row = 0, column = 0)
        Label(self.priceframe, text = 'You paid $'+str(self.caseyfinal)).grid(row = 0, column = 0)
        Label(self.priceframe, text = 'Yarden paid $'+str(self.yardenfinal)).grid(row = 1, column = 0)
        Label(self.priceframe, text = 'Loli paid $'+str(self.lolifinal)).grid(row = 2, column = 0)
        Label(self.priceframe, text = 'Nate paid $'+str(self.natefinal)).grid(row = 3, column = 0)
        Label(self.priceframe, text = 'Other paid $'+str(self.otherfinal)).grid(row = 4, column = 0)
        Label(self.priceframe, text = 'The total bill is $'+str(self.totalbill)).grid(row = 5, column = 0)
        Button(self.priceframe, text = 'Done', command = quit).grid(row = 6, column = 0)

    def skip(self, root):
        self.createf()
        self.pricelist()
        self.firstframe.grid_forget()
        self.price_frame(root)
        
    def moveOn(self, root):
        self.createf()
        self.firstframe.grid_forget()
        self.item_frame(root)
    
    def createf(self):
        print(self.fname.get())
        print(self.date.get())
        self.arr = self.date.get().split()
        print(self.arr)
        self.f = self.fname.get() + "_" + self.arr[0] + "." + self.arr[1] + "." + self.arr[2] + ".txt"

    def addEntry(self):
        self.outputfile = open(self.f, 'a')
        cat = self.catbox.get(self.catbox.curselection())
        price = self.priceentry.get()
        peoplein = ""
        if self.yardenIn.get() == 1:
            peoplein += "y"
        if self.caseyIn.get() == 1:
            peoplein += "c"
        if self.nateIn.get() == 1:
            peoplein += "n"
        if self.loliIn.get() == 1:
            peoplein += "l"
        if self.otherIn.get() == 1:
            peoplein += "o"
        output = self.arr[0] + ' ' + self.arr[1] + ' ' + self.arr[2] + ' ' + cat + ' ' + price + ' ' + peoplein + '\n'
        self.outputfile.write(output)
        self.outputfile.close()
    
    def nextFunc(self, root):
        self.addEntry()
        self.itemframe.grid_forget()
        self.item_frame(root)

    def doneFunc(self, root):
        self.addEntry()
        self.outputfile.close()
        self.itemframe.grid_forget()
        self.pricelist()
        self.price_frame(root)

    def pricelist(self):
        file=open(self.f)
        listnumbers=[]
        listnames=[]
        counter=0
        for i in file:
            arr=i.split()
            listnumbers.append(float(arr[4]))
            listnames.append(arr[5])
            arr.clear
        numsharing=0
        for i in listnumbers:
            numsharing=len(listnames[counter])
            listnumbers[counter]=i/numsharing
            counter=counter+1
        caseytotal=[]
        yardentotal=[]
        lolitotal=[]
        natetotal=[]
        othertotal=[]
        counter=0
        for i in listnames:
            string1= i
            if string1.find('c')!=-1:
                caseytotal.append(listnumbers[counter])
            if string1.find('y')!=-1:
                yardentotal.append(listnumbers[counter])
            if string1.find('l')!=-1:
                lolitotal.append(listnumbers[counter])
            if string1.find('n')!=-1:
                natetotal.append(listnumbers[counter])
            if string1.find('o')!=-1:
                othertotal.append(listnumbers[counter])
            counter += 1
        self.caseyfinal=0
        self.yardenfinal=0
        self.lolifinal=0
        self.natefinal=0
        self.otherfinal=0
        for i in caseytotal:
            self.caseyfinal+=i
        for i in yardentotal:
            self.yardenfinal+=i
        for i in lolitotal:
            self.lolifinal+=i
        for i in natetotal:
            self.natefinal+=i
        for i in othertotal:
            self.otherfinal+=i
        self.totalbill = self.caseyfinal + self.lolifinal + self.natefinal + self.yardenfinal + self.otherfinal
        print('you paid $'+str(self.caseyfinal))
        print('yarden owes $'+str(self.yardenfinal))
        print('loli owes $'+str(self.lolifinal))
        print('nate owes $'+str(self.natefinal))
        print('other owes $'+str(self.otherfinal))
        print('total bill is $'+str(self.totalbill))
        file.close()
        

#draw tkinter window
top = Tk()
app = Frames()
app.first_frame(top)
#loop
top.mainloop()

