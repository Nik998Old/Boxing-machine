from tkinter import*
from datetime import datetime
import time
import pygame
import random

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

def getScore():
	return random.randrange(1,999)

def playSound(score):
	sound = pygame.mixer.Sound(u'assets/sounds/you_suck.wav')
	voice.play(sound)

	while voice.get_busy():
		time.sleep(0.000000000000005)
		pass

	sound = pygame.mixer.Sound(u'assets/sounds/songs/scatman.wav')
	voice.play(sound)

gui = Tk() 
gui.title('Boxing Machine GUI')
gui.geometry('350x700')
gui.config(bg='black') 

label = Label(gui, font=('bahnschrift', 72), bg='black', fg='#ED302B')
label.pack(expand=True)

count = 0
score = getScore()
print('Socre:\t', score)

# Just for debugging
start = datetime.now()
print('Start:\t', start)

pygame.mixer.init()
pygame.mixer.set_num_channels(8)
voice = pygame.mixer.Channel(5)

sound = pygame.mixer.Sound(u'assets/sounds/count_score.wav')
voice.play(sound)

while count < score:
	count += 1
	label.config(text=count)
	
	if score-count > 50:
		if count % 2 == 0:
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
print('End:\t', end)
print('Delta:\t', delta.total_seconds() * 1000, ' milliseconds')

gui.mainloop()
