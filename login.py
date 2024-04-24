from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image,ImageTk
import sqlite3

def get_connection():
    return sqlite3.connect('a.db')

def create_table():
    connection = get_connection()
    cursor = connection.cursor()

    # SQL query to create the table
    create_table_query = """
    CREATE TABLE IF NOT EXISTS employees (
        employeeid INTEGER NOT NULL,
        last_name text NOT NULL,
        first_name text NOT NULL,
        position text NOT NULL,
        department text NOT NULL,
        PRIMARY KEY("employeeid" AUTOINCREMENT)
    );
    
        CREATE TABLE IF NOT EXISTS user (
        userid INTEGER NOT NULL,
        username text NOT NULL,
        password text NOT NULL,
        email_id text NOT NULL,
        age text NOT NULL,
        gender text NOT NULL,            
        PRIMARY KEY("userid" AUTOINCREMENT)
    );

    CREATE TABLE IF NOT EXISTS patients (
        patientid INTEGER NOT NULL,
        last_name text NOT NULL,
        first_name text NOT NULL,
        department text NOT NULL,
        room text NOT NULL,
        doctorid int NOT NULL,
        checkin_date text NOT NULL,
        PRIMARY KEY("patientid" AUTOINCREMENT)
    );
    """
    # execute the create table query
    try:

        cursor.executescript(create_table_query)
        connection.commit()
        print("Tables created successfully.")
    except sqlite3.Error as err:
        print(f"Error creating tables: {err}")

    connection.close()
    
create_table()    

    
def image_resize(event):
    global background_image, resized, background_image2
    background_image = Image.open("document (5).jpeg")
    resized = background_image.resize((event.width, event.height), Image.LANCZOS)

    background_image2 = ImageTk.PhotoImage(resized)
    canvas.create_image(0, 0, image=background_image2, anchor="nw")
page = Tk()
page.title("LOGIN PAGE")
page.geometry("1350x700+0+0")
page.title("Swastha ".center(20))
####background image
image=Image.open('document (5).jpeg')
photo=ImageTk.PhotoImage(image)
canvas = Canvas(page, width=700, height=800)
canvas.pack(fill=BOTH, expand=YES)
canvas.create_image(0, 0, anchor=NW, image=photo, tags="background")

# Bind the <Configure> event to the image_resize function
canvas.bind("<Configure>", image_resize)


frame_m = Frame(page, bg='lightblue')
frame_m.place(relx=0.3, rely=0.3, width=650, height=400)

title = Label(frame_m, text='PLEASE LOGIN', font=('times new roman', 17, 'bold'), bg='lightblue', fg='red')
title.place(relx=0.5, rely=0.05, anchor='n')






###username and password in frame
username_label = Label(frame_m, text="Username:",font=('times new roman',14,'bold'),bg='lightblue')
username_label.place(x=90,y=100)
username_entry = Entry(frame_m,font=('times new roman',12),bg='lightgray')
username_entry.place(x=90,y=140,width=180)

password_label = Label(frame_m, text="Password:",font=('times new roman',14,'bold'),bg='lightblue')
password_label.place(x=360,y=100)
password_entry = Entry(frame_m, show="*",font=('times new roman',12),bg='lightgray')
password_entry.place(x=360,y=140,width=180)

def addUserToTable(username,emailId,password,age,gender):    ####kina email id pani rakheko parameter??
  connection = get_connection()
  cursor=connection.cursor()
  cursor.execute("INSERT into user (email_id,username,password,age,gender) values (?,?,?,?,?)",[emailId,username,password,age,gender])
  connection.commit()
  cursor.close()


def loginUser(username, password):
  connection = get_connection()
  cursor=connection.cursor()
  cursor.execute("SELECT * from user WHERE username = ? and password = ?",[username,password])
  data = cursor.fetchone()  
  if(data == None):
    messagebox.showerror(message="User Not found")
  else:
    messagebox.showinfo(message="LOGIN Success")   
    page.destroy()
    import main
    
    




#####REGISTRATION####
def register():
  # def onRegister():
  #     reg.destroy()
    reg = Toplevel()
    fullname_value = StringVar(reg)
    Email_value = StringVar(reg)
    Gender_value = StringVar(reg)
    Age_value = IntVar(reg)
    password_value=StringVar(reg)
    reg.title("Registration form")
    reg.geometry("400x400")
    A = Label(reg, text='PLEASE REGISTER FIRST', fg='grey', font='AERIAL')
    A.pack(side='top')

    Label(reg, text="", font="1").place(x=1, y=1)

    fullname = Label(reg, text="Enter your username")
    fullname.place(x=30, y=50)
    Email = Label(reg, text="Enter your email")
    Email.place(x=30, y=100)
    Gender = Label(reg, text="Enter your gender")
    Gender.place(x=30, y=150)
    Age = Label(reg, text="Enter your date of age")
    Age.place(x=30, y=200)
    password_r = Label(reg, text="Enter your password")
    password_r.place(x=30, y=250)

    fullname_entry = Entry(reg, textvariable=fullname_value)
    fullname_entry.place(x=180, y=50)
    Email_entry = Entry(reg, textvariable=Email_value)
    Email_entry.place(x=180, y=100)
    Gender_entry=Entry(reg,textvariable=Gender_value)
    Gender_entry.place(x=180, y=150)
    Age_entry = Entry(reg, textvariable=Age_value)
    Age_entry.place(x=180, y=200)
    password_reg= Entry(reg, textvariable=password_value)
    password_reg.place(x=180, y=250)     
    def signupuser():
      
    # enter_btn = Button(text="ENTER",command=signupuser)
    # enter_btn.place(x=220, y=300)
      addUserToTable(fullname_value.get(),Email_value.get(),password_value.get(),Age_value.get(),Gender_value.get())   ###adduserto table vanne function yaa aayera lekhyaxa why??
      messagebox.askokcancel(title="Success",message="User has been signed up succesfully")
      reg.destroy()###k garxa esle exactly
    
  
    register=Button(reg,text='REGISTER',padx=10,pady=10,command=signupuser).place(x=150,y=300) 
      #entry fields

    

login= Button(frame_m, text="LOGIN",font=('times new roman',13,'bold'), bg="lightblue",command=lambda : loginUser(username_entry.get(),password_entry.get())).place(x=275,y=200)
register= Button(frame_m, text="Registration form ",font=('times new roman',13,'bold'),bg="lightblue", command=register).pack(side='bottom',pady=80)

    


page.mainloop()