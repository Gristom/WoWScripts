from pynput.keyboard import Key, Controller
import time
from random import randrange

keyboard = Controller()

while True:

    time.sleep(randrange(292))

    x = randrange(2)
    print(x)

    if x == 0:

        keyboard.press('w')  
        keyboard.release('w')  

    elif x == 1:

        keyboard.press(Key.space)
        keyboard.release(Key.space)  
