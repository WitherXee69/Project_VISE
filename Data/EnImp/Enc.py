import os

from Data.Imports.local_imports import *
from Data.Imports.global_imports import *
from Data.Speak_All.speak_print_only import speak
from Data.MLogin.vise_login import login_main

user = fr"{os.getcwd()}\User_credentials\en\do\not\even\try\to\access\to\me\because\i\am\encrypted\and\good\bye\fileuser.ekey"
passwrd = fr"{os.getcwd()}\User_credentials\en\do\not\even\try\to\access\to\me\because\i\am\encrypted\and\good\bye\filepass.ekey"
#open(user)
#open(passwrd)
#os.chdir("E:\Python_Projects\Project_Vise")
#os.makedirs(fr"{os.getcwd()}\User_credentials\en")
os.makedirs(fr"{os.getcwd()}\User_credentials\en\do\not\even\try\to\access\to\me\because\i\am\encrypted\and\good\bye", exist_ok=True)


# open(r"\User_credentials\")

def encrypt_files():
    # open("username.elx")
    # open("user_pass.elx")
    os.chdir("D:\Python_Projects\Project_Vise")
    username_credit = fr"{os.getcwd()}\User_credentials\username.vic"
    passwrd_credit = fr"{os.getcwd()}\User_credentials\user_pass.vic"

    keyuser = Fernet.generate_key()
    keypass = Fernet.generate_key()

    with open(
            rf'{os.getcwd()}\User_credentials\en\do\not\even\try\to\access\to\me\because\i\am\encrypted\and\good\bye\fileuser.ekey',
            'wb') as filekeyu:
        filekeyu.write(keyuser)

    with open(
            rf'{os.getcwd()}\User_credentials\en\do\not\even\try\to\access\to\me\because\i\am\encrypted\and\good\bye\filepass.ekey',
            'wb') as filekeyp:
        filekeyp.write(keypass)

    with open(
            rf'{os.getcwd()}\User_credentials\en\do\not\even\try\to\access\to\me\because\i\am\encrypted\and\good\bye\fileuser.ekey',
            'rb') as fileuser:
        keyuser = fileuser.read()

    fernetu = Fernet(keyuser)
    with open(username_credit, 'rb') as origuser:
        originalu = origuser.read()

    encrypted = fernetu.encrypt(originalu)

    with open(username_credit, 'wb') as encrypted_fileu:
        encrypted_fileu.write(encrypted)

    with open(
            rf'{os.getcwd()}\User_credentials\en\do\not\even\try\to\access\to\me\because\i\am\encrypted\and\good\bye\filepass.ekey',
            'rb') as filepass:
        keypass = filepass.read()

    fernetp = Fernet(keypass)
    with open(passwrd_credit, 'rb') as origuserpass:
        originalp = origuserpass.read()

    encryptedp = fernetp.encrypt(originalp)

    with open(passwrd_credit, 'wb') as encrypted_filep:
        encrypted_filep.write(encryptedp)


def maind():
    username_credit = fr"{os.getcwd()}\User_credentials\username.vic"
    passwrd_credit = fr"{os.getcwd()}\User_credentials\user_pass.vic"
    if not os.path.exists(username_credit) and os.path.exists(passwrd_credit):
        login_main()

    else:
        speak("All Settled UP!")


if __name__ == '__main__':

    passkey = fr'{os.getcwd()}\User_credentials\en\do\not\even\try\to\access\to\me\because\i\am\encrypted\and\good\
    \bye\filepass.ekey '
    userkey = fr'{os.getcwd()}\User_credentials\en\do\not\even\try\to\access\to\me\because\i\am\encrypted\and\good\
    \bye\fileuser.ekey '

    time_mod_pass = os.path.getctime(passkey)
    time_mod_user = os.path.getctime(userkey)

    pass_time = time.ctime(time_mod_pass)
    user_time = time.ctime(time_mod_user)

    latest_date = datetime.date.today()

    if user_time == latest_date and pass_time == latest_date:
        encrypt_files()
        maind()

    else:
        maind()
