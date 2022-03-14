from tkinter import*
import time
from datetime import datetime
import winsound
import threading
import pygame

# temporary
import random

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
		retVal = 0.02

	return retVal

def playsound(path):
	winsound.PlaySound(path,winsound.SND_ASYNC)

def stopsound():
	winsound.PlaySound(None, winsound.SND_PURGE)

def getScore():
	# TODO: Read accelerometer and calculate Score
	return random.randrange(1,999)

def playSound(score):
	# TODO: play different sounds based on score
	sound = pygame.mixer.Sound(u"assets/sounds/you_suck.wav")
	voice.play(sound)

	while voice.get_busy():
		pass

	sound = pygame.mixer.Sound(u"assets/sounds/songs/scatman.wav")
	voice.play(sound)

gui = Tk() 
gui.title("Boxing Machine GUI")
gui.geometry("350x700") # unnecessary when using fullscreen
gui.config(bg="black") 
#gui.attributes('-fullscreen',True) # Maximize window
#gui.overrideredirect(True) # Make window borderless

icon = PhotoImage(file=u'assets/img/logo.png')
gui.iconphoto(TRUE,icon)

label = Label(gui, font=('bahnschrift', 72), bg="black", fg="#ED302B")
label.pack(expand=True)

# TODO: Implement accelerometer --> calculate score based on accelerometer (velocity=distance/time)
count = 0
score = getScore()
print("Socre:\t", score)

# Just for debugging
start = datetime.now()
print("Start:\t", start)

pygame.mixer.init()
pygame.mixer.set_num_channels(8)
voice = pygame.mixer.Channel(5)

sound = pygame.mixer.Sound(u"assets/sounds/count_score.wav")
voice.play(sound)

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

playSound(score)

# Just for debugging
end = datetime.now()
delta = end - start
print("End:\t", end)
print("Delta:\t", delta.total_seconds() * 1000, " milliseconds")

gui.mainloop()