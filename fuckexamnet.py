import keyboard as key
import time, pyperclip
from pynput import keyboard as kb

#store whats on clipboard
clipboard = ""

def on_activate_i():
    global clipboard
    #gets whats on the clipboard
    clipboard = pyperclip.paste()
    print('Clipboard content: ' + clipboard)
    time.sleep(1)
    #writes to the keyboard
    key.write("hola")


#add hotkey
with kb.GlobalHotKeys({
        #the keys you want.    the function you want to call
        '<cmd>+<shift>+<tab>': on_activate_i}) as h:
    h.join()


