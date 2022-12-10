import tkinter
import mysql.connector
from tkinter import *


def reg():
    root1 = tkinter.Tk()
    root1.geometry("580x240")
    root1.title("Register")

    root1.config(background="#088a88")
    frame = tkinter.Frame(root1, background="#088a88")
    frame.pack()

    def cancale():
        root1.destroy()

    def apply():
        if entry_pass.get() == entry_cof_pass.get():
            cnx = mysql.connector.connect(
                host="localhost",
                user="root",
                password=" ",
                database="register_form",
            )

            cursor = cnx.cursor()

            create_table_query = """
                CREATE TABLE IF NOT EXISTS users (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    first_name VARCHAR(255) NOT NULL,
                    second_name VARCHAR(255),
                    last_name VARCHAR(255) NOT NULL,
                    username VARCHAR(255) NOT NULL UNIQUE,
                    email VARCHAR(255) NOT NULL UNIQUE,
                    phone VARCHAR(255) NOT NULL UNIQUE,
                    password VARCHAR(255) NOT NULL
                )
            """

            cursor.execute(create_table_query)
            insert_query = """
                INSERT INTO users (first_name, second_name, last_name, username, email, phone, password)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """

            cursor.execute(
                insert_query,
                (
                    entry_first_name.get(),
                    entry_second_name.get(),
                    entry_last_name.get(),
                    entry_user_name.get(),
                    entry_email.get(),
                    entry_phone.get(),
                    entry_pass.get(),
                ),
            )

            cnx.commit()

            cursor.close()
            cnx.close()
            root1.destroy()
        else:
            tkinter.messagebox.showerror(
                "Error", "Password and confirmed password do not match"
            )

    label = tkinter.Label(
        frame,
        text="Register",
        background="#088a88",
        foreground="white",
        font=("Arial", 19),
    )
    label.grid(row=0, column=1)

    label_first_name = tkinter.Label(
        frame,
        text="First name",
        background="#088a88",
        foreground="white",
        font=("Arial", 10),
    )
    label_first_name.grid(row=1, column=0)
    entry_first_name = tkinter.Entry(frame, font=("Arial", 10))
    entry_first_name.grid(row=2, column=0, padx=20)

    label_second_name = tkinter.Label(
        frame,
        text="Second name",
        background="#088a88",
        foreground="white",
        font=("Arial", 10),
    )
    label_second_name.grid(row=1, column=1)
    entry_second_name = tkinter.Entry(frame, font=("Arial", 10))
    entry_second_name.grid(row=2, column=1, padx=20)

    label_last_name = tkinter.Label(
        frame,
        text="Last name",
        background="#088a88",
        foreground="white",
        font=("Arial", 10),
    )
    label_last_name.grid(row=1, column=2)
    entry_last_name = tkinter.Entry(frame, font=("Arial", 10))
    entry_last_name.grid(row=2, column=2, padx=20)

    label_user_name = tkinter.Label(
        frame,
        text="User name",
        background="#088a88",
        foreground="white",
        font=("Arial", 10),
    )
    label_user_name.grid(row=3, column=0)
    entry_user_name = tkinter.Entry(frame, font=("Arial", 10))
    entry_user_name.grid(row=4, column=0, padx=20)

    label_email = tkinter.Label(
        frame,
        text="Email",
        background="#088a88",
        foreground="white",
        font=("Arial", 10),
    )
    label_email.grid(row=3, column=1)
    entry_email = tkinter.Entry(frame, font=("Arial", 10))
    entry_email.grid(row=4, column=1, padx=20)

    label_phone = tkinter.Label(
        frame,
        text="Phone",
        background="#088a88",
        foreground="white",
        font=("Arial", 10),
    )
    label_phone.grid(row=3, column=2)
    entry_phone = tkinter.Entry(frame, font=("Arial", 10))
    entry_phone.grid(row=4, column=2, padx=20)

    label_pass = tkinter.Label(
        frame,
        text="Password:",
        background="#088a88",
        foreground="white",
        font=("Arial", 10),
    )
    label_pass.grid(row=5, column=0)
    entry_pass = tkinter.Entry(frame, show="*", font=("Arial", 10))
    entry_pass.grid(row=6, column=0, padx=20)

    label_cof_pass = tkinter.Label(
        frame,
        text="Confirme password:",
        background="#088a88",
        foreground="white",
        font=("Arial", 10),
    )
    label_cof_pass.grid(row=7, column=0)
    entry_cof_pass = tkinter.Entry(frame, show="*", font=("Arial", 10))
    entry_cof_pass.grid(row=8, column=0, padx=20)

    butt_next = tkinter.Button(
        frame,
        text="Apply",
        background="white",
        fg="#088a88",
        font=("Arial", 10),
        width=20,
        command=apply,
    )
    butt_next.grid(row=8, column=2)

    butt_cancale = tkinter.Button(
        frame,
        text="Cancale",
        background="white",
        fg="#088a88",
        font=("Arial", 10),
        width=20,
        command=cancale,
    )
    butt_cancale.grid(row=8, column=1)

    root1.mainloop()
