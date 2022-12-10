import tkinter
from tkinter import messagebox
from Register import reg


root = tkinter.Tk()
root.geometry("280x340")
root.title("System")
root.config(background="#088a88")


def login():
    username = "asdasd"
    password = "1234"
    if entry_user.get() == username and entry_pass.get() == password:
        messagebox.showinfo(title="Login Success", message="You are logged in")
    else:
        messagebox.showerror(title="Login Error", message="Invalid info")


frame = tkinter.Frame(background="#088a88")

label = tkinter.Label(
    frame, text="Login", background="#088a88", foreground="white", font=("Arial", 19)
)


label_user = tkinter.Label(
    frame,
    text="Username:",
    background="#088a88",
    foreground="white",
    font=("Arial", 10),
)
entry_user = tkinter.Entry(frame, font=("Arial", 10))
label_pass = tkinter.Label(
    frame,
    text="Password:",
    background="#088a88",
    foreground="white",
    font=("Arial", 10),
)
entry_pass = tkinter.Entry(frame, show="*", font=("Arial", 10))
butt_log = tkinter.Button(
    frame,
    text="Login",
    background="white",
    fg="#088a88",
    font=("Arial", 10),
    command=login,
    width=13,
)
butt_reg = tkinter.Button(
    frame,
    text="Register",
    background="white",
    fg="#088a88",
    font=("Arial", 10),
    width=13,
    command=reg,
)

label.grid(row=0, column=0, sticky="news", pady=10)
label_user.grid(row=1, column=0)
entry_user.grid(row=1, column=1, pady=15)
label_pass.grid(row=2, column=0)
entry_pass.grid(row=2, column=1, pady=15)
butt_log.grid(row=5, column=1)
butt_reg.grid(row=5, column=0)
frame.pack()
root.mainloop()
