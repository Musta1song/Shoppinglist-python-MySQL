from tkinter import *
import tkinter
import mysql.connector as myconn
from tkinter.messagebox import showinfo
from tkinter.font import Font
import time
from datetime import datetime


currTime = datetime.now()
year = str((currTime.year))
month = str((currTime.month))
day = str((currTime.day))
todaysDate = (year+"-"+month+"-"+day)




mydb = myconn.connect(
  host="localhost",
  user="root",
  password="",
  database="Einkaufsliste")
print(mydb)
obj= mydb.cursor();
obj.execute("CREATE DATABASE IF NOT EXISTS Einkaufsliste");
obj.execute("CREATE TABLE IF NOT EXISTS Einkaufsliste(produkt TEXT, erledigt_am DATE, erledigt_von TEXT)")
my_conn = mydb.cursor()




fn = tkinter.Tk()                    # fenster
fn.title("Einkaufsliste")                  
fn.resizable(False, False)
fn.columnconfigure(0, weight=1)
fn.rowconfigure(0, weight=1)
img = PhotoImage(file="shopping.png")
background_label = Label(image=img)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
def show():
 label1= Label(fn,text="Produkt")
 label1.grid(padx=5,pady=5,column=0,row=0)
 label2= Label(fn,text="erledigt am: ")
 label2.grid(column=1,row=0)
 label3= Label(fn,text="erledigt von: ")
 label3.grid(column=2,row=0)


 i=1
 obj.execute("SELECT * FROM Einkaufsliste")
 for Einkaufsliste in obj: 
  for j in range(len(Einkaufsliste)):
        e = Listbox(fn,fg='green', height=1)
        
        e.configure(font=("Times New Roman", 14))

        e.grid(padx=3,pady=10,row=i, column=j) 
        e.insert(END, Einkaufsliste[j])
        
        
  i=i+1 
falsch = 'false'
i1=1
def destroy():
   fn.destroy()
def addtolist():
    if entry1.get() != "":
     entryGet= entry1.get()
     add=("INSERT INTO Einkaufsliste (produkt, erledigt_am)" "Values(%s,%s)")
     addinsert= (entryGet, "offen")
     obj.execute(add, addinsert)
     mydb.commit()
    show()
def reflist(): 
   entryGet= entry1.get()
   add=("UPDATE Einkaufsliste SET erledigt_am = %s WHERE produkt=%s;")
   addinsert= (todaysDate,entryGet)
   obj.execute(add,addinsert)
   mydb.commit()
   show()
def reflist2(): 
   entryGet= entry1.get()
   erledigtvon = entry2.get()
   add="""UPDATE Einkaufsliste SET erledigt_von = %s WHERE produkt=%s;"""
   addinsert= (erledigtvon,entryGet)
   obj.execute(add,addinsert)
   mydb.commit()
   show()
def removal():
  obj.execute("DELETE FROM Einkaufsliste WHERE erledigt_am IS NOT NULL;")
  mydb.commit()
  time.sleep(2)
  show()
def deleteall():
   obj.execute("DELETE FROM Einkaufsliste;")
   mydb.commit()
   show()
entry1 = Entry(fn, bg="light blue")
entry1.grid(row=1,column=4,padx=0,pady=0,sticky='news')

bn1 = tkinter.Button(fn, text="Zur Einkaufsliste\nhinzufügen",command=addtolist, width=25,bg="light blue")
bn1.grid(row=2, column=4, padx=1, pady=10, sticky="w")

bn2 = tkinter.Button(fn, text="als erledigt markieren",command=reflist, width=25,bg="light blue")
bn2.grid(row=3, column=4, padx=1, pady=10, sticky="w")

entry2 = Entry(fn, bg="light green")
entry2.grid(row=1,column=5,padx=10)

bn3 = tkinter.Button(fn, text="erledigt von:",
                     command=reflist2, width=15, bg="light green")
bn3.grid(row=1, column=6, padx=10, pady=10, sticky="w")
bn4 = tkinter.Button(fn, text="erledigte Einträge\nlöschen:",
                     command=removal, width=15)
bn4.grid(row=3, column=6, padx=10, pady=10, sticky="w")
bn5 = tkinter.Button(fn, text="Einkaufsliste leeren",
                     command=deleteall, width=15)
bn5.grid(row=4,column=6,padx=10, pady=10, sticky="w")
bn6 = tkinter.Button(fn, text="Ende",command=destroy, width=16,bg="light gray")

bn6.grid(row=4,column=4,padx=10, pady=10, sticky="w")

show()
xyz =input()

mainloop()
