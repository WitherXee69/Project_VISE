import os
from os import scandir
import getpass
import socket
import wget
from wget import *
import sys
from tqdm import tqdm
import time
import shutil
from pathlib import Path
from datetime import datetime


def loading():
    for i in tqdm(range(100),
                  desc="Loading…",
                  ascii=False, ncols=75):
        time.sleep(0.01)
    print("Completed!\n")
    time.sleep(2)


def message(string):
    for i in string:
        print(i, end="")

        time.sleep(0.5)


main_dir = f"C:\\Users\\{getpass.getuser()}\\Desktop\\LEOS\\{socket.gethostname()}\\{getpass.getuser()}"
main_dir1 = "root"
progfile_dir = f"{main_dir}\\ProgramFiles"
mainuser_dir = f"{main_dir}\\UserFiles"
home_dir = f"{mainuser_dir}\\Home"
docu_dir = f"{mainuser_dir}\\Document"
down_dir = f"{mainuser_dir}\\Downloads"
pics_dir = f"{mainuser_dir}\\Images"
music_dir = f"{mainuser_dir}\\Music"

showpath = f""

username = f"{progfile_dir}\\username.king"
password = f"{progfile_dir}\\password.king"


def login():
    os.chdir(main_dir)
    file_exist_user = open(f"{progfile_dir}\\username.king", "r", encoding="utf8")
    file_exist_pass = open(f"{progfile_dir}\\password.king", "r", encoding="utf8")

    log_name = file_exist_user.read()
    log_pass = file_exist_pass.read()

    user_name = input("enter your username for login: ")
    user_pass = input("enter your password for login: ")

    if (user_name == log_name) and (user_pass == log_pass):
        msg_access = "Access granted......."
        message(msg_access)
        time.sleep(1)
        name = log_name.capitalize()
        print(f"Welcome {name}")
        while True:
            cmd()
    else:
        print("please enter right username or password\n")
        login()


def myCommand():
    os.chdir(main_dir)
    try:
        if os.path.exists(username) and os.path.exists(password):
            filwuname = open(username, "r")
            uname = filwuname.read()
            query = input(f"\n<{uname}@localhost><{os.getcwd()}>>>")
        else:
            print("Run Installer for show username.....")
            query = input(f"\n<{getpass.getuser()}@localhost><>>>")
    except None:
        print("input cmd correctly")
    return query


def cmd():
    os.chdir(main_dir)
    global del_enter
    query = myCommand()
    query = query.lower()

    if "gdir" in query:
        try:
            print("Welcome to Change directory module")
            query = input("Enter dir: ")
            os.chdir(query)
            print(f"Changed main dir to {os.getcwd()}")
        except FileNotFoundError:
            print("Please check input file is not found!!!")
            cmd()

    elif query == "lst":
        entries1 = os.listdir(os.getcwd())
        for entry1 in entries1:
            if entry1 is None:
                print("This folder is empty")
            else:
                listdirsize = os.path.getsize(entry1)
                print(f"{entry1}\t\t Size:{listdirsize}")

    elif "shutdown" in query:
        print("Shutting Down LEOS......")
        sys.exit()

    elif query == "lst -d":
        def convert_date(timestamp):
            d = datetime.utcfromtimestamp(timestamp)
            formated_date = d.strftime('%d %b %Y')
            return formated_date

        dir_entries = scandir(os.getcwd())
        for entry in dir_entries:
            info = entry.stat()
            print(f'{entry.name}\t\t Last Modified: {convert_date(info.st_mtime)}')

    elif query == "lst -all":
        path = os.getcwd()
        file_list = []

        for path, folders, files in os.walk(path):
            for file in files:
                file_list.append(os.path.join(path, file))

        for filename in file_list:
            print(f"{filename}\n")

    elif query == "mkdir":
        query = input("Enter new DIR name: ")
        p = Path(f'{query}')
        p.mkdir(exist_ok=True)

    elif query == "delf":
        print(f"Here is the files and folders in '{os.getcwd()}' with modified dates:->>>")

        def convert_date(timestamp):
            d = datetime.utcfromtimestamp(timestamp)
            formated_date = d.strftime('%d %b %Y')
            return formated_date

        dir_entries = scandir(os.getcwd())
        for entry in dir_entries:
            info = entry.stat()
            print(f'{entry.name}\t\t Last Modified: {convert_date(info.st_mtime)}')

        try:
            del_enter = input("\nEnter file or folder name to delete: ")
            os.rmdir(del_enter)
            loading()
            print(f"Successfully deleted '{del_enter}' folder")
        except NotADirectoryError:
            os.remove(del_enter)
            loading()
            print(f"Successfully deleted '{del_enter}' file")

    elif query == "fcopy -s":
        source = input("Enter Source place: ")
        query = input("Enter Destination place: ")
        shutil.move(source, query)
        print(f"\nSuccessfully move '{source} to '{query}'")

    elif query == "fcopy -full":
        source = input("Enter Source place: ")
        query = input("Enter Destination place: ")
        shutil.move(source, query, copy_function=shutil.copytree)
        print(f"\nSuccessfully moved all files in '{source} folder to '{query}'")

    elif query == "rename":
        filerename = input("Enter file for rename: ")
        newname = input("Enter new name: ")
        os.rename(filerename, newname)
        print(f"\nSuccessfully renamed '{filerename}' to '{newname}'")

    elif query == "netdow":
        def bar_progress(current, total, width=80):
            progress_message = "Downloading: %d%% [%d / %d] bytes" % (current / total * 100, current, total)
            # Don't use print() as it will print in new line every time.
            sys.stdout.write("\r" + progress_message)
            sys.stdout.flush()

        url1 = input("Enter URL for download: ")
        try:
            wget.download(url=url1, out=down_dir, bar=bar_progress)
            print(f"\nSuccessfully downloaded into '{down_dir}'")
        except ConnectionAbortedError or ConnectionError or ConnectionRefusedError or ConnectionResetError:
            print("Please check your internet connection and try again")
            cmd()

    # elif query == "ext":
    elif query == "root":
        print(f"Your main path is {main_dir}")

    elif query == "gdir--root":
        msg = "Working on it......"
        message(msg)
        os.chdir(main_dir)
        print(f"Successfully DIR changed to {os.getcwd()}")


