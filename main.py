import time
import datetime
from pyautogui import press, typewrite, hotkey



def press_key():

   is_active_loop = True
   print("Welcome to  run cursor automatic")
   while is_active_loop:
       now = datetime.datetime.now()
       print("Last run in : ")
       print(now)
       press('q')
       time.sleep(5)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
   press_key()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
