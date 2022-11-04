try:
    import sys,os,pywhatkit,random,requests,datetime,time,wikipedia,speech_recognition as sr,pyttsx3,platform , pyautogui , keyboard
except:

    print("F.R.I.D.A.Y Error[x0129]\nGet To F.R.I.D.A.Y official site down below \nto know more about this error")

import webbrowser
from pyautogui import click, leftClick, rightClick, middleClick , displayMousePosition , doubleClick
from keyboard import write, press, press_and_release

os.system("cls")
os.system("title Friday.Main.Window")

class System:
    def __checkVersion__():
        pc_System_version = Brain.GetPC_Info.pc_System_Version
        if pc_System_version == "Windows 8.1":return "Windows 8.1 = True"
        else:return "Windows 8.1 = False"
    
    def __SessionID__():
        return random.randint(100000 , 999999)

__SessionID__ = System.__SessionID__()

print(f"Your Session Id :  {__SessionID__}")


class Brain:
    class ApplicationsPaths:
        taskmanager         = "C:\\Windows\\System32\\Taskmgr.exe"
        DiskManagement      = "C:\\Windows\\System32\\Diskmgmt.msc"
        CMD                 = "C:\\Windows\\System32\\cmd.exe"
        Notepad             = "C:\\Windows\\notepad.exe"
        fileMGMT            = "C:\\Windows\\explorer.exe"
        regEditor           = "C:\\Windows\\regedit.exe"
        camera              = "C:\\Windows\\Camera\\camera.exe"
        DeviceMGMT          = "C:\\Windows\\System32\\Devmgmt.msc"
        DeviceInfo          = "C:\\Windows\\System32\\dxdiag.exe"
        HOSTName            = "C:\\Windows\\System32\\HOSTNAME.EXE"
        IPConfig            = "C:\\Windows\\System32\\ipconfig.exe"
        MSConfig            = "C:\\Windows\\System32\\msconfig.exe"
        MSINFO              = "C:\\Windows\\System32\\msinfo32.exe"
        Chrome_exe          = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        
        ### Friday Artificial Intelligence ###
        Friday              = "C:\\Users\\H\\Desktop\\Folder\\A.I\\Python\\Main.py"  ### Put you Friday path here
        base_path_location  = "C:\\Users\\H\\Desktop\\Folder\\A.I\\Python"  ### Put your Friday folder here
        ### End ###

    class Chatbot:
        def __init__(self, query):
            query = str(query)
            speak = Brain.speakr.speak
            hellohi = [
                'hi',
                'hello',
                'huh',
                'hello friday',
                'oh hello',
                'oh hello friday',
                'hola',
                'hola amigo',
                'bonjour'
                ]

            hellohi_reply = [
                'Oh hello Sir',
                'Hello Sir',
               f'Hello {os. getlogin()}',
                'Oh hello sir, How are you Doing',
                'Hello Sir, How are you?'
                ]

            how_send = ['how are you' , 'how are you doing' , 'how about you' , 'how are you friday']
            how_return = [
                "I'm fine",
                "I'm fine Sir",
                "Fine Sir",
                "I'm good",
                "I'm good Sir",
                "I'm very well Sir", 
                "well Sir"
                ]

            work_send = ['what are you doing' , 'what you doing']
            work_reply = ['Sir, I am listening and answering to you.' , 'I am speaking to you']

            iam_send =  ["i am fine" , "i am good" , "mai theek hun" , "not good"]
            iam_reply = [
                'Totally Fine',
                "That's good",
                "That's Fine",
                "Oh, Great!",
                "Good To Hear That",
                "Great!",
                "Good."
                ]

            iam2_send = ["i am not fine" , "i am not good"]
            iam2_reply = [
                "Oh?, What happened?",
                "That's not good",
                "OH!",
                "Sorry to hear that but what happened?",
                "What happened?"
                ]

            Nothing = ['nothing' , "what can you do" , 'nothing at all']
            Nothing_reply = ['Nothing', 'nothing at all' , 'Absolutely Nothing']

            if query in hellohi:
                speak(random.choice(hellohi_reply))

            elif query in Nothing:
                speak(random.choice(Nothing_reply))
            
            elif query in iam2_send:
                speak(random.choice(iam2_reply))

            elif query in how_send:
                speak(random.choice(how_return))

            elif query in work_send:
                speak(random.choice(work_reply))

            elif 'introduce yourself to ' in query:
                query = str(query)
                query = query.replace("introduce yourself to " , "")
                Brain.OnStart.Introducetosomeone(query)

            elif '*' in query:
                speak("Please don't try to abuse")
                
            elif 'who are you' in query or 'well by the way who are you' in query or 'who the heck are you' in query:
                Brain.OnStart.Intro()

            elif query in iam_send:
                speak(random.choice(iam_reply))


        ### End ###


    class ClickerAt:
        def Pos(x=0, y=0 , fortype=None):
            if fortype != None: fortype = fortype
            elif fortype == None: fortype = "left"
            x = int(x)
            y = int(y)
            t = str(fortype)
            time.sleep(1)
            if 'left' in t:
                leftClick(x , y)
            elif 'right' in t:
                rightClick(x , y)
            elif 'middle' in t:
                middleClick(x, y)
            elif 'double' in t:
                doubleClick(x , y)
            elif 'mouse position' in t:
                displayMousePosition()
            else:
                print("No position or key word found")
        
        ### End ###

    class DataChecker:
        def __Data__():
            try: data = requests.get("https://www.google.com");return "connected"
            except: return "Not Connected"
        
        ### End ###

    class GetPC_Info:
        pc_name = f"{os.getlogin()}"
        pc_system = f"{platform.system()}"
        pc_info = f"{platform.uname()}"
        pc_System_Info= pc_info.replace("node" , "Computer Name")
        pc_System_Version = f"{platform.system()} {platform.release()}"
        
        ### End ###

    class GetTime:
        def __ChangeSet__(hour):
            hour = int(hour)
            if hour == 13:
                return "1"
            elif hour == 14:
                return "2"
            elif hour == 15:
                return "3"
            elif hour == 16:
                return "4"
            elif  hour == 17:
                return "5"
            elif hour == 18:
                return "6"
            elif hour == 19:
                return "7"
            elif hour == 20:
                return "8"
            elif hour == 21:
                return "9"
            elif hour == 22:
                return "10"
            elif hour == 23:
                return "11"
            elif hour == 24:
                return "12"
            else:pass

        def GiveTime():
            hour = datetime.datetime.now().strftime("%H")
            minute = datetime.datetime.now().strftime("%M")
            second = datetime.datetime.now().strftime("%S")
            Day = datetime.datetime.now().strftime("%d")
            month = datetime.datetime.now().strftime("%m")
            year = datetime.datetime.now().strftime("%y")

            hour = int(hour)

            if hour <= 12: _get = "AM"

            elif hour >= 13:
                hour = Brain.GetTime.__ChangeSet__(hour); _get = "PM"

            return f"Time is {hour}:{minute} {_get} of date {Day} : {month} : {year}"
        
        ### End ###

    class Google:
        def __init__(self, query):
            speak = Brain.speakr.speak
            query = str(query)
            query = query.replace("google search " , "")
            query = query.replace("google " , "")
            query2 = query.replace(" " , "+")
            pywhatkit.search(query2)
            try:
                Brain.Wiki(query , condition="google")                
            except:
                speak("Sorry, The results got, can't be spoken")       
        
        ### End ###

    class Listenr:
        def __Listen__():
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening...")
                try:
                    audio = r.listen(source, 7)
                except:pass

            try:
                print("Initializing...")
                query = r.recognize_google(audio, language="en-US")
                print("")
                print(f"User Said : {query}")
                print("")
            except Exception:
                query = "none"

            return query
        
        ### End ###

    class OnStart:
        def Introducetosomeone(name):
            Brain.speakr.speak(f"Hello {name}, Nice to meet you")

        def Intro():
            speak = Brain.speakr.speak
            speak("Allow me to introduce myself")
            time.sleep(0.2)
            speak("I'm Friday, A virtual artificial intelligence and I'm here to assist you with a variety of task as best i can")


        def SelfIntro():
            Brain.speakr.speak(f"Welcome Back Sir, {Brain.GetTime.GiveTime()}")
        
        ### End ###

    class Restarter:
        def __init__(self):
            speak = Brain.speakr.speak
            speak("Restarting Friday")
            os.startfile(Brain.ApplicationsPaths.Friday)
            print("Session Ended")
            time.sleep(2)
            sys.exit()
        
        ### End ###

    class SetVolume:
        def __init__(self, query):
            query = str(query)
            query = query.replace("volume set to " , "")
            query = int(query)

            if 'mute' in query:
                leftClick(x=1227, y=752)
                time.sleep(1)
                leftClick(x=1232, y=645)

            elif '50' in query:
                leftClick(x=1227, y=752)
                time.sleep(1)
                leftClick(x=1222, y=559)     

            elif '100' in query:
                leftClick(x=1227, y=752)
                time.sleep(1)
                leftClick(x=1223, y=502)  
        
        ### SetVolume hasn't Finished yet ###

    class speakr:
        def speak(audio):
            if audio == "none":pass
            else:
                engine = pyttsx3.init('sapi5')
                voices = engine.getProperty('voices')
                engine.setProperty('voice', voices[2].id)
                engine.setProperty('rate' , 205)
                engine.setProperty('volume' , 1)
                engine.say(audio)
                print(f"Friday : {audio}")
                engine.runAndWait()
        
        ### End ###

    class SystemCommand:
        def __System__(command):
            speak = Brain.speakr.speak
            if 'shutdown computer' in command or 'shutdown pc' in command or 'shutdown my pc' in command:
                speak("Shutting down the computer")
                press_and_release("win + d")
                time.sleep(1)
                press_and_release("alt + f4")
                time.sleep(1)
                press_and_release("enter")

            elif 'restart my pc' in command or 'restart pc' in command or 'get my pc a restart' in command or 'get my pc a fresh restart' in command:
                speak("Restarting the Computer")
                press_and_release("win + d")
                time.sleep(1)
                press_and_release('alt + f4')
                time.sleep(1)
                press_and_release('down')
                time.sleep(1)
                press_and_release('enter')
            
            elif 'put computer to sleep' in command or 'put my pc to sleep' in command:
                speak("Putting Computer to sleep")
                press_and_release("win + d")
                time.sleep(1)
                press_and_release('alt + f4')
                time.sleep(1)
                press_and_release('up')
                time.sleep(1)
                press_and_release('enter')

        def Sys(command):
            speak = Brain.speakr.speak
            command = str(command)
            command = command.lower()
            if 'task manager' in command:
                os.startfile(Brain.ApplicationsPaths.taskmanager)
                speak("Opened Task manager")

            elif 'copy output of ' in command:
                query = str(command)
                commanded = query.replace("copy output of " , "")
                command = f"{commanded} | clip"
                try:
                    os.system(command)
                    speak(f"Copied output of {commanded}")
                except:
                    speak(f"Sorry, Can't copy output of {commanded} , Maybe wrong command?")

            elif 'disk management' in command:
                os.startfile(Brain.ApplicationsPaths.DiskManagement)
                speak("Opened Disk Management")

            elif 'cmd' in command:
                os.startfile(Brain.ApplicationsPaths.CMD)
                speak("Opened Command Prompt")

            elif 'notepad' in command:
                os.startfile(Brain.ApplicationsPaths.Notepad)
                speak("Opened Notepad")

            elif 'file manager' in command:
                os.startfile(Brain.ApplicationsPaths.fileMGMT)
                speak("Opened File Explorer")

            elif 'registry editor' in command:
                os.startfile(Brain.ApplicationsPaths.regEditor)
                speak("Opened Registry Editor")

            elif 'camera' in command:
                os.startfile(Brain.ApplicationsPaths.camera)
                speak("Opnened Camera")

            elif 'device manager' in command:
                os.startfile(Brain.ApplicationsPaths.DeviceMGMT)
                speak("Opened Device Manager")

            elif 'device info' in command:
                os.startfile(Brain.ApplicationsPaths.DeviceInfo)
                speak("Opened Device Information")

            elif 'hostname' in command:
                os.system(Brain.ApplicationsPaths.HOSTName)
                speak("Printed Hostname")

            elif 'ip address' in command:
                os.system(Brain.ApplicationsPaths.IPConfig)
                speak("Printed IP Address")

            elif 'system config' in command:
                os.startfile(Brain.ApplicationsPaths.MSConfig)
                speak("Opened Microsoft Configurations")

            elif 'system info' in command:
                os.startfile(Brain.ApplicationsPaths.MSINFO)
                speak("Opened Microsoft Information")

            elif 'take screenshot' in command or 'take a screenshot' in command:
                press_and_release("win + printscreen")
                speak("ScreenShot Taken")

            elif 'open chrome' in command:
                os.startfile(Brain.ApplicationsPaths.Chrome_exe)
                speak("Opened Chrome")

            elif 'open virtualbox' in command:
                os.startfile(Brain.ApplicationsPaths.VB_exe)
                speak("Opened Virtual Box")

            elif 'close chrome' in command or 'shutdown chrome' in command:
                os.system("Taskkill /f /im chrome.exe")
                speak("Closed Chrome")
                os.system("cls")

            elif 'clear screen' in command or 'cls' in command:
                os.system("cls")

            elif 'close opened window' in command:
                press_and_release("alt + f4")
                speak("Closed Opened window")

            elif 'go to desktop' in command:
                press_and_release("win + d")
                speak("Done!, You're on Desktop now")          

            elif 'start gta 4' in command:
                os.startfile(Brain.ApplicationsPaths.GTA_IV)
            
            elif 'start gta vice city' in command or 'start gta vc' in command:
                os.startfile(Brain.ApplicationsPaths.GTA_VC)
            
            elif 'start gta 3' in command:
                os.startfile(Brain.ApplicationsPaths.GTA_III)
            
            elif 'start gta sa' in command or 'start gta san andreas' in command:
                os.startfile(Brain.ApplicationsPaths.GTA_SA)
            
            elif 'click ' in command:
                query = str(command)
                query = query.replace("click at ", "")
                query = query.replace("click ", "")
                print(query)
                print("")
                try:
                    x ,mv, y  = query.split(" ")
                except:
                    x = 0
                    y = 0 
                    mv = None
                print("X : " + x + "   Y : " + y + "MV : " + mv)
                x = int(x)
                y = int(y)
                mv = str(mv)
                Brain.ClickerAt.Pos(x , y)

                speak("Clicked!")
            else:
                Brain.SystemCommand.__System__(command)
        
        ### End ###
    def atWelcome():
        speak = Brain.speakr.speak
        speak("Welcome Back Sir")
        ptime = Brain.GetTime.GiveTime()
        speak(f"Sir, {ptime}")
        speak("Now, What can i do for you?")
        

    class Wiki:
        def __getcondition__(condition, results=None):
            speak = Brain.speakr.speak
            if condition == "casual":
                speak("According to Wikipedia...")
            
            elif condition == "google":
                speak("According to Internet...")
            
            elif condition == "notspeak":
                pass
            
            if results != None:
                if condition =="notspeak":pass
                else:
                    speak(results)

            else:pass

        def __init__(self, query , condition=None):
            if condition == None:condition = "casual"
            speak = Brain.speakr.speak
            query = str(query)
            query = query.replace("wikipedia search " , "")
            try:
                results = wikipedia.summary(query, sentences=2)
                Brain.Wiki.__getcondition__(condition , results)
            except:
                try:
                    results = wikipedia.summary(f"define {query}", sentences=2)
                    Brain.Wiki.__getcondition__(condition , results)
                except:
                    try:
                        results = wikipedia.summary(f"defination of {query}", sentences=2)
                        Brain.Wiki.__getcondition__(condition , results)
                    except:
                        try:
                            results = wikipedia.summary(f"who is {query}", sentences=2)
                            Brain.Wiki.__getcondition__(condition , results)
                        except:
                            try:
                                results = wikipedia.summary(f"what is {query}", sentences=2)
                                Brain.Wiki.__getcondition__(condition , results)
                            except:
                                print("")
                                speak("Sorry, Couldn't fetch any data or relatable data from wikipedia")
        
        ### End ###

    class Youtube:
        def __init__(self, query):
            query = str(query)
            query = query.replace("youtube search " , "")
            query1 = query.replace(" " , "+")
            if 'play+playlist' in query1:
                webbrowser.open("https://www.youtube.com/watch?v=V6Q-klKBkXw&list=PLTnfJXRz5-KMLKqe93Pa0ddscbzZSWdoM")
            else:
                pywhatkit.playonyt(query1)  
        
        ### End ###

    class FinderPath:
        def __findP__(name , pathtofindin):
            speak = Brain.speakr.speak
            name = str(name)
            path = str(pathtofindin)
            rpath = ""
            for x in os.listdir(path):
                if name == x:
                    speak(f"File at {path}\\{x}")
                    break
                else:
                    for items in os.listdir(f"{path}\\{x}"):
                        if name == x:
                            speak(f"File at {path}\\{x}\\{items}")
                            break 
                        else:
                            for things in os.listdir(f"{path}\\{x}\\{items}"):
                                if things == name:
                                    speak(f"File at {path}\\{x}\\{items}\\{things}")
                                    break

                                else:
                                    for files in os.listdir(f"{path}\\{x}\\{items}\\{things}"):
                                        if files == name:
                                            speak(f"File at {path}\\{x}\\{items}\\{things}")
                                            break
                                    else:
                                        speak(f"Sorry can't find {name} in drive C:\\")

        ### End ###
          
    class InstaG:
        def __login__():
            speak = Brain.speakr.speak
            speak("Logging in on Instagram as Coder H")
            webbrowser.open(f"")

        ### InstaG hasn't finished yet ###

    class ReadOutsideFile:
        def __init__(self , name):
            speak = Brain.speakr.speak
            t= 0 
            newfile = open(f"{name}_decoded_file.txt" , "w")
            for lines in open(name , "r"):
                t+=1
                print(lines)
                newfile.write(f"{lines}")

            time.sleep(1)
            newfile.close()
            speak(f"Total lines counted : {t}")

            speak("")
            speak("")
            speak("")
            speak("DONE !!!!!!!!")
            speak("")
            speak("")
            speak("")    

        ### End ###
    
    class AllReadexternalfiles:
        def __init__(self , permission):
            speak = Brain.speakr.speak
            path = "C:\\"
            if permission:pass
            else:permission = False

            if permission == True:
                name = str(name)
                rpath = ""
                for x in os.listdir(path):
                    if '.' in x:
                        Brain.ReadOutsideFile(f"{path}\\{x}")
                    else:
                        for items in os.listdir(f"{path}\\{x}"):
                            if '.' in x:
                                Brain.ReadOutsideFile(f"{path}\\{x}\\{items}")
                                break 
                            try:
                                for things in os.listdir(f"{path}\\{x}\\{items}"):
                                    if '.' in  name:
                                        speak(f"File at {path}\\{x}\\{items}\\{things}")
                                        break
                                    try:
                                        for files in os.listdir(f"{path}\\{x}\\{items}\\{things}"):
                                            if files == name:
                                                speak(f"File at {path}\\{x}\\{items}\\{things}")
                                                break
                                        else:
                                            speak(f"")
                                    except:pass
                            except:pass

        ### End ###
        