if __name__ == '__main__':
    import os
    import random
    import socket
    import getpass
    from tqdm import tqdm
    import time


    def loading_mk():
        pbar = tqdm(total=100, desc="Making Files.....", ascii=False, ncols=75)
        for i in range(10):
            time.sleep(0.1)
            pbar.update(10)
        pbar.close()
        time.sleep(3)


    def loading_fin():
        pbar = tqdm(total=100, desc="Finalizing.....…", ascii=False, ncols=75)
        for i in range(10):
            time.sleep(0.1)
            pbar.update(10)
        pbar.close()
        time.sleep(2)
        print("Completed!\n")
        time.sleep(3)


    main_dir = rf"C:\Users\{getpass.getuser()}\Desktop\LEOS\{socket.gethostname()}\{getpass.getuser()}"
    progfile_dir = f"{main_dir}\\ProgramFiles"
    mainuser_dir = f"{main_dir}\\UserFiles"
    home_dir = f"{mainuser_dir}\\Home"
    docu_dir = f"{mainuser_dir}\\Document"
    down_dir = f"{mainuser_dir}\\Downloads"
    pics_dir = f"{mainuser_dir}\\Images"
    music_dir = f"{mainuser_dir}\\Music"

    unaname = f"{progfile_dir}\\username.king"
    passwd = f"{progfile_dir}\\password.king"

    if os.path.exists(main_dir) and os.path.exists(mainuser_dir) and os.path.exists(home_dir) and os.path.exists(
            docu_dir) and os.path.exists(down_dir) and os.path.exists(pics_dir) and os.path.exists(
        music_dir) and os.path.exists(unaname) and os.path.exists(passwd):
        print("All files are exists.")
        print("Running System......")
        import time

        pbar = tqdm(total=100, desc="Starting.....", ascii=False, ncols=75)
        for i in range(10):
            time.sleep(0.1)
            pbar.update(10)
        pbar.close()
        while True:
            login()
    else:
        print("Making MAIN Dir......\n")
        os.makedirs(main_dir, exist_ok=True)
        time.sleep(3)
        loading_mk()
        loading_fin()

        print("Making PROGRAM FILES Dir......\n")
        os.makedirs(progfile_dir, exist_ok=True)
        time.sleep(3)
        loading_mk()
        loading_fin()

        print("Making MAIN USER Dir......\n")
        os.makedirs(mainuser_dir, exist_ok=True)
        time.sleep(3)
        loading_mk()
        loading_fin()

        print("Making HOME Dir......\n")
        os.makedirs(home_dir, exist_ok=True)
        time.sleep(3)
        loading_mk()
        loading_fin()

        print("Making DOCUMENT Dir......\n")
        os.makedirs(docu_dir, exist_ok=True)
        time.sleep(3)
        loading_mk()
        loading_fin()

        print("Making DOWNLOADS Dir......\n")
        os.makedirs(down_dir, exist_ok=True)
        time.sleep(3)
        loading_mk()
        loading_fin()

        print("Making IMAGES Dir......\n")
        os.makedirs(pics_dir, exist_ok=True)
        time.sleep(3)
        loading_mk()
        loading_fin()

        print("Making MUSIC Dir......\n")
        os.makedirs(music_dir, exist_ok=True)
        time.sleep(3)
        loading_mk()
        loading_fin()

        print("FINISHING INSTALL......\n")
        time.sleep(3)
        loading_fin()

        print("Finished")
        time.sleep(2)

        username = input("Enter your username: ")
        passwrd = input("Enter your Password: ")

        with open(f"{progfile_dir}\\username.king", "w", encoding="utf8") as filwuname:
            filwuname.write(username)
        with open(f"{progfile_dir}\\password.king", "w", encoding="utf8") as filwpass:
            filwpass.write(passwrd)

        name = username.capitalize()

        diro = rf"C:\Users\{getpass.getuser()}\Desktop\LEOS\{socket.gethostname()}"
        os.chdir(diro)

        # os.rename(main_dir, rf"C:\Users\acer\Desktop\Knight_OS\{socket.gethostname()}\{name}")

        print(f"Congratulations {name}!!!. LEOS is now working!!!!")
        filwuname.close()
        filwpass.close()
        import time

        pbar = tqdm(total=100, desc="Starting.....", ascii=False, ncols=75)
        for i in range(10):
            time.sleep(0.1)
            pbar.update(10)
        pbar.close()
        while True:
            login()
