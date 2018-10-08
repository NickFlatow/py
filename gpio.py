#https://gpiozero.readthedocs.io/en/stable 

from gpiozero import LED
#utilize signal framework
from signal import pause

# connect gpio pin 12 to led
led_red = LED(12)
#turn led "on"

led_red.on()

#prevent program from ending immediately 
pause()
