import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
listener = sr.Recognizer()
engine = pyttsx3.init()
voice = engine.getProperty('voices')
engine.setProperty('voice',voice[1].id)
def talk(text):
    engine.say(text)
    engine.runAndWait()
def take_command():
    try:
        with sr.Microphone() as source:
            print('listening....')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'tech' in command:
                command = command.replace('tech','')



    except:
        pass
    return  command

def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play','')
        talk('Playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M')
        talk('Current time is '+ time)
    elif 'are you commited' in command:
        talk('I am in a realationship with You')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'who' in command:
        person = command.replace('wikipedia',"")
        info = wikipedia.summary(person,1)
        talk(info)
    else:
        talk("Come Again")

while True:
    run_alexa()