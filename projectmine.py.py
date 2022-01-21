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
        for F in (StartPage,Homepage,flightschedulepage, flightsarrival,flapage,mypage,lastpage,cancelledpage):
            frame=F(container,self)

            self.frames[F]=frame

            frame.grid(row=0,column=0,sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame=self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller=controller
        self.controller.title('gaganairline')
        self.controller.state('zoomed')
        load = Image.open("20210114_212536.jpg")
        photo=ImageTk.PhotoImage(load)
        label=tk.Label(self,image=photo)
        label.image=photo
        label.place(x=0,y=0)
        
        mylabel1=tk.Label(self,text='Airline management',font=('bahnschrift',45),foreground='white',background='#1a1a1a')
        mylabel1.place(x=500)
        
        
        
        l1 =tk.Label(self, font=('bahnschrift',15),text="Username:",fg='white',bg='#000000')
        l1.place(x=500,y=100)
        t1 =tk.Entry(self, font=('bahnschrift',15),width =15)
        t1.place(x=650,y=100)
        l2=tk.Label(self, font=('bahnschrift',15),text="Password:",fg="white",bg="#000000",padx=1)
        l2.place(x=500,y=200)
        t2=tk.Entry(self, font=('bahnschrift',15),width=15)
        t2.place(x=650,y=200)
        def verify():
            with open("cred.txt", "r") as f:
                info=f.readlines()
               
                for e in info:
                    u,p=e.split(",")
                    if u.strip()== t1.get() and p.strip()==t2.get():
                        controller.show_frame(Homepage)
                        
                        break
            reset()
        def reset():
            t1.delete(0,'end')
            t2.delete(0,'end')
                    
        fs_btn=tk.Button(self,text="Submit",font=('bahnschrift',15),command=verify,fg="#000000",bg='white',padx=1)
        fs_btn.place(x=600,y=300)
        l4 =tk.Label(self, font=('bahnschrift',15),text="New User! Click Register:",fg='white',bg='#000000')
        l4.place(x=500,y=600)
        
        def register():
            window=tk.Tk()
            window.title("Register")
            l1=tk.Label(window,text="User Name",font=('bahnschrift',15),fg='white',bg='#000000')
            l1.place(x=10,y=10)
            t1=tk.Entry(window,font=('bahnschrift',15),width =15)
            t1.place(x=200,y=10)
            l2=tk.Label(window,text="Password",font=('bahnschrift',15),fg='white',bg='#000000')
            l2.place(x=10,y=60)
            t2=tk.Entry(window,font=('bahnschrift',15),width =15)
            t2.place(x=200,y=60)
            l3=tk.Label(window,text="Re enter password",font=('bahnschrift',15),fg='white',bg='#000000')
            l3.place(x=10,y=110)
            t3=tk.Entry(window,font=('bahnschrift',15),width =15)
            t3.place(x=200,y=110)
            def spy():
                if t1.get()!="" or t2.get()!="" or t3.get()!="":
                    if t2.get()==t3.get():
                        with open("cred.txt","a") as f:
                            f.write(t1.get()+","+t2.get()+"\n")
                            messagebox.showinfo("Registered Sucessfully!!!")
                    else:
                        messagebox.showinfo("Your Password didn't match!!!")
                else:
                    messagebox.showinfo("Please provide details!!!")
                    
            b1=tk.Button(window,text='Sign in',font=('bahnschrift',15),fg='white',bg='#000000',command=spy)
            b1.place(x=170,y=150)
            window.geometry("470x220")
            window.mainloop()
        ls_btn=tk.Button(self,text="Register",font=('bahnschrift',15),command=register,fg="#000000",bg='white',padx=1)
        ls_btn.place(x=500,y=700)
        
        
        
        
        
        


class Homepage(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent,bg='#1a1a1a')
        self.contoller=controller
        label1=tk.Label(self,text='Airline Home Page',font=('bahnschrift',40),fg='#ffffff',bg='#1a1a1a')
        label1.pack(pady=25)
        
        
        b_frame=tk.Frame(self,bg='#1a1a1a')
        b_frame.pack(fill='both',expand=True)
        load = Image.open("20210114_203549.jpg")
        photo=ImageTk.PhotoImage(load)
        label=tk.Label(b_frame,image=photo)
        label.image=photo
        label.place(x=0,y=0)
        fs_btn=tk.Button(b_frame,text="Add Flight Coordinators",font=('bahnschrift',15),bg='#1a1a1a',fg='white',command=lambda: controller.show_frame(flightschedulepage),relief='raised',borderwidth=2,width=50,height=5)
        fs_btn.grid(row=0,column=0)
        fa_btn=tk.Button(b_frame,text="Add Flight Schedules ",font=('bahnschrift',15),bg='#1a1a1a',fg='white',command=lambda: controller.show_frame(flightsarrival),relief='raised',borderwidth=2,width=50,height=5)
        fa_btn.grid(row=1,column=0)
        cr_btn=tk.Button(b_frame,text="Report Flight Departures",font=('bahnschrift',15),bg='#1a1a1a',fg='white',command=lambda: controller.show_frame(flapage),relief='raised',borderwidth=2,width=50,height=5)
        cr_btn.grid(row=2,column=0)
        cr1_btn=tk.Button(b_frame,text="Assign Crew ",font=('bahnschrift',15),bg='#1a1a1a',fg='white',command=lambda: controller.show_frame(mypage),relief='raised',borderwidth=2,width=50,height=5)
        cr1_btn.grid(row=3,column=0)
        cr2_btn=tk.Button(b_frame,text="Update Flight Arrivals",font=('bahnschrift',15),bg='#1a1a1a',fg='white',command=lambda: controller.show_frame(lastpage),relief='raised',borderwidth=2,width=50,height=5)
        cr2_btn.grid(row=4,column=0)
        cr3_btn=tk.Button(b_frame,text="View Cancelled Flights",font=('bahnschrift',15),bg='#1a1a1a',fg='white',command=lambda: controller.show_frame(cancelledpage),relief='raised',borderwidth=2,width=50,height=5)
        cr3_btn.grid(row=0,column=2)
        cr4_btn=tk.Button(b_frame,text="Exit",font=('bahnschrift',15),bg='#1a1a1a',fg='white',command=lambda: controller.show_frame(StartPage),relief='raised',borderwidth=2,width=50,height=5)
        cr4_btn.grid(row=1,column=2)
        
        
        

class flightschedulepage(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent,bg='#000000')
        load = Image.open("20210109_201129.jpg")
        photo=ImageTk.PhotoImage(load)
        label=tk.Label(self,image=photo)
        label.image=photo
        label.place(x=0,y=0)
        label2=tk.Label(self,text='Flight Coordinator Details',font=('bahnschrift',40),fg='#ffffff',bg='#000000')
        label2.pack()
        LeftFrame=tk.Frame(self,bd=0,relief='ridge',bg="#000000")
        LeftFrame.place(x=100,y=100,width=500,height=370)
        RightFrame=tk.Frame(self,bd=1,relief='ridge',bg="white")
        RightFrame.place(x=700,y=100,width=560,height=370)
        
        BottomFrame=tk.Frame(self,bd=0,relief='ridge',bg="#000000")
        BottomFrame.place(x=200,y=550,width=120,height=50)
        BottomFrame1=tk.Frame(self,bd=0,relief='ridge',bg="#000000")
        BottomFrame1.place(x=400,y=550,width=150,height=50)
        BottomFrame2=tk.Frame(self,bd=0,relief='ridge',bg="#000000")
        BottomFrame2.place(x=600,y=550,width=150,height=50)
        BottomFrame3=tk.Frame(self,bd=0,relief='ridge',bg="#000000")
        BottomFrame3.place(x=800,y=550,width=150,height=50)
        BottomFrame4=tk.Frame(self,bd=0,relief='ridge',bg="#000000")
        BottomFrame4.place(x=1000,y=550,width=150,height=50)
        BottomFrame6=tk.Frame(self,bd=0,relief='ridge',bg="#000000")
        BottomFrame6.place(x=1200,y=550,width=150,height=50)
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
        co_cno=tk.Label(LeftFrame,font=('bahnnschrift',15),text="Contact No:",fg='white',bg='#000000',padx=1)
        co_cno.grid(row=7,column=0)
        co_cno_en=tk.Entry(LeftFrame, font=('bahnschrift',15),width=15)
        co_cno_en.grid(row=7,column=1,pady=6, padx=20)
        co_age=tk.Label(LeftFrame,font=('bahnnschrift',15),text="Age:",fg='white',bg='#000000',padx=1)
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
            reset()
            viewData()
            messagebox.showinfo("Record Inserted!")
        s_btn=tk.Button(BottomFrame,font=('bahnschrift',22),text='Submit',command=submit,fg='#000000',bg='white',padx=2)
        s_btn.grid(row=2,column=1)
        def reset():
            co_no_en.delete(0,'end')
            co_fna_en.delete(0,'end')
            co_lna_en.delete(0,'end')
            co_age_en.delete(0,'end')
            co_cno_en.delete(0,'end')
            co_email_en.delete(0,'end')
        l_btn=tk.Button(BottomFrame6,font=('bahnschrift',22),text='Reset',command=reset,fg='#000000',bg='white',padx=2)
        l_btn.grid(row=2,column=1)
        
        
            
            
    
        fli_id=tk.Label(LeftFrame,font=('bahnschrift',15),text='Enter the CO ID to delete:',fg='white',bg='#000000',padx=1)
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
            viewData()
        
        
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
            reset()
            
            
            co_no_en.insert(0,r[0])
           
          
            co_fna_en.insert(1,r[1])
           
            co_lna_en.insert(2,r[2])
            co_age_en.insert(3,r[3])
            
            
            co_cno_en.insert(4,r[4])
           
            co_email_en.insert(5,r[5])
             
             
            
        scrollbar= tk.Scrollbar(RightFrame)
        scrollbar.grid(row=0, column=1,sticky='ns')
        style=ttk.Style()
        style.theme_use("default")
        style.configure("Treeview",background="silver",foreground="silver",rowheight=25,fieldground="silver")
        style.map('Treeview',background=[('selected','green')])
        


        airlinelist= ttk.Treeview(RightFrame ,height=30,column=("coid","cofna","colna","cocono","coag","coemail"), yscrollcommand=scrollbar.set )
        airlinelist.heading("coid",text="Coordinato ID")
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
            c.execute("UPDATE FLIGHT_CO SET CO_FNAME=?, CO_LNAME=?,  CO_AGE=?,CO_CONTNO=?, CO_EMAIL=?  WHERE CO_ID=?",(a,m,s,e,i,n))
            conn.commit()
            conn.close()
        

        
            


        u_btn=tk.Button(BottomFrame3,font=('bahnschrift',22),text='Update',command=update,fg='#000000',bg='white',padx=2)
        u_btn.grid(row=16,column=0)
            
class flightsarrival(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent,bg='#000000')
        label2=tk.Label(self,text='Flight Schedules ',font=('bahnschrift',40),fg='#ffffff',bg='#000000')
        label2.pack()
    
        
        LeftFrame=tk.Frame(self,bd=0,relief='ridge',bg="#000000")
        LeftFrame.place(x=100,y=100,width=470,height=450)
        RightFrame=tk.Frame(self,bd=1,relief='ridge',bg="white")
        RightFrame.place(x=700,y=100,width=760,height=370)
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
        BottomFrame6=tk.Frame(self,bd=0,relief='ridge',bg="#000000")
        BottomFrame6.place(x=1200,y=550,width=150,height=50)
        
        
        fl_no =tk.Label(LeftFrame, font=('bahnschrift',15),text="Flight No:",fg='white',bg='#000000')
        fl_no.grid(row=1,column=0)
        fl_no_en =tk.Entry(LeftFrame, font=('bahnschrift',15),width =15)
        fl_no_en.grid(row=1,column=1,padx=6,pady=20)
        fl_na=tk.Label(LeftFrame, font=('bahnschrift',15),text="Flight Name:",fg="white",bg="#000000",padx=1)
        fl_na.grid(row=2,column=0)
        fl_na_en=tk.Entry(LeftFrame, font=('bahnschrift',15),width=15)
        fl_na_en.grid(row=2,column=1,pady=6, padx=20)
        fl_type=tk.Label(LeftFrame,font=('bahnnschrift',15),text="Flight From:",fg='white',bg='#000000',padx=1)
        fl_type.grid(row=3,column=0)
        fl_type_en=tk.Entry(LeftFrame, font=('bahnschrift',15),width=15)
        fl_type_en.grid(row=3,column=1,pady=6, padx=20)
        fl_from=tk.Label(LeftFrame,font=('bahnnschrift',15),text="Flight To:",fg='white',bg='#000000',padx=1)
        fl_from.grid(row=4,column=0)
        fl_from_en=tk.Entry(LeftFrame, font=('bahnschrift',15),width=15)
        fl_from_en.grid(row=4,column=1,pady=6, padx=20)
        fl_de=tk.Label(LeftFrame,font=('bahnnschrift',15),text="Flight Capacity:",fg='white',bg='#000000',padx=1)
        fl_de.grid(row=5,column=0)
        fl_de_en=tk.Entry(LeftFrame, font=('bahnschrift',15),width=15)
        fl_de_en.grid(row=5,column=1,pady=6, padx=20)
        fl_ca=tk.Label(LeftFrame,font=('bahnnschrift',15),text="Flight Date:",fg='white',bg='#000000',padx=1)
        fl_ca.grid(row=6,column=0)
        fl_ca_en=tk.Entry(LeftFrame, font=('bahnschrift',15),width=15)
        fl_ca_en.grid(row=6,column=1,pady=6, padx=20)
        fl_da=tk.Label(LeftFrame,font=('bahnnschrift',15),text="Flight Time:",fg='white',bg='#000000',padx=1)
        fl_da.grid(row=7,column=0)
        fl_da_en=tk.Entry(LeftFrame, font=('bahnschrift',15),width=15)
        fl_da_en.grid(row=7,column=1,pady=6, padx=20)
        fl_ti=tk.Label(LeftFrame,font=('bahnnschrift',15),text="Scheduled CO:",fg='white',bg='#000000',padx=1)
        fl_ti.grid(row=8,column=0)
        fl_ti_en=tk.Entry(LeftFrame, font=('bahnschrift',15),width=15)
        fl_ti_en.grid(row=8,column=1,pady=6, padx=20)
        
        
        def submit():
            conn=sqlite3.connect('b.db')
            c=conn.cursor()
            c.execute("INSERT INTO FS VALUES(:f_no,:f_na,:f_da,:f_so,:f_de,:f_ti,:u,:g)",
                      {
                             'f_no':fl_no_en.get(),
                             'f_na':fl_na_en.get(),
                             'f_da':fl_type_en.get(),
                             'f_so':fl_from_en.get(),
                             'f_de':fl_de_en.get(),
                             'f_ti':fl_ca_en.get(),
                             'u':fl_da_en.get(),
                             'g':fl_ti_en.get()
                            
                             
                             })
            conn.commit()
            conn.close()
        s_btn=tk.Button(BottomFrame,font=('bahnschrift',22),text='Submit',command=submit,fg='#000000',bg='white',padx=2)
        s_btn.grid(row=2,column=1)
        def reset():
            fl_no_en.delete(0,'end')
            fl_na_en.delete(0,'end')
            fl_type_en.delete(0,'end')
            fl_from_en.delete(0,'end')
            fl_de_en.delete(0,'end')
            fl_ca_en.delete(0,'end')
            fl_da_en.delete(0,'end')
            fl_ti_en.delete(0,'end')
        l_btn=tk.Button(BottomFrame6,font=('bahnschrift',22),text='Reset',command=reset,fg='#000000',bg='white',padx=2)
        l_btn.grid(row=2,column=1)

        
        
        
        
        
            
            
    
        fli_id=tk.Label(LeftFrame,font=('bahnschrift',15),text='Enter the Flight No to cancel:',fg='white',bg='#000000',padx=1)
        fli_id.grid(row=12,column=0)
        fli_id_en=tk.Entry(LeftFrame,font=('bahnschrift',15),width=15)
        fli_id_en.grid(row=12,column=1,pady=6, padx=20)
        fs_btn=tk.Button(BottomFrame5,text="Home",font=('bahnschrift',22),command=lambda: controller.show_frame(Homepage),fg="#000000",bg='white',padx=1)
        fs_btn.grid(row=0,column=2)
        

        def viewData():
            con = sqlite3.connect("b.db")
            cur = con.cursor()
            cur.execute("SELECT * FROM FS")
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
            fl_de_en.insert(4,r[4])
            fl_ca_en.insert(5,r[5])
            fl_da_en.insert(6,r[6])
            fl_ti_en.insert(7,r[7])
            
            
            
             
            
        scrollbar= tk.Scrollbar(RightFrame)
        scrollbar.grid(row=0, column=1,sticky='ns')
        


        airlinelist= ttk.Treeview(RightFrame, height=16,column=("fno","fna","ffrom","fto","fca","fda","fti","schedco"), yscrollcommand=scrollbar.set )
        airlinelist.heading("fno",text="Flight No")
        airlinelist.heading("fna",text="First Name")
        airlinelist.heading("ffrom",text="Flight From")
        airlinelist.heading("fto",text="Flight To")
        airlinelist.heading("fca",text="Flight Capacity")
        airlinelist.heading("fda",text="Flight date")
        airlinelist.heading("fti",text="Flight Time")
        airlinelist.heading("schedco",text="Scheduled CO")

        airlinelist['show']='headings'

        airlinelist.column("fno",width=90)
        airlinelist.column("fna",width=90)
        airlinelist.column("ffrom",width=90)
        airlinelist.column("fto",width=90)
        airlinelist.column("fca",width=90)
        airlinelist.column("fda",width=90)
        airlinelist.column("fti",width=90)
        airlinelist.column("schedco",width=90)

        airlinelist.bind('<ButtonRelease>',selected)

        airlinelist.grid(row=0,column=0,sticky='ns')

        d_btn=tk.Button(BottomFrame2,font=('bahnschrift',22),text='Display',command=viewData,fg='#000000',bg='white',padx=2)
        d_btn.grid(row=11,column=0)

        
        

        
        
        
        
        
        
        
        
        
        

        
        
                

        def deleteRec():
                con=sqlite3.connect("b.db")
                cur = con.cursor()
                cur.execute("DELETE FROM FS WHERE FL_NO="+ fli_id_en.get())
                con.commit()
                con.close
        delet_btn=tk.Button(BottomFrame1,font=('bahnschrift',22),text='Delete',command=deleteRec,fg='#000000',bg='white',padx=2)
        delet_btn.grid(row=0,column=5)
        
        
        
        def searchDatabase():
            airlinelist.delete(*airlinelist.get_children())
            
            for row in searchData(fl_no_en.get(),fl_na_en.get(),fl_type_en.get(),fl_from_en.get(),fl_de_en.get(),fl_ca_en.get(),fl_da_en.get(),fl_ti_en.get()):
                airlinelist.insert('','end',value=row)
                
        def searchData(FL_NO="",FL_NAME="",FLI_FROM="",FLI_TO="",FLI_CAPACITY="",FLI_DATE="",FLI_DUR="",SCHED_CO=""):
            con=sqlite3.connect("b.db")
            cur = con.cursor()
            cur.execute("SELECT * FROM FS WHERE FL_NO=? OR FL_NAME=? OR FLI_FROM=? OR FLI_TO=? OR FLI_CAPACITY=? OR FLI_DATE=? OR FLI_DUR=? OR SCHED_CO=?", \
                        (FL_NO,FL_NAME,FLI_FROM,FLI_TO,FLI_CAPACITY,FLI_DATE,FLI_DUR,SCHED_CO))
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
            s=fl_de_en.get()
            i=fl_ca_en.get()
            j=fl_da_en.get()
            k=fl_ti_en.get()
            
            conn=sqlite3.connect('b.db')
            c=conn.cursor()
            c.execute("UPDATE FS SET FL_NAME=?, FLI_FROM=?, FLI_TO=?, FLI_CAPACITY=?,FLI_DATE=?,FLI_DUR=?,SCHED_CO=? WHERE FL_NO=? ",(a,m,e,s,i,j,k,n))
            conn.commit()
            conn.close()
        u_btn=tk.Button(BottomFrame3,font=('bahnschrift',22),text='Update',command=update,fg='#000000',bg='white',padx=2)
        u_btn.grid(row=16,column=0)
        

        
            


        
class flapage(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent,bg='#000000')
        label2=tk.Label(self,text='Flight Departures Details',font=('bahnschrift',40),fg='#ffffff',bg='#000000')
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
        BottomFrame6=tk.Frame(self,bd=0,relief='ridge',bg="#000000")
        BottomFrame6.place(x=1200,y=550,width=150,height=50)
        
        #main_la=tk.Label(LeftFrame,font=('bahnschrift',20),text='Flight Schedule Details')
        #main_la.grid()
        co_no =tk.Label(LeftFrame, font=('bahnschrift',15),text="Flight No:",fg='white',bg='#000000')
        co_no.grid(row=1,column=0)
        co_no_en =tk.Entry(LeftFrame, font=('bahnschrift',15),width =15)
        co_no_en.grid(row=1,column=1,padx=6,pady=20)
        co_fna=tk.Label(LeftFrame, font=('bahnschrift',15),text="Flight Name:",fg="white",bg="#000000",padx=1)
        co_fna.grid(row=3,column=0)
        co_fna_en=tk.Entry(LeftFrame, font=('bahnschrift',15),width=15)
        co_fna_en.grid(row=3,column=1,pady=6, padx=20)
        co_lna=tk.Label(LeftFrame,font=('bahnnschrift',15),text="Flight Type:",fg='white',bg='#000000',padx=1)
        co_lna.grid(row=5,column=0)
        co_lna_en=tk.Entry(LeftFrame, font=('bahnschrift',15),width=15)
        co_lna_en.grid(row=5,column=1,pady=6, padx=20)
        co_cno=tk.Label(LeftFrame,font=('bahnnschrift',15),text="Flight Destination:",fg='white',bg='#000000',padx=1)
        co_cno.grid(row=7,column=0)
        co_cno_en=tk.Entry(LeftFrame, font=('bahnschrift',15),width=15)
        co_cno_en.grid(row=7,column=1,pady=6, padx=20)
        co_age=tk.Label(LeftFrame,font=('bahnnschrift',15),text="Flight departure time:",fg='white',bg='#000000',padx=1)
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
            c.execute("INSERT INTO F VALUES(:f_no,:f_na,:f_da,:f_so,:f_de,:f_ti)",
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
        def reset():
            co_no_en.delete(0,'end')
            co_fna_en.delete(0,'end')
            co_lna_en.delete(0,'end')
            co_age_en.delete(0,'end')
            co_cno_en.delete(0,'end')
            co_email_en.delete(0,'end')
        l_btn=tk.Button(BottomFrame6,font=('bahnschrift',22),text='Reset',command=reset,fg='#000000',bg='white',padx=2)
        l_btn.grid(row=2,column=1)
        
        

        
        
            
            
    
        fli_id=tk.Label(LeftFrame,font=('bahnschrift',15),text='Enter the Flight No to delete:',fg='white',bg='#000000',padx=1)
        fli_id.grid(row=13,column=0)
        fli_id_en=tk.Entry(LeftFrame,font=('bahnschrift',15),width=15)
        fli_id_en.grid(row=13,column=1,pady=6, padx=20)
        fs_btn=tk.Button(BottomFrame5,text="Home",font=('bahnschrift',22),command=lambda: controller.show_frame(Homepage),fg="#000000",bg='white',padx=1)
        fs_btn.grid(row=0,column=2)
        
        
        
        
        def delete():
            
           
            
            conn=sqlite3.connect('b.db')
            c=conn.cursor()
            c.execute("DELETE from F WHERE F_NO="+ fli_id_en.get())
            
            
            
            
                      
            
            conn.commit()
            conn.close()
        
        
        delet_btn=tk.Button(BottomFrame1,font=('bahnschrift',22),text='Delete',command=delete,fg='#000000',bg='white',padx=2)
        delet_btn.grid(row=0,column=5)
        
        def viewData():
            con = sqlite3.connect("b.db")
            cur = con.cursor()
            cur.execute("SELECT * FROM F")
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
        airlinelist.heading("coid",text="Flight No")
        airlinelist.heading("cofna",text="FLight Name")
        airlinelist.heading("colna",text="Flight Type ")
        airlinelist.heading("cocono",text="Flight To")
        airlinelist.heading("coag",text="Flight Time")
        airlinelist.heading("coemail",text="Reported CO ID")

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
        def searchData(F_NO="",F_NA="",F_TY="",F_TO="",F_TIME="",REP_CO=""):
            con=sqlite3.connect("b.db")
            cur = con.cursor()
            cur.execute("SELECT  *FROM F WHERE F_NO=? OR F_NA=? OR F_TY=? OR F_TO=? OR F_TIME=? OR REP_CO=? ", \
                (F_NO,F_NA,F_TY,F_TO,F_TIME,REP_CO))
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
            c.execute("UPDATE F SET F_NA=?, F_TY=?, F_TO=?, F_TIME=?, REP_CO=?  WHERE F_NO=?",(a,m,e,s,i,n))
            conn.commit()
            conn.close()
        

        
            


        u_btn=tk.Button(BottomFrame3,font=('bahnschrift',22),text='Update',command=update,fg='#000000',bg='white',padx=2)
        u_btn.grid(row=16,column=0)

class mypage(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent,bg='#000000')
        label2=tk.Label(self,text='Crew Details',font=('bahnschrift',40),fg='#ffffff',bg='#000000')
        label2.pack()
        LeftFrame=tk.Frame(self,bd=0,relief='ridge',bg="#000000")
        LeftFrame.place(x=100,y=100,width=470,height=400)
        RightFrame=tk.Frame(self,bd=1,relief='ridge',bg="white")
        RightFrame.place(x=700,y=100,width=640,height=370)
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
        BottomFrame6=tk.Frame(self,bd=0,relief='ridge',bg="#000000")
        BottomFrame6.place(x=1200,y=550,width=150,height=50)
        
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
        co_assf=tk.Label(LeftFrame,font=('bahnnschrift',15),text="Assigned Flight:",fg='white',bg='#000000',padx=1)
        co_assf.grid(row=12,column=0)
        co_assf_en=tk.Entry(LeftFrame, font=('bahnschrift',15),width=15)
        co_assf_en.grid(row=12,column=1,pady=6, padx=20)
        
        co_email=tk.Label(LeftFrame,font=('bahnnschrift',15),text="Assigned by:",fg='white',bg='#000000',padx=1)
        co_email.grid(row=13,column=0)
        co_email_en=tk.Entry(LeftFrame, font=('bahnschrift',15),width=15)
        co_email_en.grid(row=13,column=1,pady=6, padx=20)
        
        def submit():
            conn=sqlite3.connect('b.db')
            c=conn.cursor()
            c.execute("INSERT INTO CREW VALUES(:f_no,:f_na,:f_da,:f_so,:f_de,:fc,:f_ti)",
                      {
                             'f_no':co_no_en.get(),
                             'f_na':co_fna_en.get(),
                             'f_da':co_lna_en.get(),
                             'f_so':co_age_en.get(),
                             'f_de':co_cno_en.get(),
                             'fc':co_assf_en.get(),
                             'f_ti':co_email_en.get()

                             })
            conn.commit()
            conn.close()
        s_btn=tk.Button(BottomFrame,font=('bahnschrift',22),text='Submit',command=submit,fg='#000000',bg='white',padx=2)
        s_btn.grid(row=2,column=1)
        def reset():
            co_no_en.delete(0,'end')
            co_fna_en.delete(0,'end')
            co_lna_en.delete(0,'end')
            co_age_en.delete(0,'end')
            co_cno_en.delete(0,'end')
            co_assf_en.delete(0,'end')
            co_email_en.delete(0,'end')
        l_btn=tk.Button(BottomFrame6,font=('bahnschrift',22),text='Reset',command=reset,fg='#000000',bg='white',padx=2)
        l_btn.grid(row=2,column=1)
        
        
        
            
            
    
        fli_id=tk.Label(LeftFrame,font=('bahnschrift',15),text='Enter the Crew No to delete:',fg='white',bg='#000000',padx=1)
        fli_id.grid(row=15,column=0)
        fli_id_en=tk.Entry(LeftFrame,font=('bahnschrift',15),width=15)
        fli_id_en.grid(row=15,column=1,pady=6, padx=20)
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
            co_cno_en.insert(4,r[4])
            
            
            co_age_en.insert(3,r[3])
            co_assf_en.insert(5,r[5])
            
           
            co_email_en.insert(6,r[6])
             
             
            
        scrollbar= tk.Scrollbar(RightFrame)
        scrollbar.grid(row=0, column=1,sticky='ns')
        


        airlinelist= ttk.Treeview(RightFrame, height=16,column=("coid","cofna","colna","cocono","coag","coass","coemail"), yscrollcommand=scrollbar.set )
        airlinelist.heading("coid",text="Crew id")
        airlinelist.heading("cofna",text="Crew Name")
        airlinelist.heading("colna",text="Crew Age")
        airlinelist.heading("cocono",text="Contac No")
        airlinelist.heading("coag",text="Role")
        airlinelist.heading("coass",text="Assignd Flight")
        airlinelist.heading("coemail",text="Assigned CO")

        airlinelist['show']='headings'

        airlinelist.column("coid",width=90)
        airlinelist.column("cofna",width=90)
        airlinelist.column("colna",width=90)
        airlinelist.column("cocono",width=90)
        airlinelist.column("coag",width=90)
        airlinelist.column("coass",width=90)
        airlinelist.column("coemail",width=90)

        airlinelist.bind('<ButtonRelease>',selected)

        airlinelist.grid(row=0,column=0,sticky='ns')

        
        

        d_btn=tk.Button(BottomFrame2,font=('bahnschrift',22),text='Display',command=viewData,fg='#000000',bg='white',padx=2)
        d_btn.grid(row=11,column=0)
        def searchDatabase():
            airlinelist.delete(*airlinelist.get_children())
            for row in searchData(co_no_en.get(),co_fna_en.get(),co_lna_en.get(),co_cno_en.get(),co_age_en.get(),co_assf_en.get(),co_email_en.get()):
                airlinelist.insert('','end',value=row)
        def searchData(CREW_ID="",CREW_NAME="",CREW_AGE="",CREW_ROLE="",CREW_CN="",ASS_F="",ASS_COID=""):
            con=sqlite3.connect("b.db")
            cur = con.cursor()
            cur.execute("SELECT * FROM CREW WHERE CREW_ID=? OR CREW_NAME=? OR CREW_AGE=? OR CREW_ROLE=? OR CREW_CN=? OR ASS_F=? OR ASS_COID=?", \
                (CREW_ID,CREW_NAME,CREW_AGE,CREW_ROLE,CREW_CN,ASS_F,ASS_COID))
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
            l=co_assf_en.get()
            i=co_email_en.get()
            conn=sqlite3.connect('b.db')
            c=conn.cursor()
            c.execute("UPDATE CREW SET CREW_NAME=?, CREW_AGE=?, CREW_ROLE=?, CREW_CN=?,ASS_F=?, ASS_COID=?  WHERE CREW_ID=?",(a,m,e,l,s,i,n))
            conn.commit()
            conn.close()
        

        
            


        u_btn=tk.Button(BottomFrame3,font=('bahnschrift',22),text='Update',command=update,fg='#000000',bg='white',padx=2)
        u_btn.grid(row=16,column=0)
class lastpage(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent,bg='#000000')
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
        BottomFrame6=tk.Frame(self,bd=0,relief='ridge',bg="#000000")
        BottomFrame6.place(x=1200,y=550,width=150,height=50)
    
        BottomFrame3=tk.Frame(self,bd=0,relief='ridge',bg="#000000")
        BottomFrame3.place(x=800,y=550,width=150,height=50)
        BottomFrame4=tk.Frame(self,bd=0,relief='ridge',bg="#000000")
        BottomFrame4.place(x=1000,y=550,width=150,height=50)
        BottomFrame5=tk.Frame(self,bd=0,relief='ridge',bg="#000000")
        BottomFrame5.place(x=600,y=650,width=150,height=50)
        
        #main_la=tk.Label(LeftFrame,font=('bahnschrift',20),text='Flight Schedule Details')
        #main_la.grid()
        co_no =tk.Label(LeftFrame, font=('bahnschrift',15),text="Flight No:",fg='white',bg='#000000')
        co_no.grid(row=1,column=0)
        co_no_en =tk.Entry(LeftFrame, font=('bahnschrift',15),width =15)
        co_no_en.grid(row=1,column=1,padx=6,pady=20)
        co_fna=tk.Label(LeftFrame, font=('bahnschrift',15),text="Flight Name:",fg="white",bg="#000000",padx=1)
        co_fna.grid(row=3,column=0)
        co_fna_en=tk.Entry(LeftFrame, font=('bahnschrift',15),width=15)
        co_fna_en.grid(row=3,column=1,pady=6, padx=20)
        co_lna=tk.Label(LeftFrame,font=('bahnnschrift',15),text="Flight Type:",fg='white',bg='#000000',padx=1)
        co_lna.grid(row=5,column=0)
        co_lna_en=tk.Entry(LeftFrame, font=('bahnschrift',15),width=15)
        co_lna_en.grid(row=5,column=1,pady=6, padx=20)
        co_cno=tk.Label(LeftFrame,font=('bahnnschrift',15),text="Flight From:",fg='white',bg='#000000',padx=1)
        co_cno.grid(row=7,column=0)
        co_cno_en=tk.Entry(LeftFrame, font=('bahnschrift',15),width=15)
        co_cno_en.grid(row=7,column=1,pady=6, padx=20)
        co_age=tk.Label(LeftFrame,font=('bahnnschrift',15),text="Flight Arrived time:",fg='white',bg='#000000',padx=1)
        co_age.grid(row=9,column=0)
        co_age_en=tk.Entry(LeftFrame, font=('bahnschrift',15),width=15)
        co_age_en.grid(row=9,column=1,pady=6, padx=20)
        co_email=tk.Label(LeftFrame,font=('bahnnschrift',15),text="Updated CO ID:",fg='white',bg='#000000',padx=1)
        co_email.grid(row=12,column=0)
        co_email_en=tk.Entry(LeftFrame, font=('bahnschrift',15),width=15)
        co_email_en.grid(row=12,column=1,pady=6, padx=20)
        
        def submit():
            conn=sqlite3.connect('b.db')
            c=conn.cursor()
            c.execute("INSERT INTO FD VALUES(:f_no,:f_na,:f_da,:f_so,:f_de,:f_ti)",
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
        def reset():
            co_no_en.delete(0,'end')
            co_fna_en.delete(0,'end')
            co_lna_en.delete(0,'end')
            co_age_en.delete(0,'end')
            co_cno_en.delete(0,'end')
            co_email_en.delete(0,'end')
        l_btn=tk.Button(BottomFrame6,font=('bahnschrift',22),text='Reset',command=reset,fg='#000000',bg='white',padx=2)
        l_btn.grid(row=2,column=1)

            
        
        
        
            
            
    
        fli_id=tk.Label(LeftFrame,font=('bahnschrift',15),text='Enter the Flight No to delete:',fg='white',bg='#000000',padx=1)
        fli_id.grid(row=13,column=0)
        fli_id_en=tk.Entry(LeftFrame,font=('bahnschrift',15),width=15)
        fli_id_en.grid(row=13,column=1,pady=6, padx=20)
        fs_btn=tk.Button(BottomFrame5,text="Home",font=('bahnschrift',22),command=lambda: controller.show_frame(Homepage),fg="#000000",bg='white',padx=1)
        fs_btn.grid(row=0,column=2)
        
        
        
        
        def delete():
            
           
            
            conn=sqlite3.connect('b.db')
            c=conn.cursor()
            c.execute("DELETE from FD WHERE F_NO="+ fli_id_en.get())
            
            
            
            
                      
            
            conn.commit()
            conn.close()
        
        
        delet_btn=tk.Button(BottomFrame1,font=('bahnschrift',22),text='Delete',command=delete,fg='#000000',bg='white',padx=2)
        delet_btn.grid(row=0,column=5)
        
        def viewData():
            con = sqlite3.connect("b.db")
            cur = con.cursor()
            cur.execute("SELECT * FROM FD")
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
        airlinelist.heading("coid",text="Flight No")
        airlinelist.heading("cofna",text="FLight Name")
        airlinelist.heading("colna",text="Flight Type ")
        airlinelist.heading("cocono",text="Flight From")
        airlinelist.heading("coag",text="Flight Time")
        airlinelist.heading("coemail",text="Updated CO")

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
        def searchData(F_NO="",F_NA="",F_TY="",F_ARR="",F_TIME="",REP_CO=""):
            con=sqlite3.connect("b.db")
            cur = con.cursor()
            cur.execute("SELECT * FROM FD WHERE F_NO=? OR F_NA=? OR F_TY=? OR F_ARR=? OR F_TIME=? OR REP_CO=? ", \
                (F_NO,F_NA,F_TY,F_ARR,F_TIME,REP_CO))
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
            c.execute("UPDATE FD SET F_NA=?, F_TY=?, F_ARR=?, F_TIME=?, REP_CO=?  WHERE F_NO=?",(a,m,e,s,i,n))
            conn.commit()
            conn.close()
        

        
            


        u_btn=tk.Button(BottomFrame3,font=('bahnschrift',22),text='Update',command=update,fg='#000000',bg='white',padx=2)
        u_btn.grid(row=16,column=0)
class cancelledpage(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent,bg='#000000')
        label2=tk.Label(self,text='Cancelled Flights',font=('bahnschrift',40),fg='#ffffff',bg='#000000')
        label2.pack()
        RightFrame=tk.Frame(self,bd=1,relief='ridge',bg="white")
        RightFrame.place(x=500,y=100,width=560,height=370)
        scrollbar= tk.Scrollbar(RightFrame)
        scrollbar.grid(row=0, column=1,sticky='ns')
        BottomFrame2=tk.Frame(self,bd=1,relief='ridge',bg="#000000")
        BottomFrame2.place(x=600,y=550,width=320,height=50)
        BottomFrame5=tk.Frame(self,bd=0,relief='ridge',bg="#000000")
        BottomFrame5.place(x=600,y=650,width=150,height=50)
        


        airlinelist= ttk.Treeview(RightFrame, height=16,column=("coid","cofna","colna","cocono","coag","coass","coemail"), yscrollcommand=scrollbar.set )
        airlinelist.heading("coid",text="Cancelled No")
        airlinelist.heading("cofna",text="Flight No")
        airlinelist.heading("colna",text="Flight Name")
        airlinelist.heading("cocono",text="Flight From")
        airlinelist.heading("coag",text="Flight To")
        airlinelist.heading("coass",text="Dated On")
        
        airlinelist['show']='headings'

        airlinelist.column("coid",width=90)
        airlinelist.column("cofna",width=90)
        airlinelist.column("colna",width=90)
        airlinelist.column("cocono",width=90)
        airlinelist.column("coag",width=90)
        airlinelist.column("coass",width=90)
        

        

        airlinelist.grid(row=0,column=0,sticky='ns')
        def viewData():
            con = sqlite3.connect("b.db")
            cur = con.cursor()
            cur.execute("SELECT * FROM DELETED_F")
            row =cur.fetchall()
            airlinelist.delete(*airlinelist.get_children())
            if len(row)!=0:
                        for num in row:
                            
                            airlinelist.insert('','end',value=num)
        d_btn=tk.Button(BottomFrame2,font=('bahnschrift',22),text='View Cancelled Flights',command=viewData,fg='#000000',bg='white',padx=2)
        d_btn.grid(row=11,column=0)
        fs_btn=tk.Button(BottomFrame5,text="Home",font=('bahnschrift',22),command=lambda: controller.show_frame(Homepage),fg="#000000",bg='white',padx=1)
        fs_btn.grid(row=0,column=2)
            
            

        
        
        
            
       
app=airlinewebapp()
app.mainloop()
    
