import cv2
import numpy as np
import time
import pyautogui
i

root = tk.Tk()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
#print (screen_width)
#print (screen_height)



SCREEN_SIZE = (screen_width, screen_height)
fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("xxx.avi", fourcc, 25.0, (SCREEN_SIZE))
while True:
	img = pyautogui.screenshot()
	frame = np.array(img)
	frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
	out.write(frame)
	#cv2.imshow("screenshot", frame)
	if cv2.waitKey(1) == ord("q"):
		break
cv2.destroyAllWindows()
out.release()

