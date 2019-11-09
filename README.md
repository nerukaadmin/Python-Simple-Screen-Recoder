# Python-Simple-Screen-Recoder
Create simple screen  recorder with python3.
Record your Screen in ubuntu using Python.


## Getting Started
Please Follow the steps as below.
1)pip 3 insatll modules.
  *pip3 install numpy opencv-python pyautogui 

### Dependancies.


```
apt-get install python3-tk python3-dev
sudo apt-get install scrot
```

### Create scr.py.

Create scr.py.
```
import cv2
import numpy as np
import time
import pyautogui
import tkinter as tk


root = tk.Tk()

screen_width = root.winfo_screenwidth() #use to get screen resolution
screen_height = root.winfo_screenheight()
#print (screen_width)
#print (screen_height)



SCREEN_SIZE = (screen_width, screen_height)
fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("xxx.avi", fourcc, 25.0, (SCREEN_SIZE)) #cahnge xxx waht evre you want
while True
	img = pyautogui.screenshot()
	frame = np.array(img)
	frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
	out.write(frame)
	#cv2.imshow("screenshot", frame)
	if cv2.waitKey(1) == ord("q"):
		break
cv2.destroyAllWindows()
out.release()







## Author

* **Neruka Lakshitha**  - [nerukaadmin](https://github.com/nerukaadmin)
