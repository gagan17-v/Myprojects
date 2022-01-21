import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3
class airlinewebapp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        container=tk.Frame(self)

        container.pack(side="top",fill="both",expand=True)

        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)

        self.frames={}
        for F in (StartPage,Homepage,flightschedulepage, flightsarrival,crewpage,mypage,):
            frame=F(container,self)

            self.frames[F]=frame

            frame.grid(row=0,column=0,sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame=self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent,bg='#1a1a1a')
        self.controller=controller
        self.controller.title('gaganairline')
        self.controller.state('zoomed')
        mylabel1=tk.Label(self,text='Airline management',font=('bahnschrift',45),foreground='white',background='#1a1a1a')
        mylabel1.pack(pady=25)
        button = tk.Button(self, text="Lets get in-->",
                            command=lambda: controller.show_frame(Homepage))
        button.pack()
        


class Homepage(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent,bg='#1a1a1a')
        self.contoller=controller
        label1=tk.Label(self,text='Home',font=('bahnschrift',40),fg='#ffffff',bg='#1a1a1a')
        label1.pack(pady=25)
        b_frame=tk.Frame(self,bg='#1a1a1a')
        b_frame.pack(fill='both',expand=True)
        fs_btn=tk.Button(b_frame,text="Add Flight Coordinators",font=('bahnschrift',15),bg='#1a1a1a',fg='white',command=lambda: controller.show_frame(flightschedulepage),relief='raised',borderwidth=2,width=50,height=5)
        fs_btn.grid(row=0,column=0)
        fa_btn=tk.Button(b_frame,text="Flight Schedules ",font=('bahnschrift',15),bg='#1a1a1a',fg='white',command=lambda: controller.show_frame(flightsarrival),relief='raised',borderwidth=2,width=50,height=5)
        fa_btn.grid(row=1,column=0)
        cr_btn=tk.Button(b_frame,text="Flight Arrival",font=('bahnschrift',15),bg='#1a1a1a',fg='white',command=lambda: controller.show_frame(crewpage),relief='raised',borderwidth=2,width=50,height=5)
        cr_btn.grid(row=2,column=0)
        cr1_btn=tk.Button(b_frame,text="Crew details",font=('bahnschrift',15),bg='#1a1a1a',fg='white',command=lambda: controller.show_frame(mypage),relief='raised',borderwidth=2,width=50,height=5)
        cr1_btn.grid(row=3,column=0)
        cr2_btn=tk.Button(b_frame,text="Flight Departure",font=('bahnschrift',15),bg='#1a1a1a',fg='white',command=lambda: controller.show_frame(mypage),relief='raised',borderwidth=2,width=50,height=5)
        cr2_btn.grid(row=4,column=0)
        
        
        

