import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle 
import tkinter.scrolledtext as st 
import pyttsx3
import speech_recognition as sr
import datetime
import os
import pygetwindow as gw
import time
import pyautogui as pi
import random
import pygame

# User credentials (you can replace these with a database)
user_credentials = {
    "Fahad": "333",
    "Eliya": "222",
    "Anas": "111",
    "Amjad": "000"
}

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('rate', 140)
engine.setProperty('voice', voices[0].id)

assistant_active = False  # Assistant initially inactive

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe(username):
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak(f"Good Morning!, {username}")
    elif hour >= 12 and hour < 18:
        speak(f"Good Afternoon!, {username}")
    else:
        speak(f"Good Evening!, {username}")
    speak("Ready To Comply. What can I do for you ?")

def authenticate_user(username, password):
    if username in user_credentials and user_credentials[username] == password:
        return True
    else:
        return False

def takeCommand(username, response_text):
    r = sr.Recognizer()
    
    # Display "Listening..." in the text box
    response_text.insert(tk.END, "Listening...")
    response_text.update_idletasks()  # Update the text box immediately
    
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-IN')
        print(f"{username} said: {query}")
        # Clear "Listening..." and display the user's query
        response_text.delete("1.0", tk.END)  # Delete the "Listening..." message
        response_text.insert(tk.END, f"{username} said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        # Clear "Listening..." and display an error message
        response_text.delete("1.0", tk.END)  # Delete the "Listening..." message
        response_text.insert(tk.END, "Sorry, I couldn't understand. Please try again.\n")
        return "None"
    return query


pygame.mixer.init()
def play_welcome_music():
    pygame.mixer.music.load('C:/Users/HP/Downloads/welcome.mp3')
    pygame.mixer.music.play()


def update_text():
        root.after(0, update_text)

def turn_off():
    global assistant_active, current_user
    print("Turning off the virtual assistant...")
    speak("Thank you for using the virtual assistant!")
    assistant_active = False
    start_button["state"] = "normal"  # Enable the Start Assistant button
    close_button["state"] = "enabled"  # Disable the Close Assistant button
    current_user = ""  # Clear the current user
    username_entry.delete(0, tk.END)  # Clear the username entry field
    password_entry.delete(0, tk.END)  # Clear the password entry field
    auth_button.config(state="normal")  
    
def authenticate_user():
    username = username_entry.get()
    password = password_entry.get()
    if authenticate_user_credentials(username, password):
        response_text.delete("1.0", tk.END)
        response_text.insert(tk.END, "Authentication successful!\n")
        start_button.config(state="normal")  # Enable the Start Assistant button
        auth_button.config(state="disabled")  # Disable the Authenticate button
    else:
        response_text.delete("1.0", tk.END)
        response_text.insert(tk.END, "Authentication failed. Please try again.\n")
        
      
# Create a function to authenticate user credentials
def authenticate_user_credentials(username, password):
    return username in user_credentials and user_credentials[username] == password

# Create a function to start the virtual assistant
def start_assistant():
    global assistant_active, current_user
    assistant_active = True
    username = username_entry.get()
    current_user = username  # Store the current user
    response_text.config(state=tk.NORMAL)  # Enable editing of the text widget
    play_welcome_music()
    wishMe(username)
    response_text.delete("1.0", tk.END)  # Clear the response text widget
    start_button.config(state="disabled")  # Disable the Start Assistant button
    close_button.config(state="normal")  # Enable the Close Assistant button

    while assistant_active:
        query = takeCommand(username, response_text).lower()  # Pass 'response_text' as an argument
        handle_query(query)
        
        response_text.config(state=tk.DISABLED)  # Disable editing of the text widget after the loop
        
    # After the assistant loop ends, clear the user's credentials
    current_user = ""
    username_entry.delete(0, tk.END)  # Clear the username entry field
    password_entry.delete(0, tk.END)  # Clear the password entry field
    auth_button.config(state="normal")  # Enable the Authenticate button
    start_button.config(state="disable")  # Enable the Start Assistant button after closing

def handle_query(query):
    words = []
    if 'max' in query:
        print("Yes sir")
        speak("Yes sir")

    if "turn off" in query:
        turn_off()
     
    elif "erase everything" in query:
        response_text.config(state=tk.NORMAL)  # Enable the text widget
        response_text.delete("1.0", tk.END)  # Clear the text widget
        
    elif 'who are you' in query:  
            print('I am your virtual Assistant ,max!')
            speak('I am your virtual Assistant ,max!')
        
    elif 'who created you' in query:
            print('I was created by Fuh-haad, using Python language, in Visual Studio Code.')
            speak('I was created by Fuh-haad, using Python language, in Visual Studio Code.')
            
    elif 'open pc' in query:
            os.system("explorer")

    elif "search this pc" in query:
            pi.moveTo(821, 138, 1)
            pi.click(x=821, y=138, clicks=2, button='left')
          
    elif "press enter" in query:
            pi.moveTo(555, 194, 1)
            pi.click(x=555, y=194, clicks=2, button='left')
            
    elif 'close pc' in query:
            explorer_windows = gw.getWindowsWithTitle("This pc")
            if explorer_windows:
                explorer_windows[0].close()
            else:
                speak("File Explorer window not found.")
            
    elif 'make a note' in query:
            os.system("start notepad") 
            
    elif ('type') in query:
            query = query.replace("type","")
            pi.write(f"{query}", 0.1) 
            
    elif ('save it') in query:
            pi.hotkey("ctrl","shift","s")
            time.sleep(1)
            pi.press("enter")
            
    elif 'close notepad' in query:
            os.system("taskkill /f /im notepad.exe")
            
    elif 'open command prompt' in query:
            os.system("start cmd")
            
    elif 'close command prompt' in query:
            os.system("taskkill /f /im cmd.exe")
            
    elif "refresh window" in query:
            pi.hotkey('ctrl', 'r')

        
    elif 'play music' in query:
            music_dir = 'E:\Music'  # Change this to your music directory
            songs = os.listdir(music_dir)
            music_file = os.path.join(music_dir, random.choice(songs))
            os.system(f'start wmplayer "{music_file}"')  # Play the selected music file using Windows Media Player
            
    elif 'close music' in query: 
            os.system("taskkill /f /im wmplayer.exe")
            
    elif 'tell me the time' in query:
            current_time = datetime.datetime.now().strftime("%I:%M %p")  # Get the current time
            speak(f"The current time is {current_time}")
            
    elif 'shutdown system' in query:
            speak("Shutting down the system")
            os.system("shutdown /s /t 1")  # Shutdown the system with a delay of 1 second

    elif 'restart system' in query:
            speak("Restarting the system")
            os.system("shutdown /r /t 1") 
            
    elif 'open camera' in query:
            os.system("start microsoft.windows.camera:")
            
    elif 'close camera' in query:
            os.system("taskkill /f /im WindowsCamera.exe")
            
    elif 'take a screenshot' in query:
            screenshot = pi.screenshot()
            screenshot.save('screenshot.png')
            speak("Screenshot taken and saved ")
            
    elif 'volume up' in query:
            pi.press("volumeup")
            pi.press("volumeup")
            pi.press("volumeup")
            pi.press("volumeup")
            pi.press("volumeup")
            
    elif "volume down" in query: 
            pi.press("volumedown")
            pi.press("volumedown")
            pi.press("volumedown")
            pi.press("volumedown")
            pi.press("volumedown")
            
            
    elif "open whatsapp" in query:
            pi.hotkey('win')
            time.sleep(0.2)
            pi.write('whatsapp' ,0.8 )
            time.sleep(0.2)
            pi.press('enter')  
            
    elif "search in start" in query:
            pi.hotkey('win')
            pi.moveTo(120, 748, 0.5)
            pi.click(x=120, y=748, interval=1, button='left')
            
    elif "enter" in query:
            pi.hotkey('enter')
            
    elif "close it" in query:
            pi.hotkey('alt', 'f4')
            
    elif "remove letter" in query:
            pi.hotkey('backspace')
            
    elif "remove word" in query:
            pi.hotkey('ctrl', 'backspace')
            
    
                         
            
   # Add more query handling here...
   

root = tk.Tk()
root.title("MAX - Virtual Assistant")

# Apply a themed style
style = ThemedStyle(root)
style.set_theme("breeze")  # You can choose different themes like 
"clearlooks"
"smog"
"breeze"
"winxpblue"



# Create and configure a frame for the login section
frame_login = ttk.Frame(root)
frame_login.grid(row=0, column=0, padx=10, pady=10)
semi_bold_font = ("Arial", 10, "bold")

# Create a label for user credentials
user_label = ttk.Label(frame_login, text="Username:", font=semi_bold_font)
user_label.grid(row=0, column=0)

# Create an entry field for username
username_entry = ttk.Entry(frame_login)
username_entry.grid(row=0, column=1)
username_entry.focus()  # Set focus on the username entry field initially

# Create a label for password
pass_label = ttk.Label(frame_login, text="Password:", font=semi_bold_font)
pass_label.grid(row=1, column=0)

# Create an entry field for password (use show="*" to hide characters)
password_entry = ttk.Entry(frame_login, show="*")
password_entry.grid(row=1, column=1)

# Create a button to authenticate
auth_button = ttk.Button(frame_login, text="Authenticate", command=lambda: authenticate_user())
auth_button.grid(row=2, column=0, columnspan=2)


# Create a frame for the assistant section
frame_assistant = ttk.Frame(root)
frame_assistant.grid(row=1, column=0, padx=10, pady=10)

def move_to_next(event):
    if event.widget == username_entry:
        password_entry.focus()
    elif event.widget == password_entry:
        auth_button.invoke()  # Invoke the Authenticate button's command

username_entry.bind("<Return>", move_to_next)
password_entry.grid(row=1, column=1)
password_entry.bind("<Return>", lambda event=None: auth_button.focus_set())
password_entry.bind("<Return>", lambda event=None: authenticate_user())

# Create a text box for assistant responses
response_text = tk.Text(frame_assistant, wrap=tk.WORD, width=40, height=10)
response_text.grid(row=0, column=0, columnspan=2)

# Create a button to start the assistant (initially disabled)
start_button = ttk.Button(frame_assistant, text="Start Assistant", command=lambda: start_assistant(), state="disabled")
start_button.grid(row=1, column=0, padx=5, pady=5)

# Create a button to close the assistant (initially disabled)
close_button = ttk.Button(frame_assistant, text="Close Assistant", command=lambda: turn_off(), state="enabled")
close_button.grid(row=1, column=1, padx=5, pady=5)

root.mainloop()