import speech_recognition as sr
import webbrowser as wb
import os
import sys

r1 = sr.Recognizer()
r2 = sr.Recognizer()
r3 = sr.Recognizer()
with sr.Microphone() as source:
    print('Creator: For create html pages. \nDesigner: For design your html page')
    audio = r3.listen(source)
 # Query 1

speak = r2.recognize_google(audio)
global create
def create_file(get):
    open("C:\\Users\\Lenovo\\Desktop\\SpeechToText\\" +get+".html", 'w') #Path Your file will created


if 'creator' in speak:
    r2 = sr.Recognizer()
    os.startfile("C:\\Users\\Lenovo\\Desktop\\SpeechToText")
    with sr.Microphone() as source:
        print('creating folder')
        audio = r2.listen(source)
    try:
        get = r2.recognize_google(audio)
        create_file(get)
        print('created folder ' + get + '.html')
    except sr.UnknownValueError:
        print('error')
    except sr.RequestError as e:
        print('failed' + format(e))
  # Query
if 'designer' in r1.recognize_google(audio):
    r1 = sr.Recognizer()
    with sr.Microphone() as source:
        print('adding thing')
        audio = r1.listen(source)
        try:
            get = r1.recognize_google(audio)
            if(get == "hello"):
                text = "\n<h2> Hello World </h2>"
                with open("index.html", "a") as ok:
                    ok.write(text)
            elif(get == "divide"):
                text = "\n<div> A simple div </div>"
                with open("index.html" , "a") as index:
                    index.write(text)
            elif(get == "from"):
                text = "\n<style> * { margin-top:24px; }</style>"
                with open("index.html" , "a") as index:
                    index.write(text)
        except sr.UnknownValueError:
            print('error')
        except sr.RequestError as e:
            print('failed' + format(e))