class flightschedulepage(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent,bg='#000000')
        label2=tk.Label(self,text='Flight Coordinator Details',font=('bahnschrift',40),fg='#ffffff',bg='#000000')
        label2.pack()
        LeftFrame=tk.Frame(self,bd=0,relief='ridge',bg="#000000")
        LeftFrame.place(x=100,y=100,width=470,height=400)
        RightFrame=tk.Frame(self,bd=1,relief='ridge',bg="white")
        RightFrame.place(x=700,y=100,width=560,height=370)
        BottomFrame=tk.Frame(self,bd=0,relief='ridge',bg="#000000")
        BottomFrame.place(x=200,y=550,width=150,height=50)
        BottomFrame1=tk.Frame(self,bd=0,relief='ridge',bg="#000000")
        BottomFrame1.place(x=400,y=550,width=150,height=50)
        BottomFrame2=tk.Frame(self,bd=0,relief='ridge',bg="#000000")
        BottomFrame2.place(x=600,y=550,width=150,height=50)
        BottomFrame3=tk.Frame(self,bd=0,relief='ridge',bg="#000000")
        BottomFrame3.place(x=800,y=550,width=150,height=50)
        BottomFrame4=tk.Frame(self,bd=0,relief='ridge',bg="#000000")
        BottomFrame4.place(x=1000,y=550,width=150,height=50)
        BottomFrame5=tk.Frame(self,bd=0,relief='ridge',bg="#000000")
        BottomFrame5.place(x=600,y=650,width=150,height=50)
        
        #main_la=tk.Label(LeftFrame,font=('bahnschrift',20),text='Flight Schedule Details')
        #main_la.grid()
        co_no =tk.Label(LeftFrame, font=('bahnschrift',15),text="Coordinator id:",fg='white',bg='#000000')
        co_no.grid(row=1,column=0)
        co_no_en =tk.Entry(LeftFrame, font=('bahnschrift',15),width =15)
        co_no_en.grid(row=1,column=1,padx=6,pady=20)
        co_fna=tk.Label(LeftFrame, font=('bahnschrift',15),text="First Name:",fg="white",bg="#000000",padx=1)
        co_fna.grid(row=3,column=0)
        co_fna_en=tk.Entry(LeftFrame, font=('bahnschrift',15),width=15)
        co_fna_en.grid(row=3,column=1,pady=6, padx=20)
        co_lna=tk.Label(LeftFrame,font=('bahnnschrift',15),text="Last Name:",fg='white',bg='#000000',padx=1)
        co_lna.grid(row=5,column=0)
        co_lna_en=tk.Entry(LeftFrame, font=('bahnschrift',15),width=15)
        co_lna_en.grid(row=5,column=1,pady=6, padx=20)
        co_cno=tk.Label(LeftFrame,font=('bahnnschrift',15),text="Age:",fg='white',bg='#000000',padx=1)
        co_cno.grid(row=7,column=0)
        co_cno_en=tk.Entry(LeftFrame, font=('bahnschrift',15),width=15)
        co_cno_en.grid(row=7,column=1,pady=6, padx=20)
        co_age=tk.Label(LeftFrame,font=('bahnnschrift',15),text="Contact No:",fg='white',bg='#000000',padx=1)
        co_age.grid(row=9,column=0)
        co_age_en=tk.Entry(LeftFrame, font=('bahnschrift',15),width=15)
        co_age_en.grid(row=9,column=1,pady=6, padx=20)
        co_email=tk.Label(LeftFrame,font=('bahnnschrift',15),text="Email id:",fg='white',bg='#000000',padx=1)
        co_email.grid(row=12,column=0)
        co_email_en=tk.Entry(LeftFrame, font=('bahnschrift',15),width=15)
        co_email_en.grid(row=12,column=1,pady=6, padx=20)
        
        def submit():
            conn=sqlite3.connect('b.db')
            c=conn.cursor()
            c.execute("INSERT INTO FLIGHT_CO VALUES(:f_no,:f_na,:f_da,:f_so,:f_de,:f_ti)",
                      {
                             'f_no':co_no_en.get(),
                             'f_na':co_fna_en.get(),
                             'f_da':co_lna_en.get(),
                             'f_so':co_age_en.get(),
                             'f_de':co_cno_en.get(),
                             'f_ti':co_email_en.get()

                             })
            conn.commit()
            conn.close()
        s_btn=tk.Button(BottomFrame,font=('bahnschrift',22),text='Submit',command=submit,fg='#000000',bg='white',padx=2)
        s_btn.grid(row=2,column=1)
        
        
        
            
            
    
        fli_id=tk.Label(LeftFrame,font=('bahnschrift',15),text='Enter the Flight No to delete:',fg='white',bg='#000000',padx=1)
        fli_id.grid(row=13,column=0)
        fli_id_en=tk.Entry(LeftFrame,font=('bahnschrift',15),width=15)
        fli_id_en.grid(row=13,column=1,pady=6, padx=20)
        fs_btn=tk.Button(BottomFrame5,text="Home",font=('bahnschrift',22),command=lambda: controller.show_frame(Homepage),fg="#000000",bg='white',padx=1)
        fs_btn.grid(row=0,column=2)
        
        
        
        
        def delete():
            
           
            
            conn=sqlite3.connect('b.db')
            c=conn.cursor()
            c.execute("DELETE from FLIGHT_CO WHERE CO_ID="+ fli_id_en.get())
            
            
            
            
                      
            
            conn.commit()
            conn.close()
        
        
        delet_btn=tk.Button(BottomFrame1,font=('bahnschrift',22),text='Delete',command=delete,fg='#000000',bg='white',padx=2)
        delet_btn.grid(row=0,column=5)
        
        def viewData():
            con = sqlite3.connect("b.db")
            cur = con.cursor()
            cur.execute("SELECT * FROM FLIGHT_CO")
            row =cur.fetchall()
            airlinelist.delete(*airlinelist.get_children())
            if len(row)!=0:
                        for num in row:
                            
                            airlinelist.insert('','end',value=num)
            
            
        
        def selected(event):
            viewinfo=airlinelist.focus()
            mysl=airlinelist.item(viewinfo)
            r=mysl['values']
            
            
            co_no_en.insert(0,r[0])
           
          
            co_fna_en.insert(1,r[1])
           
            co_lna_en.insert(2,r[2])
            co_cno_en.insert(3,r[3])
            
            
            co_age_en.insert(4,r[4])
           
            co_email_en.insert(5,r[5])
             
             
            
        scrollbar= tk.Scrollbar(RightFrame)
        scrollbar.grid(row=0, column=1,sticky='ns')
        


        airlinelist= ttk.Treeview(RightFrame, height=16,column=("coid","cofna","colna","cocono","coag","coemail"), yscrollcommand=scrollbar.set )
        airlinelist.heading("coid",text="Coordinator Id")
        airlinelist.heading("cofna",text="First Name")
        airlinelist.heading("colna",text="Last Name")
        airlinelist.heading("cocono",text="Age")
        airlinelist.heading("coag",text="Contact No")
        airlinelist.heading("coemail",text="Email")

        airlinelist['show']='headings'

        airlinelist.column("coid",width=90)
        airlinelist.column("cofna",width=90)
        airlinelist.column("colna",width=90)
        airlinelist.column("cocono",width=90)
        airlinelist.column("coag",width=90)
        airlinelist.column("coemail",width=90)

        airlinelist.bind('<ButtonRelease>',selected)

        airlinelist.grid(row=0,column=0,sticky='ns')

        
        

        d_btn=tk.Button(BottomFrame2,font=('bahnschrift',22),text='Display',command=viewData,fg='#000000',bg='white',padx=2)
        d_btn.grid(row=11,column=0)
        def searchDatabase():
            airlinelist.delete(*airlinelist.get_children())
            for row in searchData(co_no_en.get(),co_fna_en.get(),co_lna_en.get(),co_cno_en.get(),co_age_en.get(),co_email_en.get()):
                airlinelist.insert('','end',value=row)
        def searchData(CO_ID="",CO_FNAME="",CO_LNAME="",CO_AGE="",CO_CONTNO="",CO_EMAIL=""):
            con=sqlite3.connect("b.db")
            cur = con.cursor()
            cur.execute("SELECT * FROM FLIGHT_CO WHERE CO_ID=? OR CO_FNAME=? OR CO_LNAME=? OR CO_CONTNO=? OR CO_AGE=? OR CO_EMAIL=? ", \
                (CO_ID,CO_FNAME,CO_LNAME,CO_AGE,CO_CONTNO,CO_EMAIL))
            rows=cur.fetchall()  
            con.close()
            return rows
        d_btn1=tk.Button(BottomFrame4,font=('bahnschrift',22),text='Search',command=searchDatabase,fg='#000000',bg='white',padx=1)
        d_btn1.grid(row=15,column=0)
        def update():
            n=co_no_en.get()
            a=co_fna_en.get()
            m=co_lna_en.get()
            e=co_cno_en.get()
            s=co_age_en.get()
            i=co_email_en.get()
            conn=sqlite3.connect('b.db')
            c=conn.cursor()
            c.execute("UPDATE FLIGHT_CO SET CO_FNAME=?, CO_LNAME=?, CO_CONTNO=?, CO_AGE=?, CO_EMAIL=?  WHERE CO_ID=?",(a,m,e,s,i,n))
            conn.commit()
            conn.close()
        

        
            


        u_btn=tk.Button(BottomFrame3,font=('bahnschrift',22),text='Update',command=update,fg='#000000',bg='white',padx=2)
        u_btn.grid(row=16,column=0)
            
