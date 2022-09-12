import pyautogui
import time
import datetime


def move_cursor():

   is_active_loop = True
   print("Welcome to  run cursor automatic")
   while is_active_loop:
       now = datetime.datetime.now()
       print("Last run in : ")
       print(now)
       pyautogui.move(0, 10)
       time.sleep(5)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
   move_cursor()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
