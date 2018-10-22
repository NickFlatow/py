# utilize pygame framework
import pygame
# utilize gpio zero framework to interface gpio
from gpiozero import LED, Button
# utilize time framework
from time import sleep

# connect GPIO pin 12 to led
led_red = LED(12)
# connect GPIO pin 4 to button
button_red = Button(4)
# connect GPIO pin 12 to led
led_green = LED(19)
# connect GPIO pin 4 to button
button_green = Button(25)

# define colors using RGB values
red = [255, 0, 0]
green = [0, 255, 0]
black = [60, 60, 60]

def main():
	# when button is pressed call function
	button_red.when_pressed = show_red
	# when button is released call function
	button_red.when_released = hide_red
	# when button is pressed call function
	button_green.when_pressed = show_green
	# when button is released call function
	button_green.when_released = hide_green
	
	# create program loop
	running = True
	while running:
		# event handling gets all events from queue
		for event in pygame.event.get():
			if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
				running = False
			# if "r" is pressed
			elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
				show_red()
			# if "r" is released
			elif event.type == pygame.KEYUP and event.key == pygame.K_r:
				hide_red()
			# if "g" is pressed
			elif event.type == pygame.KEYDOWN and event.key == pygame.K_g:
				show_green()
			# if "g" is released
			elif event.type == pygame.KEYUP and event.key == pygame.K_g:
				hide_green()
		sleep(.2)
	destroy()

def show_red():
	fill_background(red)
	#led_red.on()
	# blink(on time seconds, off time in seconds, number of times to blink (None to run forever), run as background thread)
	led_red.blink(.25, .25, None, True)
	
def hide_red():
	fill_background(black)
	led_red.off()
	
def show_green():
	fill_background(green)
	led_green.on()
	
def hide_green():
	fill_background(black)
	led_green.off()

def destroy():
	print("cleanup")
	pygame.quit()

def fill_background(color):
	screen.fill(color)
	pygame.display.update()

try:
	# initialize pygame
	pygame.init()
	pygame.display.set_caption("Red / Green")
	screen = pygame.display.set_mode((400, 400))
	fill_background(black)
	main()
except KeyboardInterrupt: # end when ctrl-c is pressed
	destroy()