class flightsarrival(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent,bg='#000000')
        label2=tk.Label(self,text='Flight Arrival',font=('bahnschrift',40),fg='#ffffff',bg='#000000')
        label2.pack()
        global sd
        
        LeftFrame=tk.Frame(self,bd=1,relief='ridge',bg="#000000")
        LeftFrame.place(x=20,y=100,width=470,height=700)
        RightFrame=tk.Frame(self,bd=1,relief='ridge',bg="white")
        RightFrame.place(x=520,y=100,width=570,height=350)
        main_la=tk.Label(LeftFrame,font=('bahnschrift',20),text='Flight Schedule Details')
        main_la.grid()
        fl_no =tk.Label(LeftFrame, font=('bahnschrift',15),text="Flight No:",fg='white',bg='#000000')
        fl_no.grid(row=1,column=0)
        fl_no_en =tk.Entry(LeftFrame, font=('bahnschrift',15),width =15)
        fl_no_en.grid(row=1,column=1,padx=6,pady=20)
        fl_na=tk.Label(LeftFrame, font=('bahnschrift',15),text="Flight Name:",fg="white",bg="#000000",padx=1)
        fl_na.grid(row=2,column=0)
        fl_na_en=tk.Entry(LeftFrame, font=('bahnschrift',15),width=15)
        fl_na_en.grid(row=2,column=1,pady=6, padx=20)
        fl_type=tk.Label(LeftFrame,font=('bahnnschrift',15),text="Flight Type:",fg='white',bg='#000000',padx=1)
        fl_type.grid(row=3,column=0)
        fl_type_en=tk.Entry(LeftFrame, font=('bahnschrift',15),width=15)
        fl_type_en.grid(row=3,column=1,pady=6, padx=20)
        fl_from=tk.Label(LeftFrame,font=('bahnnschrift',15),text="Flight From:",fg='white',bg='#000000',padx=1)
        fl_from.grid(row=4,column=0)
        fl_from_en=tk.Entry(LeftFrame, font=('bahnschrift',15),width=15)
        fl_from_en.grid(row=4,column=1,pady=6, padx=20)
        fl_de=tk.Label(LeftFrame,font=('bahnnschrift',15),text="Flight Destination:",fg='white',bg='#000000',padx=1)
        fl_de.grid(row=5,column=0)
        fl_de_en=tk.Entry(LeftFrame, font=('bahnschrift',15),width=15)
        fl_de_en.grid(row=5,column=1,pady=6, padx=20)
        fl_ca=tk.Label(LeftFrame,font=('bahnnschrift',15),text="Flight Capacity:",fg='white',bg='#000000',padx=1)
        fl_ca.grid(row=6,column=0)
        fl_ca_en=tk.Entry(LeftFrame, font=('bahnschrift',15),width=15)
        fl_ca_en.grid(row=6,column=1,pady=6, padx=20)
        fl_da=tk.Label(LeftFrame,font=('bahnnschrift',15),text="Flight Date:",fg='white',bg='#000000',padx=1)
        fl_da.grid(row=7,column=0)
        fl_da_en=tk.Entry(LeftFrame, font=('bahnschrift',15),width=15)
        fl_da_en.grid(row=7,column=1,pady=6, padx=20)
        fl_ti=tk.Label(LeftFrame,font=('bahnnschrift',15),text="Flight Time:",fg='white',bg='#000000',padx=1)
        fl_ti.grid(row=8,column=0)
        fl_ti_en=tk.Entry(LeftFrame, font=('bahnschrift',15),width=15)
        fl_ti_en.grid(row=8,column=1,pady=6, padx=20)
        fl_du=tk.Label(LeftFrame,font=('bahnnschrift',15),text="Flight Duration:",fg='white',bg='#000000',padx=1)
        fl_du.grid(row=9,column=0)
        fl_du_en=tk.Entry(LeftFrame, font=('bahnschrift',15),width=15)
        fl_du_en.grid(row=9,column=1,pady=6, padx=20)
        fl_sc=tk.Label(LeftFrame,font=('bahnnschrift',15),text="Scheduled Coordinator ID:",fg='white',bg='#000000',padx=1)
        fl_sc.grid(row=10,column=0)
        fl_sc_en=tk.Entry(LeftFrame, font=('bahnschrift',15),width=15)
        fl_sc_en.grid(row=10,column=1,pady=6, padx=20)
        
        def submit():
            conn=sqlite3.connect('a.db')
            c=conn.cursor()
            c.execute("INSERT INTO FLIGHT_SCHED VALUES(:f_no,:f_na,:f_da,:f_so,:f_de,:f_ti,:u,:g,:s,:p)",
                      {
                             'f_no':fl_no_en.get(),
                             'f_na':fl_na_en.get(),
                             'f_da':fl_type_en.get(),
                             'f_so':fl_from_en.get(),
                             'f_de':fl_de_en.get(),
                             'f_ti':fl_ca_en.get(),
                             'u':fl_da_en.get(),
                             'g':fl_ti_en.get(),
                             's':fl_du_en.get(),
                             'p':fl_sc_en.get()
                             
                             })
            conn.commit()
            conn.close()
        s_btn=tk.Button(LeftFrame,font=('bahnschrift',15),text='Add Flight Schedules',command=submit,fg='#000000',bg='white',padx=1)
        s_btn.grid(row=11,column=0)
        
        
        
            
            
    
        fli_id=tk.Label(LeftFrame,font=('bahnschrift',15),text='Enter the Flight No to delete:',fg='white',bg='#000000',padx=1)
        fli_id.grid(row=12,column=0)
        fli_id_en=tk.Entry(LeftFrame,font=('bahnschrift',15),width=15)
        fli_id_en.grid(row=12,column=1,pady=6, padx=20)
        fs_btn=tk.Button(LeftFrame,text="Home",font=('bahnschrift',15),command=lambda: controller.show_frame(Homepage),fg="white",bg='#000000',padx=1)
        fs_btn.grid(row=13,column=1)
        
        
        
        
        
        
        
        
        
        def displayData():
            airlinelist.delete(0, 'end')
            airlinelist.insert('end', "{:<5s}  ".format("Name"))
            for i in viewData():
                    airlinelist.insert('end',i,str("      "))
        def viewData():
            con = sqlite3.connect("a.db")
            cur = con.cursor()
            cur.execute("SELECT * FROM FLIGHT_SCHED")
            row =cur.fetchall()
            con.close()
            return row
        
        def selected(event):
            #global sd
            searchStd=airlinelist.curselection()[0]
            sd=airlinelist.get(searchStd)
            fl_no_en.delete(0,'end')
            fl_no_en.insert('end',sd[0])
            fl_na_en.delete(0,'end')
            fl_na_en.insert('end',sd[1])
            fl_type_en.delete(0,'end')
            fl_type_en.insert('end',sd[2])
            fl_from_en.delete(0,'end')
            fl_from_en.insert('end',sd[3])
            fl_de_en.delete(0,'end')
            fl_de_en.insert('end',sd[4])
            fl_ca_en.delete(0,'end')
            fl_ca_en.insert('end',sd[5])
            fl_da_en.delete(0,'end')
            fl_da_en.insert('end',sd[6])
            fl_ti_en.delete(0,'end')
            fl_ti_en.insert('end',sd[7])
            fl_du_en.delete(0,'end')
            fl_du_en.insert('end',sd[8])
            fl_sc_en.delete(0,'end')
            fl_sc_en.insert('end',sd[9])
            
             
             
            
        scrollbar= tk.Scrollbar(RightFrame)
        scrollbar.grid(row=0, column=1,sticky='ns')
        


        airlinelist= tk.Listbox(RightFrame, width=60, height=16, font=('bahnschrift', 12, 'bold'), yscrollcommand=scrollbar.set )
        airlinelist.bind('<<ListboxSelect>>',selected)
        airlinelist.grid(row=0, column=0,sticky='ns')
        scrollbar.config(command = airlinelist.yview)

        d_btn=tk.Button(LeftFrame,font=('bahnschrift',15),text='Display',command=displayData,fg='#000000',bg='white',padx=1)
        d_btn.grid(row=11,column=0)
        
                

        def deleteRec():
                con=sqlite3.connect("a.db")
                cur = con.cursor()
                cur.execute("DELETE FROM FLIGHT_SCHED WHERE FL_NO="+ fli_id_en.get())
                con.commit()
                con.close
        
        
        delet_btn=tk.Button(LeftFrame,font=('bahnschrift',15),text='Delete',command=deleteRec,fg='#000000',bg='white',padx=1)
        delet_btn.grid(row=13,column=0)
        def searchDatabase():
            airlinelist.delete(0,'end')
            for row in searchData(fl_no_en.get(),fl_na_en.get(),fl_type_en.get(),fl_from_en.get(),fl_de_en.get(),fl_ca_en.get(),fl_da_en.get(),fl_ti_en.get(),fl_du_en.get(),fl_sc_en.get()):
                airlinelist.insert('end',row,str(" "))
        def searchData(FL_NO="",FL_NAME="",FLI_TYPE="",FLI_FROM="",FLI_TO="",FLI_CAPACITY="",FLI_DATE="",FLI_TIME="",FLI_DUR="",SCHED_CO=""):
            con=sqlite3.connect("a.db")
            cur = con.cursor()
            cur.execute("SELECT * FROM FLIGHT_SCHED WHERE FL_NO=? OR FL_NAME=? OR FLI_TYPE=? OR FLI_FROM=? OR FLI_TO=? OR FLI_CAPACITY=? OR FLI_DATE=? OR FLI_TIME=? OR FLI_DUR=? OR SCHED_CO=?", \
                        (FL_NO,FL_NAME,FLI_TYPE,FLI_FROM,FLI_TO,FLI_CAPACITY,FLI_DATE,FLI_TIME,FLI_DUR,SCHED_CO))
            rows=cur.fetchall()
            
            con.close()
            return rows
        d_btn1=tk.Button(LeftFrame,font=('bahnschrift',15),text='Search',command=searchDatabase,fg='#000000',bg='white',padx=1)
        d_btn1.grid(row=15,column=0)
        #def update():
            #n=fl_no_en.get()
            #a=fl_na_en.get()
            #m=fl_da_en.get()
            #e=fl_so_en.get()
            #s=fl_de_en.get()
            #i=fl_ti_en.get()
            #conn=sqlite3.connect('air.db')
            #c=conn.cursor()
            #c.execute("UPDATE FLIGHT1 SET FLIGHT_NAME=?, FLIGHT_SO=?, FLIGHT_DE=?, FLIGHT_TIM=?, FLIGHT_MI=?  WHERE FLIGHT_NO=?",(a,m,e,s,i,n))
            #conn.commit()
            #conn.close()
        

        
            


        #u_btn=tk.Button(LeftFrame,font=('bahnschrift',15),text='Update',command=update,fg='#000000',bg='white',padx=1)
        #u_btn.grid(row=16,column=0)
