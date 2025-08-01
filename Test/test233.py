from Data.Imports.local_imports import *
import threading


# face_reg()
def test():
    #backfunc = threading.Thread(target=face_reg, )
    #backfunc.start()
    face_reg()
    name = face_reg()
    print(str(name))


test()
