import mouse, keyboard
from time import sleep
while True:
    if mouse.is_pressed(button='left'):
        while not (keyboard.is_pressed('f')):
            sleep(00.50)

            mouse.double_click(button='left')