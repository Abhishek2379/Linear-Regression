from tkinter import*
import numpy as np
import matplotlib.pyplot as plot
from statistics import mean






class MyEntry:
    #constructor
    def __init__(self,root):

      
        #create a frame as child to root window
        self.f =Frame(root,height=350,width=500)

        #let the frame will not shrink
        self.f.propagate(0)

        #attach the frame to root window
        self.f.pack()

        #labels
        self.l1=Label(text='Enter the values of X:',font="none 12 bold")

        #create Entry widget for X
        self.e1=Entry(self.f,width=2,fg='blue',bg='cyan',font=('Arial',14))
        self.e2=Entry(self.f,width=2,fg='blue',bg='cyan',font=('Arial',14))
        self.e3=Entry(self.f,width=2,fg='blue',bg='cyan',font=('Arial',14))
        self.e4=Entry(self.f,width=2,fg='blue',bg='cyan',font=('Arial',14))
        self.e5=Entry(self.f,width=2,fg='blue',bg='cyan',font=('Arial',14))
       
        self.e5.bind("<Return>",self.display)

          #place labels and entry widget in the frame

        self.l1.place(x=50,y=50)
        self.e1.place(x=230,y=50)
        self.e2.place(x=260,y=50)
        self.e3.place(x=290,y=50)
        self.e4.place(x=320,y=50)
        self.e5.place(x=350,y=50)
    
        

        #label 2
        self.l2=Label(text='Enter the values of Y:',font="none 12 bold")

        #create Entry widget for Y
        self.a1=Entry(self.f,width=2,fg='blue',bg='cyan',font=('Arial',14))
        self.a2=Entry(self.f,width=2,fg='blue',bg='cyan',font=('Arial',14))
        self.a3=Entry(self.f,width=2,fg='blue',bg='cyan',font=('Arial',14))
        self.a4=Entry(self.f,width=2,fg='blue',bg='cyan',font=('Arial',14))
        self.a5=Entry(self.f,width=2,fg='blue',bg='cyan',font=('Arial',14))
       
        
        #when user presses enter ,bind that event to display method
        self.a5.bind("<Return>",self.display)
        

      

         #place labels and entry widget in the frame

        self.l2.place(x=50,y=80)
        self.a1.place(x=230,y=80)
        self.a2.place(x=260,y=80)
        self.a3.place(x=290,y=80)
        self.a4.place(x=320,y=80)
        self.a5.place(x=350,y=80)
       
        
        
        

        

    def display(self,event):
       
        x_data=[]
        y_data=[]
       
        #++++++++++++++++++++++++++++++++++++++
        # X-values
        str1=int(self.e1.get())
        str2=int(self.e2.get())
        str3=int(self.e3.get())
        str4=int(self.e4.get())
        str5=int(self.e5.get())
       

        #Y- Values
        stra=int(self.a1.get())
        strb=int(self.a2.get())
        strc=int(self.a3.get())
        strd=int(self.a4.get())
        stre=int(self.a5.get())
       
        #++++++++++++++++++++++++++++++++++++++

        
        x_data=[str1,str2,str3,str4,str5]
        print(x_data)

        y_data=[stra,strb,strc,strd,stre]
        print(y_data)

        q1=','.join(map(str,[x_data]) )
        q2=','.join(map(str,[y_data]) )
        lbl1 =Label(text='List 1 is :'+q1).place(x=50,y=120)
        lbl2 =Label(text='List 2 is:'+q2).place(x=50,y=150)
        l=len(x_data)

        print("length is",l)
        m_x=sum(x_data) / int(l)
        xmean='.'.join(map(str,[m_x]))
        lbl3 =Label(text="Mean of X is :"+xmean).place(x=50,y=180)
        l=len(y_data)
        m_y=sum(y_data) / int(l)
        ymean='.'.join(map(str,[m_y]))
        lbl4 =Label(text="mean of Y is :"+ymean).place(x=50,y=200)

        m = []
        c=[]
        for i in range(5):
            print("i=",i)
            b=(x_data[i]-m_x)**2
            a=(x_data[i]-m_x) * (y_data[i]-m_y)
            m.append(a)
            c.append(b)
        print(m)
        x=sum(m)
        print(x)
        y=sum(c)
        print(y)
        
        slope=(x/y)
        print(slope)
  

        print("Inside intercept slope is",slope)
        print("mean of y is",m_y)
        print("mean of x is",m_x)
        y_intercept=m_y-(slope*m_x)

        
        print(slope)
        b=y_intercept
        print(b)

        regression_line=[(slope*x)+b for x in x_data]
        plot.scatter(x_data,y_data)
        plot.plot(x_data,regression_line)
        plot.show()
       
        


  
        
        

                
                          
#create root window
root=Tk()

root.title("Linear Regression")

#create an object  to Mybuttons class
mb=MyEntry(root)

#the root window handles the mouse click event
root.mainloop()

