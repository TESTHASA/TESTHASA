from tkinter import *

from tkinter import ttk
import sqlite3
class soso :
    def __init__(self,form):
        self.form = form
        self.form.geometry('1366x682')
        #self.form.resizable(False,False)
        self.form.config(bg='black')
        self.form.title('ثانوية الطيبة المختلطة ')
        # my name is  Programmer Hassan Walid
        hasan_walied = Frame(self.form,bg='#CD6155')
        hasan_walied.place(x=1,y=1,width=1363,height=44)
        my_name = Label(hasan_walied,text='Programmer Hassan Walid',bg='#CD6155',fg='white',font=('monosbace',18))
        my_name.place(x=530,y=5)
        ent_fram = Frame(self.form,bg='white')
        ent_fram.place(x=1066,y=46,width=300,height=664)
        #10101010010101010101010110010100001100
        self.nom = StringVar()
        self.name = StringVar()
        self.email = StringVar()
        self.phone = StringVar()
        self.clas = StringVar()
        self.mstwa = StringVar()
        self.deletr = StringVar()
        nom_0 = Label(ent_fram,text='nom',bg='white',fg='black',font=('monosbace',10))
        nom_0.pack()
        ent_1 = Entry(ent_fram,bd=1,textvariable=self.nom)
        ent_1.pack()
        nom_1 = Label(ent_fram,text='name',bg='white',fg='black',font=('monosbace',10))
        nom_1.pack()
        ent_2 = Entry(ent_fram,bd=1,textvariable=self.name)
        ent_2.pack()
        nom_2 = Label(ent_fram,text='phone',bg='white',fg='black',font=('monosbace',10))
        nom_2.pack()
        ent_3 = Entry(ent_fram,
                      bd=1,
                      



                      textvariable=self.phone)
        ent_3.pack()
        nom_3 =Label(ent_fram,text='email',bg='white',fg='black',font=('monosbace',10))
        nom_3.pack()
        ent_4 = Entry(ent_fram,bd=1,textvariable=self.email)
        ent_4.pack()
        nom_4 = Label(ent_fram,text='class',bg='white',fg='black',font=('monosbace',10))
        nom_4.pack()
        ent_4 = Entry(ent_fram,bd=1,textvariable=self.clas)
        ent_4.pack()
        nom_5 = Label(ent_fram,text='mstwa',bg='white',fg='black',font=('monosbace',10))
        nom_5.pack()
        ent_5 = Entry(ent_fram,bd=2,textvariable=self.mstwa)
        ent_5.pack()
        dele = Label(ent_fram,text='delet data',bg='white',fg='red',font=('monosbace',10))
        dele.pack()
        entry = Entry(ent_fram,bd=1,textvariable=self.deletr)
        entry.pack()
        #10101001010101010
        lap_contro = Frame(ent_fram,bg='#CD6155')
        lap_contro.place(x=1,y=360,width=298,height=30)
        control = Label(lap_contro,text='control panel',bg='#CD6155',fg='white',font=('monosbace',12))
        control.place(x=98,y=2)
        #                 buttons  
        #def ad ():
         #con = sqlite3.connect('layan.db')
         #cur = con.cursor()
         #cur.execute("insert into salam values(%s,%s,%s,%s,%s,%s)",self.nom.get(),
          #                                                          self.name.get(),
           #                                                         self.phone.get(),
            #                                                        self.email.get(),
             #                                                       self.clas.get(),
              #                                                      self.mstwa.get()
          #                                                          )
         #con.commit()
         #con.close()

        add = Button(ent_fram,text='add student',bg='#CD6155',fg='white',command=self.ad)
        add.place(x=88,y=410,width=120,height=40)
        update = Button(ent_fram,text='update data',bg='#CD6155',fg='white',command=self.der)
        update.place(x=88,y=452,width=120,height=40)
        delete = Button(ent_fram,text='delete data',fg='white',bg='#CD6155',command=self.delet)
        delete.place(x=88,y=494,width=120,height=40)
        clse = Button(ent_fram,text='close',bg='#CD6155',fg='white',command=quit)
        clse.place(x=88,y=535,width=120,height=40)
        tree = Frame(self.form,bg='white')
        tree.place(x=3,y=46,width=1058,height=654)
        sco_x= Scrollbar(tree,orient=HORIZONTAL)
        sco_y = Scrollbar(tree,orient=VERTICAL)
        self.tree = ttk.Treeview(tree,
                                 
                                 
                                 
                                           columns=('nom','name','phone','email','class','mstwa'),
                                 xscrollcommand=sco_x.set,






                                 yscrollcommand= sco_y.set)
        self.tree.place(x=20,y=0,width=1050,height=630)
        self.tree.column('nom',width=160)
        self.tree.column('name',width=160)
        self.tree.column('phone',width=160)
        self.tree.column('email',width=160)
        self.tree.column('class',width=160)
        self.tree.column('mstwa',width=160)
        self.tree['show']='headings'
        self.tree.heading('nom',text='nom')
        self.tree.heading('name',text='name')
        self.tree.heading('phone',text='email')
        self.tree.heading('email',text='phone')
        self.tree.heading('class',text='class')
        self.tree.heading('mstwa',text='mstwa')
        #into = (self.nom,self.name,self.email,self.phone,self.clas,self.mstwa)
        self.fi()
    def ad (self):
     con = sqlite3.connect('layan.db')
     cur = con.cursor()
     into = (self.nom.get(),self.name.get(),self.email.get(),self.phone.get(),self.clas.get(),self.mstwa.get())
     
     cur = con.cursor()

     cur.execute('insert into layan values(?,?,?,?,?,?)',into)
                 
     
     #vas = (self.nom,self.name,self.phone,self.email,self.clas,self.mstwa)
     self.fi()
     con.commit()
     
     con.close()
    def fi(self):
       con = sqlite3.connect('layan.db')
       cur = con.cursor()
       cur.execute('select * from layan')
       ros = cur.fetchall()
       if len(ros) !=0:
          self.tree.delete(*self.tree.get_children())
          for rose in ros:
             self.tree.insert("",END,values=rose)



       con.commit()
       con.close() 
    def delet (self):
       con = sqlite3.connect('layan.db')
       der = (self.deletr.get())
       cur = con.cursor()
       cur.execute('delete from layan where nom=?;',[der])
       con.commit()
       self.fi()
       con.close()   
    def der (self):
       self.nom.set("")
       self.name.set("")
       self.email.set("")
       self.phone.set("")
       self.clas.set("")
       self.mstwa.set("")


      








































form = Tk()
od = soso(form)
form.mainloop()
