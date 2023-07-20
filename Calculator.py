from tkinter import *

class calculator:
    def frames_setup(self,window):
        self.number_frame = Frame(window,bg='blue')
        self.number_frame.place(x=30,y=100)
        self.op_frame = Frame(window,bg='red',width=200,height=400)
        self.op_frame.place(x=200,y=100)
        self.qtn = StringVar() 
        self.qtn.set("")
        self.screen = Entry(window,bg='grey',textvariable=self.qtn,width=20,font='Arial 20 bold')
        self.screen.place(x=20,y=40)
        self.numframe()
        self.opframe()

    def numframe(self):
        self.button1= Button(self.number_frame,text='1',font='Arial 15 bold',width=3,height=1,command=lambda: self.click(self.button1))
        self.button1.grid(row=0,column=0)
        self.button2= Button(self.number_frame,text='2',font='Arial 15 bold',width=3,height=1,command=lambda: self.click(self.button2))
        self.button2.grid(row=0,column=1)
        self.button3= Button(self.number_frame,text='3',font='Arial 15 bold',width=3,height=1,command=lambda: self.click(self.button3))
        self.button3.grid(row=0,column=2)
        self.button4= Button(self.number_frame,text='4',font='Arial 15 bold',width=3,height=1,command=lambda: self.click(self.button4))
        self.button4.grid(row=1,column=0)
        self.button5= Button(self.number_frame,text='5',font='Arial 15 bold',width=3,height=1,command=lambda: self.click(self.button5))
        self.button5.grid(row=1,column=1)
        self.button6= Button(self.number_frame,text='6',font='Arial 15 bold',width=3,height=1,command=lambda: self.click(self.button6))
        self.button6.grid(row=1,column=2)
        self.button7= Button(self.number_frame,text='7',font='Arial 15 bold',width=3,height=1,command=lambda: self.click(self.button7))
        self.button7.grid(row=2,column=0)
        self.button8= Button(self.number_frame,text='8',font='Arial 15 bold',width=3,height=1,command=lambda: self.click(self.button8))
        self.button8.grid(row=2,column=1)  
        self.button9= Button(self.number_frame,text='9',font='Arial 15 bold',width=3,height=1,command=lambda: self.click(self.button9))
        self.button9.grid(row=2,column=2)
        self.button0= Button(self.number_frame,text='0',font='Arial 15 bold',width=3,height=1,command=lambda: self.click(self.button0))
        self.button0.grid(row=3,column=0) 
        self.buttondot= Button(self.number_frame,text='.',font='Arial 15 bold',width=3,height=1,command=lambda: self.click(self.buttondot))
        self.buttondot.grid(row=3,column=1)
        self.buttonac= Button(self.number_frame,text='AC',font='Arial 15 bold',width=3,height=1,command=self.acclick)
        self.buttonac.grid(row=3,column=2)

    def opframe(self):
        self.add = Button(self.op_frame,text='+',font='Arial 15 bold',width=4,height=1,command=lambda: self.click(self.add))
        self.add.grid(row=0,column=0)
        self.sub = Button(self.op_frame,text='-',font='Arial 15 bold',width=4,height=1,command=lambda: self.click(self.sub))
        self.sub.grid(row=0,column=1)
        self.mul = Button(self.op_frame,text='*',font='Arial 15 bold',width=4,height=1,command=lambda: self.click(self.mul))
        self.mul.grid(row=1,column=0)
        self.div = Button(self.op_frame,text='/',font='Arial 15 bold',width=4,height=1,command=lambda: self.click(self.div))
        self.div.grid(row=1,column=1)
        self.sign = Button(self.op_frame,text='+/-',font='Arial 15 bold',width=4,height=1,command=self.signclick)
        self.sign.grid(row=2,column=0)
        self.mod = Button(self.op_frame,text='%',font='Arial 15 bold',width=4,height=1,command=lambda: self.click(self.mod))
        self.mod.grid(row=2,column=1)
        self.x2 = Button(self.op_frame,text='x^2',font='Arial 15 bold',width=4,height=1,command=self.sqrclick)
        self.x2.grid(row=3,column=0)
        self.eq = Button(self.op_frame,text='=',font='Arial 15 bold',width=4,height=1,command= self.eqclick)
        self.eq.grid(row=3,column=1)

    def click(self,button):
        self.qtn.set( self.qtn.get() + button['text'])

    def acclick(self):
        self.qtn.set("")   

    def signclick(self):
        temp = int(self.qtn.get())
        self.qtn.set(str(-temp))   

    def sqrclick(self):
        self.qtn.set( int(self.qtn.get()) ** 2)    

    def eqclick(self):
        try:
            self.qtn.set( eval(self.qtn.get()))
        except ZeroDivisionError:
            self.qtn.set('Arithmetic Error')
        except SyntaxError:
            self.qtn.set('Syntax Error')            

def main():
    window = Tk()
    window.title('Navaneethan\'s Calculator')
    c = calculator()
    c.frames_setup(window)
    window.geometry('350x300')
    
    window.mainloop()

if __name__ == '__main__':
    main()