import os
import time
from tkinter import *
from Data.Imports.global_imports import *


def errorin_pro(apptitle):
    rootv = Tk()
    rootv.geometry("340x50")
    rootv.maxsize(340, 50)
    rootv.minsize(340, 50)
    rootv.title(apptitle)
    vinput_lab = Label(text="Command---->>>")
    ventry_sec = Entry(rootv)

    def cmd_btn_enter():
        os.chdir("E:\Python_Projects\Project_Vise")
        loc = rf"{os.getcwd()}\Data\Files\deadtemp"
        entry = ventry_sec.get()
        tempfiled = rf"{loc}\datatemp_query.vitemp"
        # open(tempfiled)
        file = open(tempfiled, 'w')
        file.write(entry)
        file.close()
        rootv.quit()
        rootv.destroy()
        # print("Successe!")

    venter_btn = Button(rootv, text="Enter Command", command=cmd_btn_enter)

    vinput_lab.grid(row=1, column=2)
    venter_btn.grid(row=4, column=4)
    ventry_sec.grid(row=1, column=3)

    rootv.mainloop()


if __name__ == '__main__':
    errorin_pro(apptitle="new")
