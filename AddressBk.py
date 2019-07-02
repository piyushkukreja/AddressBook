#root is created from Tkinter's constructor Tk()
#a frame is fit above the root to work upon(objects will be placed on the frame)
#Syntax:
	#Frame(rootname, heightVal, widthVal, backgroundColor, cursor)
	#Label(frameName, fontObj, lblTxt, lblBgColor)
	#Button(frameName, btnTxt, height, width, bgColor, activeBgColor, font)
	#Entry is used for single line text field: Entry(frameName, width)
	#obj.place(x, y) is used for placing the certain object to its position
	#font = (fontName, fontSize, fontStyle)
        #rbObj = Radiobutton(frameName, variable = varName, value=valType, text, bgColor, font)
try:
	from Tkinter import *
except ImportError:
	from tkinter import *
import sqlite3
conn = sqlite3.connect("addrbk.db")
cursor = conn.cursor()
def  create():
        cursor.execute("CREATE TABLE IF NOT EXISTS details(name varchar(255),email varchar(255),phone int(11),address text(255),gender varchar(255))")
create()
root = Tk()
root.title("Contact Book")
f = Frame(root,height=1000,width=1000,bg='skyblue')#here Frame is just like class name of Java
f.pack(expand=YES,fill='both')
fnt=("Helvetica","14","bold")
#CREATING ALL COMPONENTS
#name
namelbl = Label(f, font=fnt, text='Enter Name', bg='skyblue')
nameTf = Entry(f, width=30, bg='white')
#email
emaillbl = Label(f, font=fnt, text='Enter Email ID', bg='skyblue')
emailTf = Entry(f, width=30, bg='white')
#number
phonelbl = Label(f, font=fnt, text='Enter Phone No.', bg='skyblue')
phoneTf = Entry(f, width=30, bg='white')
#address
addresslbl = Label(f, font=fnt, text='Address', bg='skyblue')
addressTf = Text(f, height=10, width=30, bg='white')
#gender radio button
var1 = IntVar()
genderlbl = Label(f, font=fnt, text='Gender', bg='skyblue')
male = Radiobutton(f,variable = var1, value=1, text='Male', bg='skyblue', font=fnt)
female = Radiobutton(f,variable = var1, value=2, text='Female', bg='skyblue', font=fnt)

#search field
searchlbl = Label(f, font=fnt, text='Search Name', bg='skyblue')
searchTf = Entry(f, width=30, bg='white')

#search result
#srchRes = Text(f, height=20, width = 30, bg='white')

#PLACING ALL COMPONENTS
namelbl.place(x=10, y=10)
nameTf.place(x=200, y=15)

emaillbl.place(x=10,y=50)
emailTf.place(x=200,y=55)

phonelbl.place(x=10,y=90)
phoneTf.place(x=200,y=95)

addresslbl.place(x=10,y=140)
addressTf.place(x=200,y=145)

genderlbl.place(x=10,y=320)
male.place(x=200,y=325)
female.place(x=330,y=325)

searchlbl.place(x=500,y=10)
searchTf.place(x=650,y=15)

#srchRes.place(x=650,y=115)


def insertIntoDb():
        name = nameTf.get()
        email = emailTf.get()
        phone = phoneTf.get()
        address = addressTf.get("1.0","end-1c")
        val = var1.get()
        if val == 1:
                v = male["text"]
        elif val == 2:
                v = female["text"]
        cursor.execute("INSERT INTO details(name, email, phone, address, gender) VALUES (?,?,?,?,?)",(name,email,phone,address,v))
        cursor.execute("commit")
def fetchFromDb():

        nameTf.delete(0,END)
        emailTf.delete(0,END)
        phoneTf.delete(0,END)
        addressTf.delete('1.0',END)
        searchField = searchTf.get()
        l = []
        cursor.execute("SELECT name FROM details WHERE name=?",(searchField,))
        name = Label(f, font=fnt, text='Name:', bg='skyblue', width=25)
        name.place(x=650,y=115)
        row = str(cursor.fetchone())
        name['text'] = "Name:  "+row.lstrip("('").rstrip("',)")
        nameTf.insert(0,row.lstrip("('").rstrip("',)"))

        cursor.execute("SELECT email FROM details WHERE name=?",(searchField,))
        email = Label(f, font=fnt, text='Email:', bg='skyblue',width=25)
        email.place(x=650,y=145)
        row = str(cursor.fetchone())
        email['text'] = "Email:  "+row.lstrip("('").rstrip("',)")
        emailTf.insert(0,row.lstrip("('").rstrip("',)"))

        cursor.execute("SELECT phone FROM details WHERE name=?",(searchField,))
        phone = Label(f, font=fnt, text='Phone:', bg='skyblue',width=25)
        phone.place(x=650,y=175)
        row = str(cursor.fetchone())
        phone['text'] = "Phone:  "+row.lstrip("('").rstrip("',)")
        phoneTf.insert(0,row.lstrip("('").rstrip("',)"))

        cursor.execute("SELECT address FROM details WHERE name=?",(searchField,))
        address = Label(f, font=fnt, text='Address:', bg='skyblue',width=25)
        address.place(x=650,y=205)
        row = str(cursor.fetchone())
        address['text'] = "Address:  "+row.lstrip("('").rstrip("',)")
        addressTf.insert(END,row.lstrip("('").rstrip("',)"))

        cursor.execute("SELECT gender FROM details WHERE name=?",(searchField,))
        gender = Label(f, font=fnt, text='Gender:', bg='skyblue',width=25)
        gender.place(x=650,y=300)
        row = str(cursor.fetchone())
        gender['text'] = "Gender:  "+row.lstrip("('").rstrip("',)")
        
        if gender['text'] == 'Gender:  Male':
                male.select()
        elif gender['text'] == 'Gender:  Female':
                female.select()
        
        def updateToDb():        
                val = var1.get()
                if val == 1:
                        v = male["text"]
                elif val == 2:
                        v = female["text"]
                updName = str(nameTf.get())
                updEmail = str(emailTf.get())
                updPhone = str(phoneTf.get())
                updAddress = str(addressTf.get("1.0","end-1c"))
                updGender = str(v)
                cursor.execute('''UPDATE details SET name = ? ,email = ? ,phone = ? ,address = ? ,gender = ? WHERE name = ?''',(updName,updEmail,updPhone,updAddress,updGender,updName))
                cursor.execute("commit")
                
                
        #update button
        update=Button(f,text="Update",width=12,height=-5,bg='grey',activebackground='white',font=fnt,command=updateToDb)
        update.place(x=400,y=380)
def clearAll():
        nameTf.delete(0,END)
        emailTf.delete(0,END)
        phoneTf.delete(0,END)
        addressTf.delete('1.0',END)
        searchTf.delete(0,END)
#clear button
clear=Button(f,text="Clear Fields",width=12,height=-5,bg='grey',activebackground='white',font=fnt,command=clearAll)
clear.place(x=200,y=450)
#submit button
submit=Button(f,text="Submit",width=12,height=-5,bg='grey',activebackground='white',font=fnt,command=insertIntoDb)
submit.place(x=200,y=380)
#searchBtn
searchbtn = Button(f,text='Search',width=8,height=-5,bg='grey',activebackground='white',font=fnt,command=fetchFromDb)
searchbtn.place(x=650,y=55)

root.mainloop()