def Responder():
    while True:
        speak = Brain.speakr.speak
        query = Brain.Listenr.__Listen__()
        query = str(query).lower()
    
        if 'wikipedia search' in query or 'define' in query or 'defination of' in query:
            Brain.Wiki(query)

        elif 'is my net connected' in query or 'am i connected to internet' in query or 'is my internet connected' in query:
            if Brain.DataChecker.__Data__() == "connected":
                speak("Yes Sir, It's connected")
            else:speak("No Sir, It's not connected")

        elif 'google search ' in query:
            Brain.Google(query)

        elif 'what time is it' in query or 'tell me time' in query or 'tell time' in query or 'speak time' in query:
            speak(Brain.GetTime.GiveTime())
        
        elif 'youtube search' in query:
            Brain.Youtube(query)
        
        elif 'set volume' in query:
            Brain.SetVolume(query)

        elif 'print session id' in query:
            print(__SessionID__)
        
        elif 'speak session id' in query:
            speak(__SessionID__)
        
        elif 'just speak ' in query:
            query = str(query)
            query = query.replace("just speak " , "")
            speak(query)

        elif 'exit' in query or 'quit' in query or 'session close' in query or 'kill session id' in query:
            speak(f"Closing System with session id : {__SessionID__}")
            sys.exit()
        
        elif 'restart yourself' in query:
            Brain.Restarter()

        elif 'open your folder' in query:
            os.startfile(Brain.ApplicationsPaths.base_path_location)
        elif 'none' in query:pass

        else:
            Brain.Chatbot(query); Brain.SystemCommand.Sys(query)

Brain.atWelcome()

while True:
    try:
        Responder()
    except Exception as e:
        Brain.speakr.speak(f"There is an Error : \n\n\n {e} \n\n\n Trying to skip this error")
