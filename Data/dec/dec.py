from Data.Imports.global_imports import *


def dec_main():
    username_credit = r"../../User_credentials/username.vic"
    passwrd_credit = r"../../User_credentials/user_pass.vic"

    with open(r'../../User_credentials/en/fileuser.ekey', 'rb') as fileuser:
        keyuser = fileuser.read()

    fernetu = Fernet(keyuser)

    with open(r'../../User_credentials/en/filepass.ekey', 'rb') as filepass:
        keypass = filepass.read()

    fernetp = Fernet(keypass)

    with open(username_credit, 'rb') as enc_fileu:
        encryptedu = enc_fileu.read()

    with open(passwrd_credit, 'rb') as enc_filep:
        encryptedp = enc_filep.read()

    decryptedu = fernetu.decrypt(encryptedu)
    decryptedp = fernetp.decrypt(encryptedp)

    with open(username_credit, 'wb') as dec_fileu:
        dec_fileu.write(decryptedu)

    with open(passwrd_credit, 'wb') as dec_filep:
        dec_filep.write(decryptedp)
