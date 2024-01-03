import tkinter
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import mysql.connector

#Connect ke database
mydb= mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="student_registeration_form"
)
mycursor= mydb.cursor()

# Define for calculation (Pilihan set & bilangan kuantiti)
def collect_data():
    
    #  put the info in terminal
    student_full_name=student_full_name_entry.get()
    print("student full name:", student_full_name)

    student_year=student_year_spinbox.get()
    print("student year:", student_year)

    student_adress=student_student_adress.get()
    print("student adress:", student_adress)

    student_gender=student_gender_combobox.get()
    print("student gender:", student_gender)

    parent_full_name=parent_full_name_entry.get()
    print("parent full name:", parent_full_name)

    parent_email=parent_email_entry.get()
    print("parent email:", parent_email)

    student_set=student_set_combobox.get()
    print("student set:", student_set)

    student_pack_quantity=student_pack_quantity_entry.get()
    print("student pack quantity:", student_pack_quantity)

    

    set_type = student_set_combobox.get()
    quantity = int(student_pack_quantity_entry.get())
    
    #  the price below is to defined the value from your selections
    prices = {"Set 1": 6, "Set 2": 10, "Set 3": 15}

     # Calculate the total price. This will be derived from your selection (Package, Pack).
    total_price = (prices[set_type] * quantity)

    # To Print total harga.
    #It will happen in the function collect_data().
    #The f before the string indicates an f-string in Python. 
    output_label.config(bg='#f0ead2', fg="#31572c", width=100, font= ("Impact", 15), text=f"Set: {set_type}, Pax: {quantity}, Total Price: RM{total_price}\nTHANK YOU")
   
    #Inserting data into a table
    sql = "INSERT INTO sarikei (student_full_name, student_year, student_adress, student_gender, parent_full_name, parent_email, student_set, student_pack_quantity) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    val = (student_full_name, student_year, student_adress, student_gender, parent_full_name, parent_email, student_set, student_pack_quantity)
    mycursor.execute(sql,val)
    mydb.commit()


##########################################################################################################
#MY GUI TITLE
root = tk.Tk()
root["bg"]="#adc178"
root.title("Student Registeration Form")
root.geometry('1080x1080')

#TITLE IN GUI/FORM-----------------------
label = tk.Label(root, bg= "#d9ed92", fg="#31572c", text="WELCOME TO SK SARIKEI", font=('Cooper Black',18))
label.pack(padx=20, pady=20)

# Saving user info (4 attributes in 1 frame)
frame = tk.Frame(root)
frame.pack()

#Frame 1 (STUDENT INFO)------------------------------------------------------------------------------
student_info_frame =tkinter.LabelFrame(frame, bg= "#dde5b6",text="Student Information")
student_info_frame.grid(row= 0, column=0, padx=20, pady=0)

#Full name
student_full_name = tkinter.Label(student_info_frame, bg= "#f0ead2", width=10, font= ("Times New Roman", 10), text="Full Name")
student_full_name.grid(row=0, column=0)
student_full_name_entry = tkinter.Entry(student_info_frame)
student_full_name_entry.grid(row=1, column=0)

#Year
student_year = tkinter.Label(student_info_frame, bg= "#f0ead2", width=10, font= ("Times New Roman", 10), text="Year")
student_year.grid(row=0, column=1)
student_year_spinbox = tkinter.Spinbox(student_info_frame, from_=1, to=6)
student_year_spinbox.grid(row=1, column=1)

#Student Adress
student_adress = tkinter.Label(student_info_frame, bg= "#f0ead2", width=15, font= ("Times New Roman", 10), text="Student Adress")
student_adress.grid(row=2, column=0)
student_student_adress = tkinter.Entry(student_info_frame)
student_student_adress.grid(row=3, column=0)

#Gender
student_gender = tkinter.Label (student_info_frame, bg= "#f0ead2", width=10, font= ("Times New Roman", 10), text="Gender")
student_gender.grid(row=2, column=1)
student_gender_combobox= ttk.Combobox (student_info_frame, values=["Male", "Female"])
student_gender_combobox.grid(row=3, column=1)

