import keyboard as key
import time, pyperclip
from pynput import keyboard as kb
# import openai

#store whats on clipboard
clipboard = ""

#api_key = "" #insert openai api key here
# openai.api_key = api_key

def on_activate_i():
    global clipboard
    #gets whats on the clipboard
    clipboard = pyperclip.paste()
    print('Clipboard content: ' + clipboard)
    # openai_response = openai.Completion.create(
    #     model="text-davinci-003",
    #     prompt=clipboard,
    #     temperature=0.5,
    #     max_tokens=1000)
    time.sleep(1)
    #writes to the keyboard
    key.write("hola")
    # key.write(openai_response.choices[0].text)


#add hotkey
with kb.GlobalHotKeys({
        #the keys you want.    the function you want to call
        '<cmd>+<shift>+<tab>': on_activate_i}) as h:
    h.join()


