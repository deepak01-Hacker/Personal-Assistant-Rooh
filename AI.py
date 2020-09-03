import pyttsx3
import webbrowser
import smtplib
import random
import speech_recognition as sr
import wikipedia
import wolframalpha
import os
import sys
import pyaudio

engine = pyttsx3.init('sapi5')

client = wolframalpha.Client('Your_App_ID')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices) - 1].id)


def speak(audio):
    print('Computer: ' + audio)
    engine.say(audio)
    engine.runAndWait()


def greetMe():
    currentH = int(datetime.datetime.now().hour)
    speak('Good Morning!')


greetMe()

speak('Hello Sir, I am your digital assistant Rooh')
speak('How may I help you?')


def myCommand(choiec):
    r = sr.Recognizer()
    if choiec == 'yes':
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language='en-in')
            print('User: ' + query + '\n')
        except sr.UnknownValueError:
            speak('Sorry sir! I didn\'t get that! Try typing the command!')
            query = str(input('Command: '))
    elif choiec == 'no':
        try:
            speak('so you type the command')
            query = str(input('Command : '))
        except:
            speak('sorry sir re -write the command')
            query = str(input('Command : '))
    return query


if __name__ == '__main__':

    speak('If you want to AI listen your command Press yes and for type press no')
    choiec = str(input("command : "))

    while True:

        query = myCommand(choiec);
        query = query.lower()

        if 'open youtube' in query:
            speak('okay')
            webbrowser.open('www.youtube.com')

        elif 'open google' in query:
            speak('okay')
            webbrowser.open('www.google.co.in')
        elif 'play music' in query:
            speak('okay')
            webbrowser.open('https://www.youtube.com/watch?v=MtHugZNPC4Y')

        elif 'open gmail' in query:
            speak('okay')
            webbrowser.open('www.gmail.com')
        elif 'what is your name' in query or 'your name' in query or 'say about you' in query:
            speak('i am a digital assitant\n name rooh \n made by deepak \n my mainly purpose is your entertain')
        elif 'who is your founder' in query:
            speak('Deepak')
        elif 'who is your father' in query:
            speak('Deepak')
        elif 'love' in query:
            speak('Waste of time')
        elif 'today weather' in query:
            webbrowser.open('https://www.google.com/search?q=today+weather&rlz=1C1CHBF_enIN863IN863&oq=today&aqs=chrome.2.69i57j69i59j35i39j0l3.4425j1j7&sourceid=chrome&ie=UTF-8')

        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))

        elif 'check internet speed' in query:
            webbrowser.open('https://fast.com')

        elif 'email' in query:
            speak('Who is the recipient? ')
            recipient = myCommand()

            if 'me' in recipient:
                try:
                    speak('What should I say? ')
                    content = myCommand()

                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login("Your_Username", 'Your_Password')
                    server.sendmail('Your_Username', "Recipient_Username", content)
                    server.close()
                    speak('Email sent!')

                except:
                    speak('Sorry Sir! I am unable to send your message at this moment!')


        elif 'nothing' in query or 'abort' in query or 'stop' in query:
            speak('okay')
            speak('Bye Sir, have a good day.')
            sys.exit()

        elif 'hello' in query or 'hello rooh' in query:
            speak('Hello Sir')

        elif 'bye' in query or 'stop' in query:
            speak('Bye Sir, have a good day.')
            sys.exit()

        else:
            query = query
            speak('Searching...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('WOLFRAM-ALPHA says - ')
                    speak('Got it.')
                    speak(results)

                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak('Got it.')
                    speak('WIKIPEDIA says - ')
                    speak(results)

            except:
                speak('unable to understand')
                speak('search on google')
                webbrowser.open('www.google.com')


        speak('Next Command! Sir!')

# Limitation of Assitant is that
# 1. No  / Yes                                  - press then AI say type
# 2. Hello                                       - hello to rooh
# 3. how are you                                 - cmd
# 4. What is your name                           -cmd
# 5. who is your founder
# 6. today weather
# 7. Check internet speed
# 8. play music
# 9. open google
# 10. open youtube
# 11.stop assistant press stop
