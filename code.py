import speech_recognition as sr  
import webbrowser
import pyttsx3                 # windows 
import MusicLib
import requests
from openai import OpenAI
# from gtts import gTTs     # for better text to speech 
import os 
import pygame



def aiProcess(c):
    client = OpenAI(
        api_key = "Generate Your Own Key"
    )

    completion = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages =[
            {"role":"system", "content" : "You are virtual assisstant named jarvis skilled in general tasks like playing the songs or opening the different websites etc" } ,
            {"role" : "user" , "content" : c }
        ]
    )

    return (completion.choices[0].message.content) 
     
 
def processCommand(c):
    print(c)
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://www.linkedin.com/in/adityadevsingh58/")    
    elif "open github" in c.lower():
        webbrowser.open("https://github.com/iAdityaDev") 
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com/") 
    elif "open whatsapp" in c.lower():
        webbrowser.open("https://web.whatsapp.com/") 
    elif "open discord" in c.lower():
        webbrowser.open("https://discord.com/channels/@me")    
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]  # convert in list plsy skyfall 
        link = MusicLib.music[song]
        webbrowser.open(link) 
    elif "news" in c.lower() :  
        r = requests.get(f"Generate Your Own Key")           
        if r.status_code == 200 :  # if fetch was successfu; 
            
            data = r.json()
            articles = data.get('articles',[])
            
            for article in articles:
                speak(article['title'])
    else :
        output = aiProcess(c)
        speak(output)         

# recognizer is a class that give speech functionn fuctionality 
engine = pyttsx3.init()     # engine hai 

def speak(text):
    engine.say(text)
    # print(engine.getProperty('rate'))
    engine.setProperty('rate', 125) 
    # voices = engine.getProperty('voices')   
    engine.runAndWait()
    
    
    
if __name__ == '__main__':
    speak("initializing Jarvis......")   
   
    while True :
        r = sr.Recognizer()
        #  Listen for the wake word Jarvis 
        
        #obtain the audio from the microphone
      
            
        
            # recognise speech using the Google  
        print("Recognising.....")
        try:
            with sr.Microphone() as source :
                print("Listening......")
                audio = r.listen(source,timeout=5,phrase_time_limit=10)
                word = r.recognize_google(audio)
            if(word.lower()=="jarvis"):
                speak("Activating Jarvis")
                
                # listen for command    
                with sr.Microphone() as source :
                    print("Command sir......")
                    audio = r.listen(source,timeout=5,phrase_time_limit=10)
                    command = r.recognize_google(audio)
                    
                    processCommand(command)
        except Exception as e :
            print(e)    
            
            
            
# gtts for good text to speech             
                