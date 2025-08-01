import time


def set_alarm_time():

    alarm_phrase = input("Enter phrase(eg:- 'wake me in 10/32/3 seconds/minutes/hours'): ")
    phrase_lst = alarm_phrase.split()
    #print(phrase_lst)

    if "hour" in phrase_lst or "hours" in phrase_lst:
        emphst = ""
        for ht in phrase_lst:
            if ht.isdigit():
                emphst = ht
        htosec = (int(emphst)*60)*60
        time.sleep(htosec)
        print("ring ring ring")
        print(htosec) #for debug

    elif "minute" in phrase_lst or "minutes" in phrase_lst:
        empmst = ""
        for mt in phrase_lst:
            if mt.isdigit():
                empmst = mt
        mtosec = int(empmst)*60
        time.sleep(mtosec)
        print("ring ring ring")
        print(mtosec) #for debug

    elif "second" in phrase_lst or "seconds" in phrase_lst:
        empsst = ""
        for st in phrase_lst:
            if st.isdigit():
                empsst = st
        time.sleep(int(empsst))
        print("ring ring ring")
        print(empsst) #for debug



if __name__ == '__main__':
    set_alarm_time()