import mysql.connector
connection=mysql.connector.connect(host="localhost",user="root",password="",database="client")

    
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
def check_user():
    exist=False
    if connection.is_connected:
        cursor=connection.cursor()
        cursor.execute("SELECT username,password from personne1")
        
        row=cursor.fetchall()
        for i in row:
            if((user_champ.get(),password_champ.get())==i):
                \
                exist=True
        
        if(exist==True):
           f.destroy()
        else:
           messagebox.showerror("Error", "This user don't exist or password is wrong!! ")
           user_champ.delete(0,'end')
           password_champ.delete(0,'end')
           user_champ.insert(0,"Username")
           password_champ.insert(0,"Password")
def forget_password(e):
        password_window=Tk()
        password_window.geometry("500x500")
        password_window.mainloop()

            
def afficher_user():
    
    Valeur1=user_champ.get()
    Valeur2=password_champ.get()
    print(f"{Valeur1} et {Valeur2}")
    
def entry_in_user(e):
    if user_champ.get() == 'Username':   
        user_champ.delete(0, 'end')

def on_leave_user(e):
    if user_champ.get() == '':
        user_champ.insert(0, 'Username')

def entry_in_password(e):
    if password_champ.get() == 'Password':   
        password_champ.delete(0, 'end')

def on_leave_password(e):
    if password_champ.get() == '':
        password_champ.insert(0, 'Password')

def login():
    print("Connexion en cours...")

f = Tk()
f.geometry("1000x500")
f.title("Fitness")
f.configure(bg="white")

image_1 = Image.open("C:\\Users\\Mohamed Sabbar\\OneDrive\\Bureau\\java programme\\FitTracker\\FitTracker\\images\\fitnees.jpg")
image_user = Image.open("C:\\Users\\Mohamed Sabbar\\OneDrive\\Bureau\\java programme\\FitTracker\\FitTracker\\images\\user.jpg")
image_password = Image.open("C:\\Users\\Mohamed Sabbar\\OneDrive\\Bureau\\password.webp")

image_1 = image_1.resize((300, 500), Image.BICUBIC)
photo_1 = ImageTk.PhotoImage(image_1)

image_user = image_user.resize((40, 40), Image.BICUBIC)
photo_2 = ImageTk.PhotoImage(image_user)

image_password = image_password.resize((25, 25), Image.BICUBIC)
photo_3 = ImageTk.PhotoImage(image_password)

label = Label(f, image=photo_1)
label.pack(side=LEFT)

Label(f, text="Sign in", bg="white", font=("Arial", 20)).pack()

Label(f, image=photo_2, bg="white").place(x=450, y=108)

user_champ = Entry(f, borderwidth=1, relief="flat",font=("Arial",18))
user_champ.insert(0,"Username")
user_champ.bind("<FocusIn>", entry_in_user)
user_champ.bind("<FocusOut>", on_leave_user)

user_champ.place(x=530, y=115)
Frame(f,bg="black",width=250,height=2).place(x=530,y=150)
Label(f, image=photo_3, bg="white").place(x=460, y=180)

password_champ = Entry(f, borderwidth=1, relief="flat", font=("Arial",18))
password_champ.insert(0,"Password")
password_champ.bind("<FocusIn>", entry_in_password)
password_champ.bind("<FocusOut>", on_leave_password)
password_champ.place(x=530, y=180)
Frame(f,bg="black",width=250,height=2).place(x=530,y=215)

# Création d'un bouton personnalisé avec une image
rounded_button_image = Image.open("C:\\Users\\Mohamed Sabbar\\OneDrive\\Bureau\\java programme\\FitTracker\\FitTracker\\images\\button.png") 
rounded_button_image = rounded_button_image.resize((150, 70), Image.BICUBIC)
rounded_button_photo = ImageTk.PhotoImage(rounded_button_image)

button_1 = Button(f, image=rounded_button_photo, borderwidth=0, bg="white", relief="sunken",command=check_user)
button_1.place(x=530, y=250)

button_2 = Label(f, text="password forget", font=("Arial", 12), bg="white", fg="blue")
button_2.place(x=530, y=350)
button_2.bind("<Button-1>",forget_password)
f.mainloop()

