from tkinter import *
from tkinter import messagebox
from random import choice,randint,shuffle
import pyperclip

def generate_password():
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8,10))]
    password_symbols = [choice(numbers) for _ in range(randint(2,4))]
    password_numbers = [choice(symbols)  for _ in range(randint(2, 4))]

    password_list = password_letters+password_symbols+password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)





def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website)==0 or len(password)==0:
        messagebox.showinfo(title="Oops", message="please make sure you haven't left any fields empty..... ")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \n Email:{email}"
                                                              f"\nPassword: {password}\n Is it ok to save ?")

        if is_ok:
            with open("data.txt",'a') as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0,END)
                password_entry.delete(0,END)




window = Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)
canvas = Canvas(height=500, width=500,highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(250,250,image=logo_img)
canvas.grid(row=0,column=1)

#labels
website_label = Label(text="Website")
website_label.grid(row=1,column=0)
email_label = Label(text="Email/Username")
email_label.grid(row=2,column=0)
password_label = Label(text="password")
password_label.grid(row=3,column=0)

#entry
website_entry = Entry(width=35)
website_entry.grid(row=1,column=1,columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,"Your email address")
password_entry = Entry(width=35)
password_entry.grid(row=3,column=1,columnspan=2)

#buttons
generate_password_button = Button(text="Generate Password",command=generate_password)
generate_password_button.grid(row=3,column=2)
add_button = Button(text="Add",width=33,command=save)
add_button.grid(row=4,column=1,columnspan=2)


















window.mainloop()