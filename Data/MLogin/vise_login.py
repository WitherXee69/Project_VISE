import os

from Data.Imports.local_imports import *
from Data.Speak_All.speak_print_only import speak
#from Data.EnImp.Enc import encrypt_files


def login_main():
    root = Tk()
    root.title("#_Vise_Login_#")

    leb_name = Label(text='Username')
    leb_pass = Label(text='Password')

    get_name = Entry(root)
    get_password = Entry(root, show="*")

    def close_tk():
        root.quit()
        root.destroy()

    def save():
        os.chdir("D:\Python_Projects\Project_Vise")
        name = get_name.get()
        passw = get_password.get()
        filep = open(rf"{os.getcwd()}\User_credentials\user_pass.elx", "w")
        filep.write(passw)
        filep.close()
        filen = open(rf"{os.getcwd()}\User_credentials\username.elx", "w")
        filen.write(name)
        filen.close()
        tkinter.messagebox.showinfo("Welcome!", f"Successfully Logged in {name}!")
        speak(f"Successfully Logged in {name}!")
        encrypt_files()

        root.quit()

    btn_save = Button(root, text='Login', command=save)
    btn_close = Button(root, text='Close', command=close_tk)
    leb_name.grid(row=0, column=1)
    get_name.grid(row=0, column=2)
    leb_pass.grid(row=2, column=1)
    get_password.grid(row=2, column=2)
    btn_save.grid(row=4, column=1)
    btn_close.grid(row=4, column=2)

    root.mainloop()


if __name__ == '__main__':
    login_main()
