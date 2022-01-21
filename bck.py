class lastpage(tk.Frame):

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
        
        
        
            
            
    
        fli_id=tk.Label(LeftFrame,font=('bahnschrift',15),text='Enter the Crew No to delete:',fg='white',bg='#000000',padx=1)
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
            viewinfo=airlinelis.focus()
            mysl=airlinelis.item(viewinfo)
            r=mysl['values']
            
            
            co_no_en.insert(0,r[0])
           
          
            co_fna_en.insert(1,r[1])
           
            co_lna_en.insert(2,r[2])
            co_cno_en.insert(3,r[3])
            
            
            co_age_en.insert(4,r[4])
           
            co_email_en.insert(5,r[5])
             
             
            
        scrollbar= tk.Scrollbar(RightFrame)
        scrollbar.grid(row=0, column=1,sticky='ns')
        


        airlinelis= ttk.Treeview(RightFrame, height=16,column=("coid","cofna","colna","cocono","coag","coemail"), yscrollcommand=scrollbar.set )
        airlinelis.heading("coid",text="Coordinator Id")
        airlinelis.heading("cofna",text="First Name")
        airlinelis.heading("colna",text="Last Name")
        airlinelis.heading("cocono",text="Age")
        airlinelis.heading("coag",text="Contact No")
        airlinelis.heading("coemail",text="Email")

        airlinelis['show']='headings'

        airlinelis.column("coid",width=90)
        airlinelis.column("cofna",width=90)
        airlinelis.column("colna",width=90)
        airlinelis.column("cocono",width=90)
        airlinelis.column("coag",width=90)
        airlinelis.column("coemail",width=90)

        airlinelis.bind('<ButtonRelease>',selected)

        airlinelis.grid(row=0,column=0,sticky='ns')

        
        

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
            c.execute("UPDATE FD SET F_NA=?, F_TY=?, F_TO=?, F_TIME=?, REP_CO=?  WHERE F_NO=?",(a,m,e,s,i,n))
            conn.commit()
            conn.close()
        

        
            


        u_btn=tk.Button(BottomFrame3,font=('bahnschrift',22),text='Update',command=update,fg='#000000',bg='white',padx=2)
        u_btn.grid(row=16,column=0)
            
       
        
            

       
    
            
            
            
            
    
        
        
        
