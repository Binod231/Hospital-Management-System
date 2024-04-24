import tkinter as tk
from PIL import ImageTk, Image
from all import *
# connect to database using sqlite3
connection = sqlite3.connect('a.db')




# configure main tkinter window
root = tk.Tk()
root.title("Swastha")
root.minsize(width=400, height=400)
root.geometry("600x500")

# function to resize background image
def image_resize(event):
    global background_image, resized, background_image2
    background_image = Image.open("main_bg.jpeg")
    resized = background_image.resize((event.width, event.height), Image.LANCZOS)

    background_image2 = ImageTk.PhotoImage(resized)
    canvas.create_image(0, 0, image=background_image2, anchor="nw")

# add background image to main application screen
background_image = ImageTk.PhotoImage(file="main_bg.jpeg")
canvas = tk.Canvas(root, width=700, height=800)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=background_image, anchor="nw")
canvas.bind("<Configure>", image_resize)

# root.bind("<Configure>", image_resize)


# add heading frame
headingFrame1 = tk.Frame(root, bg="blue", bd=2)
headingFrame1.place(relx=0.1, rely=0.02, relwidth=0.6, relheight=0.12)
headingLabel = tk.Label(headingFrame1, text="Welcome to Swastha\n A Hospital Management System", bg="green", fg="black", font=('Courier', 15,'bold'))
headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

# add main screen buttons
button1 = tk.Button(root, text="Check-in Patient", bg="green", fg="black",font=('Courier',10,'bold'), command=add_patient)
button1.place(relx=0.18, rely=0.2, relwidth=0.45, relheight=0.1)

button2 = tk.Button(root, text="Check-out Patient", bg="green", fg="black",font=('Courier',10,'bold'), command=delete_patient)
button2.place(relx=0.18, rely=0.3, relwidth=0.45, relheight=0.1)

button3 = tk.Button(root, text="View Patients", bg="green", fg="black",font=('Courier',10,'bold'), command=view_patients)
button3.place(relx=0.18, rely=0.4, relwidth=0.225, relheight=0.1)

button4 = tk.Button(root, text="Search Patients", bg="green", fg="black",font=('Courier',10,'bold'), command=patient_search)
button4.place(relx=0.405, rely=0.4, relwidth=0.225, relheight=0.1)

button5 = tk.Button(root, text="Add Employee", bg="green", fg="black",font=('Courier',10,'bold'),command=add_employee)
button5.place(relx=0.18, rely=0.5, relwidth=0.225, relheight=0.1)

button6 = tk.Button(root, text="Remove Employee", bg="green", fg="black",font=('Courier',10,'bold'), command=delete_employee)
button6.place(relx=0.405, rely=0.5, relwidth=0.225, relheight=0.1)

button7 = tk.Button(root, text="View Employees", bg="green", fg="black",font=('Courier',10,'bold'), command=view_employees)
button7.place(relx=0.18, rely=0.6, relwidth=0.225, relheight=0.1)

button8 = tk.Button(root, text="Search Employees", bg="green", fg="black",font=('Courier',10,'bold'),command=employee_search)
button8.place(relx=0.405, rely=0.6, relwidth=0.225, relheight=0.1)

button9 = tk.Button(root, text=" Exit ", bg="red", fg="black",font=('Courier',10,'bold'), command=root.destroy)
button9.place(relx=0.18, rely=0.7, relwidth=0.45, relheight=0.1)



root.mainloop()



