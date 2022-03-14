from tkinter import*
import time
from datetime import datetime
import winsound
# imports for microchip
#import board
#import busio
#import adafruit_adxl34x

def getSleepTime(dif):
	retVal = 0
	
	if dif == 0:
	  retVal = 1.2
	  
	if dif == 1:
		retVal = 1

	elif dif == 2:
		retVal = 0.5

	elif dif == 3:
		retVal = 0.3
	
	elif dif < 5:
		retVal = 0.25

	elif dif < 20:
		retVal = 0.1

	elif dif < 25:
		retVal = 0.05

	elif dif <= 50:
		retVal = 0.04

	return retVal

def playsound(path):
	winsound.PlaySound(path,winsound.SND_ASYNC)

def stopsound():
	winsound.PlaySound(None, winsound.SND_PURGE)

gui = Tk() 
gui.geometry("700x700")
gui.config(bg="black") 
#gui.attributes('-fullscreen',True) # Maximize window
#gui.overrideredirect(True) # Make window borderless

label = Label(gui, font=('bahnschrift', 72), bg="black", fg="#ED302B")
label.anchor('center')
label.pack()

# TODO: Implement accelerometer --> calculate score based on accelerometer (velocity=distance/time)
score = 972
count = 0

if score > 999:
	score = 999
	
# Just for debugging
start = datetime.now()
print("Start:\t", start)

playsound(u"sounds/count_score.wav")

while count < score:
	count += 1
	label.config(text=count)
	
	if score-count > 50:
		if count % 2 == 0:
			# TODO: check how many deimal places time.sleep can handle
			time.sleep(0.000000000000005)
			gui.update()
	else:
		gui.update()
		dif = score-count
		sleep = getSleepTime(dif)
		time.sleep(sleep)
	pass

# TODO: Play different sounds --> low score: "You can do better" / high score: "wooow!"
playsound(u"sounds/jackpot.wav")

# Just for debugging
end = datetime.now()
delta = end - start
print("End:\t", end)
print("Delta:\t", delta.total_seconds() * 1000, " milliseconds")

gui.mainloop()