class crewpage(tk.Frame):
    

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent,bg='#000000')
        self.contoller=controller
        label2=tk.Label(self,text='Flight Arrival Details',font=('bahnschrift',40),fg='#ffffff',bg='#000000')
        label2.pack()
        LeftFrame=tk.Frame(self,bd=0,relief='ridge',bg="#000000")
        LeftFrame.place(x=100,y=100,width=470,height=400)
        RightFrame=tk.Frame(self,bd=1,relief='ridge',bg="white")
        RightFrame.place(x=700,y=100,width=560,height=370)
        BottomFrame=tk.Frame(self,bd=0,relief='ridge',bg="#000000")
        BottomFrame.place(x=200,y=550,width=150,height=50)
        BottomFrame1=tk.Frame(self,bd=0,relief='ridge',bg="#000000")
        BottomFrame1.place(x=400,y=550,width=150,height=50)
        BottomFrame2=tk.Frame(self,bd=0,relief='ridge',bg="#000000")
        BottomFrame2.place(x=600,y=550,width=150,height=50)
        BottomFrame3=tk.Frame(self,bd=0,relief='ridge',bg="#000000")
        BottomFrame3.place(x=800,y=550,width=150,height=50)
        BottomFrame4=tk.Frame(self,bd=0,relief='ridge',bg="#000000")
        BottomFrame4.place(x=1000,y=550,width=150,height=50)
        BottomFrame5=tk.Frame(self,bd=0,relief='ridge',bg="#000000")
        BottomFrame5.place(x=600,y=650,width=150,height=50)
        

        fl_no =tk.Label(LeftFrame, font=('bahnschrift',15),text="Flight No:",fg='white',bg='#000000')
        fl_no.grid(row=1,column=0)
        fl_no_en =tk.Entry(LeftFrame, font=('bahnschrift',15),width =15)
        fl_no_en.grid(row=1,column=1,padx=6,pady=20)
        fl_na=tk.Label(LeftFrame, font=('bahnschrift',15),text="Flight Name:",fg="white",bg="#000000",padx=1)
        fl_na.grid(row=3,column=0)
        fl_na_en=tk.Entry(LeftFrame, font=('bahnschrift',15),width=15)
        fl_na_en.grid(row=3,column=1,pady=6, padx=20)
        fl_type=tk.Label(LeftFrame,font=('bahnnschrift',15),text="Flight Type:",fg='white',bg='#000000',padx=1)
        fl_type.grid(row=5,column=0)
        fl_type_en=tk.Entry(LeftFrame, font=('bahnschrift',15),width=15)
        fl_type_en.grid(row=5,column=1,pady=6, padx=20)
        fl_from=tk.Label(LeftFrame,font=('bahnnschrift',15),text="Flight From:",fg='white',bg='#000000',padx=1)
        fl_from.grid(row=7,column=0)
        fl_from_en=tk.Entry(LeftFrame, font=('bahnschrift',15),width=15)
        fl_from_en.grid(row=7,column=1,pady=6, padx=20)
        fl_atime=tk.Label(LeftFrame,font=('bahnnschrift',15),text="Flight Arrived Time:",fg='white',bg='#000000',padx=1)
        fl_atime.grid(row=9,column=0)
        fl_atime_en=tk.Entry(LeftFrame, font=('bahnschrift',15),width=15)
        fl_atime_en.grid(row=9,column=1,pady=6, padx=20)
        r_coid=tk.Label(LeftFrame,font=('bahnnschrift',15),text="Reported Co ID:",fg='white',bg='#000000',padx=1)
        r_coid.grid(row=12,column=0)
        r_coid_en=tk.Entry(LeftFrame, font=('bahnschrift',15),width=15)
        r_coid_en.grid(row=12,column=1,pady=6, padx=20)
        def submit():
            conn=sqlite3.connect('b.db')
            c=conn.cursor()
            c.execute("INSERT INTO FLIGHTAR VALUES(:f_no,:f_na,:f_da,:f_so,:f_de,:f_ti)",
                      {
                             'f_no':fl_no_en.get(),
                             'f_na':fl_na_en.get(),
                             'f_da':fl_type_en.get(),
                             'f_so':fl_from_en.get(),
                             'f_de':fl_atime_en.get(),
                             'f_ti':r_coid_en.get()

                             })
            conn.commit()
            conn.close()
        s_btn=tk.Button(BottomFrame,font=('bahnschrift',22),text='Submit',command=submit,fg='#000000',bg='white',padx=2)
        s_btn.grid(row=2,column=1)
        
        
        
            
            
    
        fli_id=tk.Label(LeftFrame,font=('bahnschrift',15),text='Enter the Flight No to delete:',fg='white',bg='#000000',padx=1)
        fli_id.grid(row=13,column=0)
        fli_id_en=tk.Entry(LeftFrame,font=('bahnschrift',15),width=15)
        fli_id_en.grid(row=13,column=1,pady=6, padx=20)
        fs_btn=tk.Button(BottomFrame5,text="Home",font=('bahnschrift',22),command=lambda: controller.show_frame(Homepage),fg="#000000",bg='white',padx=1)
        fs_btn.grid(row=0,column=2)
        
        
        
        
        def delete():
            
           
            
            conn=sqlite3.connect('b.db')
            c=conn.cursor()
            c.execute("DELETE from FLIGHTAR WHERE FLI_NO="+ fli_id_en.get())
            
            
            
            
                      
            
            conn.commit()
            conn.close()
        
        
        delet_btn=tk.Button(BottomFrame1,font=('bahnschrift',22),text='Delete',command=delete,fg='#000000',bg='white',padx=2)
        delet_btn.grid(row=0,column=5)
        
        def viewData():
            con = sqlite3.connect("b.db")
            cur = con.cursor()
            cur.execute("SELECT * FROM FLIGHTAR")
            row =cur.fetchall()
            airlinelist.delete(*airlinelist.get_children())
            if len(row)!=0:
                        for num in row:
                            
                            airlinelist.insert('','end',value=num)
            
            
        
        def selected(event):
            viewinfo=airlinelist.focus()
            mysl=airlinelist.item(viewinfo)
            r=mysl['values']
            
            
            fl_no_en.insert(0,r[0])
           
          
            fl_na_en.insert(1,r[1])
           
            fl_type_en.insert(2,r[2])
            fl_from_en.insert(3,r[3])
            
            
            fl_atime_en.insert(4,r[4])
           
            r_coid_en.insert(5,r[5])
             
             
            
        scrollbar= tk.Scrollbar(RightFrame)
        scrollbar.grid(row=0, column=1,sticky='ns')
        


        airlinelist= ttk.Treeview(RightFrame, height=16,column=("coid","cofna","colna","cocono","coag","coemail"), yscrollcommand=scrollbar.set )
        airlinelist.heading("coid",text="Flight No")
        airlinelist.heading("cofna",text="Flight Name")
        airlinelist.heading("colna",text="Flight Type")
        airlinelist.heading("cocono",text="Flight From")
        airlinelist.heading("coag",text="Flight Arr Time")
        airlinelist.heading("coemail",text="Reported Co id")

        airlinelist['show']='headings'

        airlinelist.column("coid",width=90)
        airlinelist.column("cofna",width=90)
        airlinelist.column("colna",width=90)
        airlinelist.column("cocono",width=90)
        airlinelist.column("coag",width=90)
        airlinelist.column("coemail",width=90)

        airlinelist.bind('<ButtonRelease>',selected)

        airlinelist.grid(row=0,column=0,sticky='ns')

        
        

        d_btn=tk.Button(BottomFrame2,font=('bahnschrift',22),text='Display',command=viewData,fg='#000000',bg='white',padx=2)
        d_btn.grid(row=11,column=0)
        def searchDatabase():
            airlinelist.delete(*airlinelist.get_children())
            for row in searchData(fl_no_en.get(),fl_na_en.get(),fl_type_en.get(),fl_from_en.get(),fl_atime_en.get(),r_coid_en.get()):
                airlinelist.insert('','end',value=row)
        def searchData(FLI_NO="",FLI_NAME="",FLI_TYPE="",FLI_FROM="",FLI_A_TIME="",REPORTED_CO_ID=""):
            con=sqlite3.connect("b.db")
            cur = con.cursor()
            cur.execute("SELECT * FROM FLIGHTAR WHERE FLI_NO=? OR FLI_NAME=? OR FLI_TYPE=? OR FLI_FROM=? OR FLI_A_TIME=? OR REPORTED_CO_ID= ?", \
                (FLI_NO,FLI_NAME,FLI_TYPE,FLI_FROM,FLI_A_TIME,REPORTED_CO_ID))
            rows=cur.fetchall()  
            con.close()
            return rows
        d_btn1=tk.Button(BottomFrame4,font=('bahnschrift',22),text='Search',command=searchDatabase,fg='#000000',bg='white',padx=1)
        d_btn1.grid(row=15,column=0)
        def update():
            n=fl_no_en.get()
            a=fl_na_en.get()
            m=fl_type_en.get()
            e=fl_from_en.get()
            s=fl_atime_en.get()
            i=r_coid_en.get()
            conn=sqlite3.connect('b.db')
            c=conn.cursor()
            c.execute("UPDATE   FLIGHTAR SET FLI_NAME=?, FLI_TYPE=?, FLI_FROM=?, FLI_A_TIME=?, REPORTED_CO_ID=?  WHERE FLI_NO=?",(a,m,e,s,i,n))
            conn.commit()
            conn.close()
        

        
            


        u_btn=tk.Button(BottomFrame3,font=('bahnschrift',22),text='Update',command=update,fg='#000000',bg='white',padx=2)
        u_btn.grid(row=16,column=0)
