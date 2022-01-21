import sqlite3

conn=sqlite3.connect('air.db')
c=conn.cursor()
c.execute("""CREATE TABLE flightschedules (flight_no text,flight_name text,origin text,destination text,time text,flight_capacity text ,miles text)""")
c.execute("""CREATE TABLE flightarrival (flight_no text,flight_name text,flight_service text,flight_from text,flight_atime text)""")
c.execute("""CREATE TABLE flightdeparture(flight_no text,flight_name text,flight_service text,flight_to text,flight_dtime text)""")
conn.commit()
conn.close()
