from click import command
import pyttsx3
from platform import machine
import speech_recognition as sr
import os
import datetime
import speech_recognition as sr
import webbrowser
import playsound
import random
import wikipedia
from gtts import gTTS
from tkinter import *
from PIL import ImageTk,Image

r = sr.Recognizer()
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<= 12:
        speak("Good Morning!!")

    elif hour>=12 and hour<=18:
        speak("Good Afternoon!!")

    else:
        speak("Good Evening!!")
    
    speak("I am your Assistant. How may i help you")

def addition():
    try:
        with sr.Microphone() as source:
            speak('Say First Number :')
            voice = r.listen(source)
            command = r.recognize_google(voice)
            num1 = command
            n1 = int(command)
            print('Your First Number :' + num1)
            speak('Say Second Number :')

            voice = r.listen(source)
            command = r.recognize_google(voice)
            num2 = command
            n2 = int(command)
            print('Your Second Number :' + num2)
            n3 = n1 + n2
            sum1 = str(n3)
            return sum1
    except Exception as e:
        print(e)

def takeCommand():

    
    with sr.Microphone() as source:
        print("Listening...")
        speak('Listening')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("recognizing....")
        speak("Recognizing")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")
    
    except Exception as e:
        print("Say that again please")
        speak('Say that again please')
        return "None"
    return query


class Widget:
    def __init__(self):
        root=Tk()

        root.title('laila')
        root.geometry('520x320')
        root.minsize(1000,500)
        root.maxsize(200,200)

        scrollbar=Scrollbar()
        scrollbar.pack(side=RIGHT)

        # img=ImageTk.PhotoImage(Image.open('1.jpg'))
        # panel =Label(root, image=img)
        # panel.pack(side='right',fill='both',expand=0)

        global userText
        userText =StringVar()

        userText.set('Your Virtual assistant')
        userFrame =LabelFrame(root, text='Virtual Assitant',font=('Railways',50,'bold'))
        userFrame.pack(fill='both',expand=1)

        top=Message(userFrame,textvariable=userText,bg='black',fg='white')
        top.config(font=("Century Gothic",30,'bold'))
        top.pack(side='top',fill='both',expand=1)

        btn=Button(root, text='Run', font=('railways',20,'bold'),bg='red',fg='white',command=run).pack(fill='x',expand=0)
        
        btn1=Button(root, text='Exit', font=('railways',20,'bold'),bg='yellow',fg='black',command=root.destroy).pack(fill='x',expand=0)
        
        root.mainloop()




def run():
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Seraching wikkipedia.....')
            query = query.replace('wikipedia', "")
            results = wikipedia.summary(query,sentences=1)
            speak("According to wikipedia")
            print(results)
            speak(results)
            
            break
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            break
        
        elif 'open google' in query:
            webbrowser.open("google.com")
            break

        elif 'play music' in query:
            music='E:\project\tkinter\songs'
            songs = os.listdir(music)
            value = random.randint(0,3)
            os.startfile(os.path.join(music, songs[value]))
            break
        
        elif 'the time' in  query:
            Time = datetime.datetime.now().strftime("%H:%M;%S")
            speak(f"Sir,the time is{Time}") 
            break
        
        elif 'number' in query:
            number =random.randrange(0,100)
            speak('A random number between 0 and 100 is')
            print('A random number between 0 and 100 is')
            speak(number)
            break
        elif 'time' in query:
            time = datetime.datetime.now().strftime('%I:%M %p')
            speak('Current time is ' + time)
            print(time)
            break
        elif 'exit' in query:
            speak('Have a nice day, bye')
            print('Have a nice day, bye')
            break
    

        elif 'bye' in query:
            speak('Have a nice day, bye')
            print('Have a nice day, bye')
            break
        elif 'add' in query:
            sol = addition()
            speak("sum is "+sol)
            print("sum is "+sol)
            break



if __name__== '__main__':
    widget = Widget()



