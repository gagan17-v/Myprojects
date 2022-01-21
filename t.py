import tkinter as tk
import sqlite3
conn=sqlite3.connect('b.db')
c=conn.cursor()
c.execute("CREATE PROCEDURE select AS  BEGIN SELECT * FROM DELETED_F END")
            
            
            
            
            
                      
            
conn.commit()
conn.close()