#Jarak attributes dgn frame 1
for widget in student_info_frame.winfo_children():
    widget.grid_configure(padx=60, pady=5)


#Frame 2 (FATHER/MOTHER/GUARDIAN INFO)---------------------------------------------------------------
parent_info_frame =tkinter.LabelFrame(frame, bg= "#dde5b6", text="Father/ Mother/ Guardian Information")
parent_info_frame.grid(row= 0, column=1, padx=20, pady=0)

#Full name Parents
parent_full_name = tkinter.Label(parent_info_frame, bg= "#f0ead2", width=10, font= ("Times New Roman", 10), text="Full Name")
parent_full_name.grid(row=0, column=0)
parent_full_name_entry = tkinter.Entry(parent_info_frame)
parent_full_name_entry.grid(row=1, column=0)

#Email
parent_email = tk.Label(parent_info_frame, bg= "#f0ead2", width=10, font= ("Times New Roman", 10), text="Email")
parent_email.grid(row=0, column=1)
parent_email_entry = tk.Entry(parent_info_frame)
parent_email_entry.grid(row=1, column=1)

#Jarak attributes dgn frame 2
for widget in parent_info_frame.winfo_children():
    widget.grid_configure(padx=60, pady=20)

#Frame 3 (Stationery package)------------------------------------------------------------------------
stat_pack_frame =tkinter.LabelFrame(frame, bg= "#dde5b6", text="Stationary Package To Buy")
stat_pack_frame.grid(row= 1, column=0, padx=20, pady=10)

# Prices List by using textbox
prices_text = tk.Text(stat_pack_frame, bg="#f0ead2", fg='#31572c', height=15, width=45, font= ("Cooper Black", 10))

# The defined list by using pricebox
prices_text.insert(tk.END, "Set 1:\nPencil (Set),\nEraser (Set),\nRuler\nRM 6.00\n\n")
prices_text.insert(tk.END, "Set 2:\nPencil (Set),\n5 writing books\nRM 10.00\n\n")
prices_text.insert(tk.END, "Set 3:\nPencil (Set),\nEraser (Set),\nRuler,\n5 writing books\nRM 15.00")
prices_text.configure(state='disabled')
prices_text.grid(padx=70, pady=0)


#Frame 4 (Select n pay)------------------------------------------------------------------------------
sp_info_frame =tkinter.LabelFrame(frame, bg= "#dde5b6", text="Select & Pay")
sp_info_frame.grid(row= 1, column=1, padx=20, pady=0)

#Set
student_set = tkinter.Label (sp_info_frame, bg= "#f0ead2", width=10, font= ("Times New Roman", 10), text="Set")
student_set.grid(row=0, column=0)
student_set_combobox= ttk.Combobox (sp_info_frame, values=["Set 1", "Set 2", "Set 3"])
student_set_combobox.grid(row=0, column=1)

#Quantity
student_pack_quantity = tk.Label(sp_info_frame, bg= "#f0ead2", width=10, font= ("Times New Roman", 10), text="Quantity / Pax")
student_pack_quantity.grid(row=1, column=0)
student_pack_quantity_entry = tk.Entry(sp_info_frame)
student_pack_quantity_entry.grid(row=1, column=1)

#Jarak attributes dgn frame 4
for widget in sp_info_frame.winfo_children():
    widget.grid_configure(padx=70, pady=45)

#Button for BUY
save_button = tk.Button(root, bg= "#d9ed92", text="Submit Data", font= ("Times New Roman", 15), command=collect_data)
save_button.pack(pady=5)

# Print Output & result
label = tk.Label(root, bg= "#d9ed92", text='Payment Details:', font=("Times New Roman",15))
label.pack(ipadx=10, ipady=10)
output_label = tk.Label(root, text="")
output_label.pack()


root.mainloop()

