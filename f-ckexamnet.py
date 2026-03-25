# Disclaimer: I do not intend this piece of code to be used for cheating or academic
# dishonesty of any kind. I personally have not and never will use this software 
# for cheating in examnet. I instead would like people to know about this vulnerability 
# so that they are able to demonstrate to teachers or administrators that examnet 
# isn't secure and shouldn't be used in class specifically for urban high school and 
# possibly lwhs if i get around to it).

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
    #prints whats on the clipboard
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
        #the keys you want : the function you want to call
        '<cmd>+<shift>+<tab>': on_activate_i}) as h:
    h.join()


