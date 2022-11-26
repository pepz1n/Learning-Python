import pyautogui
from pynput.keyboard import Key, Listener 

def show(key): 

  if key == Key.delete: 
    pyautogui.click(150, 300)
    pyautogui.click(150, 300)
  else:
    print("Aperte DELETE Para Pickar")
    
with Listener(on_press = show) as listener: 
  listener.join() 