class mypage(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent,bg='#000000')
        label2=tk.Label(self,text='Flight Coordinator Details',font=('bahnschrift',40),fg='#ffffff',bg='#000000')
        label2.pack()
        LeftFrame=tk.Frame(self,bd=0,relief='ridge',bg="#000000")
        LeftFrame.place(x=100,y=100,width=470,height=400)
        RightFrame=tk.Frame(self,bd=1,relief='ridge',bg="white")
        RightFrame.place(x=700,y=100,width=560,height=370)
        BottomFrame=tk.Frame(self,bd=0,relief='ridge',bg="#000000")
        BottomFrame.place(x=200,y=550,width=150,height=50)
        BottomFrame1=tk.Frame(self,bd=0,relief='ridge',bg="#000000")
        BottomFrame1.place(x=400,y=550,width=150,height=50)
        BottomFrame2=tk.Frame(self,bd=0,relief='ridge',bg="#000000")
        BottomFrame2.place(x=600,y=550,width=150,height=50)
        BottomFrame3=tk.Frame(self,bd=0,relief='ridge',bg="#000000")
        BottomFrame3.place(x=800,y=550,width=150,height=50)
        BottomFrame4=tk.Frame(self,bd=0,relief='ridge',bg="#000000")
        BottomFrame4.place(x=1000,y=550,width=150,height=50)
        BottomFrame5=tk.Frame(self,bd=0,relief='ridge',bg="#000000")
        BottomFrame5.place(x=600,y=650,width=150,height=50)
        
        #main_la=tk.Label(LeftFrame,font=('bahnschrift',20),text='Flight Schedule Details')
        #main_la.grid()
        co_no =tk.Label(LeftFrame, font=('bahnschrift',15),text="Crew No:",fg='white',bg='#000000')
        co_no.grid(row=1,column=0)
        co_no_en =tk.Entry(LeftFrame, font=('bahnschrift',15),width =15)
        co_no_en.grid(row=1,column=1,padx=6,pady=20)
        co_fna=tk.Label(LeftFrame, font=('bahnschrift',15),text="Crew Name:",fg="white",bg="#000000",padx=1)
        co_fna.grid(row=3,column=0)
        co_fna_en=tk.Entry(LeftFrame, font=('bahnschrift',15),width=15)
        co_fna_en.grid(row=3,column=1,pady=6, padx=20)
        co_lna=tk.Label(LeftFrame,font=('bahnnschrift',15),text="Crew Age:",fg='white',bg='#000000',padx=1)
        co_lna.grid(row=5,column=0)
        co_lna_en=tk.Entry(LeftFrame, font=('bahnschrift',15),width=15)
        co_lna_en.grid(row=5,column=1,pady=6, padx=20)
        co_cno=tk.Label(LeftFrame,font=('bahnnschrift',15),text="Job Role:",fg='white',bg='#000000',padx=1)
        co_cno.grid(row=7,column=0)
        co_cno_en=tk.Entry(LeftFrame, font=('bahnschrift',15),width=15)
        co_cno_en.grid(row=7,column=1,pady=6, padx=20)
        co_age=tk.Label(LeftFrame,font=('bahnnschrift',15),text="Contact No:",fg='white',bg='#000000',padx=1)
        co_age.grid(row=9,column=0)
        co_age_en=tk.Entry(LeftFrame, font=('bahnschrift',15),width=15)
        co_age_en.grid(row=9,column=1,pady=6, padx=20)
        co_email=tk.Label(LeftFrame,font=('bahnnschrift',15),text="Assigned by:",fg='white',bg='#000000',padx=1)
        co_email.grid(row=12,column=0)
        co_email_en=tk.Entry(LeftFrame, font=('bahnschrift',15),width=15)
        co_email_en.grid(row=12,column=1,pady=6, padx=20)
        
        def submit():
            conn=sqlite3.connect('b.db')
            c=conn.cursor()
            c.execute("INSERT INTO CREW VALUES(:f_no,:f_na,:f_da,:f_so,:f_de,:f_ti)",
                      {
                             'f_no':co_no_en.get(),
                             'f_na':co_fna_en.get(),
                             'f_da':co_lna_en.get(),
                             'f_so':co_age_en.get(),
                             'f_de':co_cno_en.get(),
                             'f_ti':co_email_en.get()

                             })
            conn.commit()
            conn.close()
        s_btn=tk.Button(BottomFrame,font=('bahnschrift',22),text='Submit',command=submit,fg='#000000',bg='white',padx=2)
        s_btn.grid(row=2,column=1)
        
        
        
            
            
    
        fli_id=tk.Label(LeftFrame,font=('bahnschrift',15),text='Enter the Crew No to delete:',fg='white',bg='#000000',padx=1)
        fli_id.grid(row=13,column=0)
        fli_id_en=tk.Entry(LeftFrame,font=('bahnschrift',15),width=15)
        fli_id_en.grid(row=13,column=1,pady=6, padx=20)
        fs_btn=tk.Button(BottomFrame5,text="Home",font=('bahnschrift',22),command=lambda: controller.show_frame(Homepage),fg="#000000",bg='white',padx=1)
        fs_btn.grid(row=0,column=2)
        
        
        
        
        def delete():
            
           
            
            conn=sqlite3.connect('b.db')
            c=conn.cursor()
            c.execute("DELETE from CREW WHERE CREW_ID="+ fli_id_en.get())
            
            
            
            
                      
            
            conn.commit()
            conn.close()
        
        
        delet_btn=tk.Button(BottomFrame1,font=('bahnschrift',22),text='Delete',command=delete,fg='#000000',bg='white',padx=2)
        delet_btn.grid(row=0,column=5)
        
        def viewData():
            con = sqlite3.connect("b.db")
            cur = con.cursor()
            cur.execute("SELECT * FROM CREW")
            row =cur.fetchall()
            airlinelist.delete(*airlinelist.get_children())
            if len(row)!=0:
                        for num in row:
                            
                            airlinelist.insert('','end',value=num)
            
            
        
        def selected(event):
            viewinfo=airlinelist.focus()
            mysl=airlinelist.item(viewinfo)
            r=mysl['values']
            
            
            co_no_en.insert(0,r[0])
           
          
            co_fna_en.insert(1,r[1])
           
            co_lna_en.insert(2,r[2])
            co_cno_en.insert(3,r[3])
            
            
            co_age_en.insert(4,r[4])
           
            co_email_en.insert(5,r[5])
             
             
            
        scrollbar= tk.Scrollbar(RightFrame)
        scrollbar.grid(row=0, column=1,sticky='ns')
        


        airlinelist= ttk.Treeview(RightFrame, height=16,column=("coid","cofna","colna","cocono","coag","coemail"), yscrollcommand=scrollbar.set )
        airlinelist.heading("coid",text="Coordinator Id")
        airlinelist.heading("cofna",text="First Name")
        airlinelist.heading("colna",text="Last Name")
        airlinelist.heading("cocono",text="Age")
        airlinelist.heading("coag",text="Contact No")
        airlinelist.heading("coemail",text="Email")

        airlinelist['show']='headings'

        airlinelist.column("coid",width=90)
        airlinelist.column("cofna",width=90)
        airlinelist.column("colna",width=90)
        airlinelist.column("cocono",width=90)
        airlinelist.column("coag",width=90)
        airlinelist.column("coemail",width=90)

        airlinelist.bind('<ButtonRelease>',selected)

        airlinelist.grid(row=0,column=0,sticky='ns')

        
        

        d_btn=tk.Button(BottomFrame2,font=('bahnschrift',22),text='Display',command=viewData,fg='#000000',bg='white',padx=2)
        d_btn.grid(row=11,column=0)
        def searchDatabase():
            airlinelist.delete(*airlinelist.get_children())
            for row in searchData(co_no_en.get(),co_fna_en.get(),co_lna_en.get(),co_cno_en.get(),co_age_en.get(),co_email_en.get()):
                airlinelist.insert('','end',value=row)
        def searchData(CO_ID="",CO_FNAME="",CO_LNAME="",CO_AGE="",CO_CONTNO="",CO_EMAIL=""):
            con=sqlite3.connect("b.db")
            cur = con.cursor()
            cur.execute("SELECT * FROM FLIGHT_CO WHERE CO_ID=? OR CO_FNAME=? OR CO_LNAME=? OR CO_CONTNO=? OR CO_AGE=? OR CO_EMAIL=? ", \
                (CO_ID,CO_FNAME,CO_LNAME,CO_AGE,CO_CONTNO,CO_EMAIL))
            rows=cur.fetchall()  
            con.close()
            return rows
        d_btn1=tk.Button(BottomFrame4,font=('bahnschrift',22),text='Search',command=searchDatabase,fg='#000000',bg='white',padx=1)
        d_btn1.grid(row=15,column=0)
        def update():
            n=co_no_en.get()
            a=co_fna_en.get()
            m=co_lna_en.get()
            e=co_cno_en.get()
            s=co_age_en.get()
            i=co_email_en.get()
            conn=sqlite3.connect('b.db')
            c=conn.cursor()
            c.execute("UPDATE FLIGHT_CO SET CO_FNAME=?, CO_LNAME=?, CO_CONTNO=?, CO_AGE=?, CO_EMAIL=?  WHERE CO_ID=?",(a,m,e,s,i,n))
            conn.commit()
            conn.close()
        

        
            


        u_btn=tk.Button(BottomFrame3,font=('bahnschrift',22),text='Update',command=update,fg='#000000',bg='white',padx=2)
        u_btn.grid(row=16,column=0)

app=airlinewebapp()
app.mainloop()
    
