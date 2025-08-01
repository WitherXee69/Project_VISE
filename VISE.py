from Data.Imports.global_imports import *
from Data.Imports.local_imports import *


def start():
    time_say()
    # weather()
    sys_status()


def begin():
    from pynput import keyboard

    def on_press(key):
        if key == (keyboard.Key.ctrl and keyboard.Key.caps_lock):
            main_data()

    def on_release(key):
        # print('combination released')
        if key == keyboard.Key.esc:
            # Stop listener
            return False

    with keyboard.Listener(
            on_press=on_press, on_release=on_release) as listener:
        listener.join()


def main_data():
    username_credit = r"../User_credentials/username.vic"
    passwrd_credit = r"../User_credentials/user_pass.vic"

    def polite_before_request():
        polite = random.choice(before_request)
        speak(polite)

    def polite_after_request():
        another_polite = random.choice(after_request)
        speak(another_polite)

    def com_voice_fail():
        voice_fail = random.choice(computer_voice_faluier)
        speak(voice_fail)

    def com_sys_fail():
        sys_fail = random.choice(computer_sys_faluier)
        speak(sys_fail)

    def polite_command():
        ask = random.choice(ask_for_command)
        speak(ask)

    def application_not():
        not_found = random.choice(app_not_found)
        speak(not_found)

    def secs2hours(secs):
        mm, ss = divmod(secs, 60)
        hh, mm = divmod(mm, 60)
        return "%dhour, %02d minute, %02s seconds" % (hh, mm, ss)

    def myCommand():
        try:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                # ding()
                print("Listening...")
                # r.pause_threshold = 1
                r.energy_threshold = 350
                r.dynamic_energy_threshold = True
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source=source, timeout=20, phrase_time_limit=50000)  # timeout=20 phrase_time_limit=5
                options = {"download_root": "Data/SR_Model/"}
                query = r.recognize_whisper(audio, model="base", load_options=options, language="en")
                # dec_main()
                # username = open(username_credit, 'rb')
                # uname = username.read()
                uname = "Admin"
                print(f'{uname}: ' + query + '\n')
                # encrypt_files()

        except sr.UnknownValueError:
            com_sys_fail()
            speak("Starting 'Error Protocol'....")
            import time
            pbar = tqdm(total=100, desc="Starting.....", ascii=False, ncols=75)
            for i in range(10):
                time.sleep(0.1)
                pbar.update(10)
            pbar.close()
            errorin_pro(apptitle="Unknown Value Error")
            filetemp = r"Data\Files\deadtemp\datatemp_query.vitemp"
            with open(filetemp, 'r') as fileinput:
                readof = fileinput.read()
            query = readof
            os.remove(filetemp)
            # query = input('UVE command: ')

        except sr.WaitTimeoutError:
            com_voice_fail()
            speak("Starting 'Error Protocol'....")
            import time
            pbar = tqdm(total=100, desc="Starting.....", ascii=False, ncols=75)
            for i in range(10):
                time.sleep(0.1)
                pbar.update(10)
            pbar.close()
            errorin_pro(apptitle="Wait Timeout Error")
            filetemp = r"Data\Files\deadtemp\datatemp_query.vitemp"
            with open(filetemp, 'r') as fileinput:
                readof = fileinput.read()
            query = readof
            os.remove(filetemp)
            # query = input('WTE command: ')

        except sr.RequestError:
            com_voice_fail()
            speak("Starting 'Error Protocol'....")
            import time
            pbar = tqdm(total=100, desc="Starting.....", ascii=False, ncols=75)
            for i in range(10):
                time.sleep(0.1)
                pbar.update(10)
            pbar.close()
            errorin_pro(apptitle="Request Error")
            filetemp = r"Data\Files\deadtemp\datatemp_query.vitemp"
            with open(filetemp, 'r') as fileinput:
                readof = fileinput.read()
            query = readof
            os.remove(filetemp)
            # query = input('RE command: ')

        except TimeoutError:
            speak(
                "Please check your internet connection sir. Without internet i have few tasks to run ! ")
            speak("Added background task: Waiting for connection.....")

        return query

    query = myCommand()
    query = query.lower()
    query_lst = query.split()

    def say_sorry():
        if ((
                    "it" in query_lst or "that" in query_lst or "this" in query_lst) and "is" in query_lst and "not" in query_lst and "my" in query_lst and "command" in query_lst) or (
                (
                        "it" in query_lst or "that" in query_lst or "this" in query_lst) and "is" in query_lst and "not" in query_lst and "command" in query_lst):
            sorry()

    # 'show weather information' in query
    if ("show" in query_lst and "weather" in query_lst and ("information" in query_lst or "info" in query_lst)) or (
            "how" in query_lst and "is" in query_lst and "weather" in query_lst):
        webbrowser.open_new_tab(weather_url)
        polite_after_request()

    elif 'open youtube' in query:
        polite_before_request()
        webbrowser.open('www.youtube.com')
        polite_after_request()

    # 'check corona updates' in query
    elif "check" in query_lst and ("corona" in query_lst or "coronavirus" in query_lst or "covid19" in query_lst) and (
            "updates" in query_lst or "Data" in query_lst or "update" in query_lst):
        import time
        covidData = None
        try:
            speak('Input your country name')
            cname = input("Input your country name:")
            covidData = requests.get(covid_data_url + cname)

        except:
            speak("check your internet connection sir. ")

        if covidData is not None:
            data = covidData.json()

            while True:
                notification.notify(
                    title=f"COVID19 Stats of {cname} on {datetime.date.today()}",
                    message="Total cases : {totalcases}\nToday cases : {todaycases}\nToday deaths :{todaydeaths}\nTotal active :{active}\nTotal Deaths :{deaths}".format(
                        totalcases=data['cases'],
                        todaycases=data['todayCases'],
                        todaydeaths=data['todayDeaths'],
                        active=data["active"],
                        deaths=data["deaths"]),
                    timeout=1000
                )
                time.sleep(60 * 60 * 4)

    elif 'open chrome' in query:
        polite_before_request()
        subprocess.call(r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
        polite_after_request()
        speak('Next Command! Boss!')

    elif 'open google' in query:
        polite_before_request()
        webbrowser.open('www.google.com')
        #speak(f'Next Command! {str(facer.id)}!')

    elif 'open gmail' in query:
        polite_before_request()
        webbrowser.open('www.gmail.com')
        speak('Next Command! Boss!')

    elif 'open facebook' in query:
        polite_before_request()
        webbrowser.open('www.facebook.com')
        speak(f'Next Command! Boss!')

    elif 'open twitter' in query:
        polite_before_request()
        webbrowser.open('www.twitter.com')
        speak('Next Command! Boss!')

    # 'show saved wifi passwords' in query
    elif ("show" in query_lst and "saved" in query_lst and "wifi" in query_lst and (
            "passwords" in query_lst or "password" in query_lst)) or (
            "saved" in query_lst and ("password" in query_lst or "passwords" in query_lst) and "please" in query_lst):
        polite_before_request()
        p = subprocess.Popen(["powershell.exe",
                              "C:\\Users\\acer\\Desktop\\password.ps1"],
                             stdout=sys.stdout)
        p.communicate()
        speak(f'Here you go sir. Anything else?')

    elif 'open yahoo' in query:
        polite_before_request()
        webbrowser.open(yahoo_url)
        polite_after_request()

    elif 'what is uve' in query:
        speak(
            'U.V.E means Unknown Value Error. But you don\'t worry. when it comes you can type your command!')
        polite_after_request()

    elif 'what is wte' in query:
        speak(
            'W.T.E means Wait Timeout Error. When it comes you can type your command! So don\'t worry, Be happy')
        polite_after_request()

    elif 'open whatsapp' in query:
        polite_before_request()
        whatapp_path = rf'C:\Users\{getpass.getuser()}\AppData\Local\WhatsApp\WhatsApp.exe'
        if os.path.exists(whatapp_path):
            subprocess.call(
                rf'C:\Users\{getpass.getuser()}\AppData\Local\WhatsApp\WhatsApp.exe')
        else:
            speak("Sorry sir. I Couldn't find WhatsApp. I think its not installed!!!")
        polite_after_request()

    elif 'open antivirus system' in query:
        polite_before_request()
        speak('Next command boss!')

    elif 'play movie' in query:
        polite_before_request()
        webbrowser.open('D:\\Desktop\\movies')
        polite_after_request()

    elif 'access to command prompt' in query:
        polite_before_request()
        speak('i am successfully access command prompt')
        subprocess.call(r'C:\Windows\System32\cmd.exe')
        polite_after_request()

    elif 'control panel please' in query or "open control panel please" in query or "open control panel" in query:
        polite_before_request()
        try:
            subprocess.call(rf'C:\Users\{getpass.getuser()}\Desktop\Control Panel')
        except WindowsError:
            return query
        # except WinError:
        # return query
        polite_after_request()

    elif 'access to EDITH' in query:
        edith_path = r'C:\User\acer\Desktop\EDITH'
        if os.path.exists(edith_path):
            speak('collecting information.....')
            speak('This is an encrypted area fo this pc')
            speak('if you really want access I need to verify is that my boss')
            speak('Please enter the EDITH Launching Password')
            password = (input('EDITH Launching Password:- '))
            if password == '20040729':
                speak('access granted!')
                speak('Wellcome to the EDITH!')
                subprocess.call(rf'C:\User\{getpass.getuser()}\Desktop\EDITH')
                speak('Next Command! Boss!')
            else:
                speak('access denied!')
                speak(f'Sorry Boss try it later!')
                speak('Anything Else?')

        else:
            speak(f"Sorry sir.")
            application_not()
    # "play games" in query
    elif "play" in query_lst and ("games" in query_lst or "game" in query):
        main_ttt()

    # 'show battery info' in query
    elif ("show" in query_lst and "battery" in query_lst and ("info" in query_lst or "satatics" in query_lst)) or (
            "tell" in query_lst and "battery" in query_lst):
        speak('Getting information.......')
        polite_before_request()
        print(psutil.sensors_battery())
        speak('Next Command! Boss!')

    elif 'get file about me' in query:
        speak('Getting information about you...........')
        polite_before_request()
        speak('this is a summary about you!')
        path_to_name = "/Alex/Alex_AI\\"
        fileop = open(f"{path_to_name}username.txt")
        name_of_file = fileop.read()
        speak(f'your name is {name_of_file}')
        speak('Next Command! Boss!')

    elif 'import date and time' in query:
        polite_before_request()
        speak('Getting information about date and time.......')
        polite_after_request()
        now = datetime.datetime.now()
        speak(f"Current date and time is {now.strftime('%y %m %d  %H:%M:%S')}")
        speak('Next Command! Boss!')

    elif 'it is dj time' in query:
        speak('Its gonna be fun')
        polite_before_request()
        subprocess.call(r'C:\Program Files (x86)\VirtualDJ\virtualdj8.exe')
        polite_after_request()
        speak('Next Command! Boss!')

    elif 'google translator' in query:
        polite_before_request()
        webbrowser.open('www.translate.google.com')
        polite_after_request()
        speak('Next Command! Boss!')

    elif 'open rainmeter desktop' in query:
        polite_before_request()
        subprocess.call(r'C:\Program Files\Rainmeter\Rainmeter.exe')
        speak('here your smart desktop')
        speak('Next Command! Boss!')

    elif 'open kmplayer' in query:
        polite_before_request()
        subprocess.call(r'C:\Program Files (x86)\The KMPlayer\KMPlayer.exe')
        polite_after_request()
        speak('Next Command! Boss!')

    elif 'open android studio' in query:
        polite_before_request()
        subprocess.call(r'D:\Program Files\android\Android Studio\bin\studio64.exe')
        polite_after_request()
        speak('Next Command! Boss!')

    elif 'shutdown my pc' in query:
        polite_before_request()
        speak('Shutting down all the systems........')
        speak('shutting down all the sequences........')
        speak('Bye Boss, happy to help you, have a good day')
        speak('Let\'s meet again someday')
        os.system('shutdown -s')
        sys.exit()

    elif 'charge' in query:
        battery = psutil.sensors_battery()
        plugged = battery.power_plugged
        percent = int(battery.percent)
        time_left = secs2hours(battery.secsleft)
        print(percent)
        if percent < 40 and plugged == False:
            speak('sir, please connect charger because i can survive only ' + time_left)
        if percent < 40 and plugged == True:
            speak("don't worry sir, charger is connected")
        else:
            speak('sir, no need to connect the charger because i can survive ' + time_left)

    elif 'restart my pc' in query:
        polite_before_request()
        speak('Shutting down all the systems........')
        speak('shutting down all the sequences........')
        speak('Bye Boss, happy to help you, have a good day')
        speak('Let\'s meet again someday')
        os.system('shutdown /r /t 1')
        sys.exit()

    elif 'open pc shutdown timer' in query:
        polite_before_request()
        speak('Turning on PC SHUTDOWN TIMER......')
        speak('please input time as seconds!')
        time = int(input('time:- '))
        os.system(f'shutdown -s -t {time}')
        sys.exit()

    elif "what\'s up" in query or 'how are you' in query:
        stMsgs = ['Just doing my thing sir!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
        speak(random.choice(stMsgs))

    elif 'email' in query:
        polite_before_request()
        speak('Who is the recipient? ')
        recipient = myCommand()

        if 'me' in recipient:
            try:
                speak('What should I say? ')
                content = myCommand()

                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.ehlo()
                server.starttls()
                server.login("Tool Bot", 'Tool Bot')
                server.sendmail('Tool Bot', "samantha police 937", content)
                server.close()
                speak('Email sent!')
                speak('Next Command! Boss!')

            except:
                speak('Sorry Boss! Something going on! I am unable to send your message at this moment!')
                speak('Next Command! Boss!')

    elif "shutdown" in query or "exit" in query or "logout" in query or "bye" in query:
        speak("GoodBye sir!!!. Have a nice day!")
        sys.exit()

    elif 'hello' in query:
        speak(f'Hello Boss')

    elif 'open' in query:
        os.system('explorer C:\\ {}'.format(query.replace('Open', '')))
        os.system('explorer D:\\ {}'.format(query.replace('Open', '')))
        speak('Next Command! Boss!')

    elif 'play music' in query:
        polite_before_request()
        speak('starting required application')
        files = os.listdir(music_path)
        d = random.choice(files)
        os.startfile(music_path + d)
        print(music_path + d)
        speak('enjoy your music sir')
        speak('Next Command! Boss!')

    elif 'tell me total ram' in query or 'total ram please' in query or 'installed ram on pc' in query or 'tell me ' \
                                                                                                          'how much ' \
                                                                                                          'ram ' \
                                                                                                          'installed ' \
                                                                                                          'on pc' in \
            query:
        total_ram_show = ["Total RAM is", "Total installed RAM is"]
        total = random.choice(total_ram_show)
        speak(f"{total} {int(round(ramtotal, 4))} GB")

    elif 'tell me available ram' in query or 'available ram please' in query or 'tell me hoe much ram free on pc' in query:
        speak(f"Free RAM or Available RAM is {int(round(ramfree, 4))} MB")
        speak(f"Percent is {rampersent}%")

    elif 'how much ram used by me' in query or 'how much ram used by programs' in query or 'how much ram used my apps' in query:
        speak(f"used ram is {int(round(ramuse, 4))} GB")
        speak("Any thing else sir?")

    elif 'connect' in query and ('with' in query or 'to' in query) and ('leo' in query or 'leo terminal' in query):
        speak("query is processing......")
        speak("Connection estabalizing with LEO Terminal......")
        import time
        pbar = tqdm(total=100, desc="Connecting.....", ascii=False, ncols=75)
        for i in range(10):
            time.sleep(0.1)
            pbar.update(10)
        pbar.close()
        speak("connection successful!!!!")
        # TODO add the command for leo_terminal
        leo_protocol = "Data\\Protocols\\leo_terminal_protocol.py"
        os.system(f"python {leo_protocol}")
        time.sleep(3)

    else:
        client = wolframalpha.Client('JWXXJE-J3LQKXR74W')
        query = query
        speak('Searching for result...')
        try:
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    polite_before_request()
                    # speak('Got it!')
                    wolalph_req = random.choice(wolframe_alpha_data_send)
                    speak(wolalph_req)
                    speak(results)
                    speak('Next Command! Boss!')

                except:
                    None

            except:
                try:
                    results = wikipedia.summary(query, sentences=5)
                    polite_before_request()
                    # speak('Got it!')
                    wiki_req = random.choice(wikipedia_data_send)
                    speak(wiki_req)
                    speak(results)
                    speak('Next Command! Boss!')

                except wikipedia.exceptions.PageError:
                    speak("Sir you asked topic can't fount in Wikipedia servers! Try another one!")

        except requests.exceptions.ConnectionError:
            speak("Please check your internet connection sir. I can't connect at the moment")


if __name__ == '__main__':

    username_credit = r"../User_credentials/username.vic"
    passwrd_credit = r"../User_credentials/user_pass.vic"
    if os.path.exists(username_credit) and os.path.exists(passwrd_credit):
        login_main()
    else:
        while True:
            start()
            while True:
                begin()
