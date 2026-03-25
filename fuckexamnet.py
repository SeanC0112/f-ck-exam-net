import keyboard as key
import time, pyperclip
from pynput import keyboard as kb

clipboard = ""

def on_activate_i():
    global clipboard
    clipboard = pyperclip.paste()
    print('Clipboard content: ' + clipboard)
    time.sleep(1)
    key.write("hola")


with kb.GlobalHotKeys({
        '<cmd>+<shift>+<tab>': on_activate_i}) as h:
    h.join()
    # keyboard.add_abbreviation('@@', 'my.long.email@example.com')


# while True:
#     print(i)
#     i+=1
#     time.sleep(30)
#     keyboard.write('hi')
#     print(pyperclip.paste())

