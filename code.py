import time
import board
import random
import math
from digitalio import DigitalInOut, Direction, Pull
import usb_hid
# from adafruit_hid.keyboard import Keyboard
# from adafruit_hid.keycode import Keycode
# from adafruit_hid.consumer_control import ConsumerControl
# from adafruit_hid.consumer_control_code import ConsumerControlCode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.mouse import Mouse
from config import *

# remember to put in the library for adafruit_hid and digitalio into the rpi2040


mouse = Mouse(usb_hid.devices)
led = DigitalInOut(board.LED)
led.direction = Direction.OUTPUT
# kbd = Keyboard(usb_hid.devices)
# layout = KeyboardLayoutUS(kbd)

def rng_coords(max_dist = 100):
    # every 100 timesteps, go in a new direction
    # max_dist can be imagined as a rectangle in both directions, e.g 50 would mean 50 in up down left right, i.e 100 x 100 square
    curr_x = 0
    curr_y = 0
    
    while True:
        tgt_x = random.randint(-max_dist, max_dist)
        tgt_y = random.randint(-max_dist, max_dist)
        step_x = tgt_x / no_timesteps 
        step_y = tgt_y / no_timesteps
        next_x = 0
        next_y = 0
        for _ in range(no_timesteps):
            curr_x += step_x
            curr_y += step_y
            
            rem_x = round(curr_x % 1, 2)
            div_x = curr_x // 1
            if abs(div_x) > 0:
                curr_x = rem_x
                next_x = div_x
            
            rem_y = round(curr_y % 1, 2)
            div_y = curr_y // 1
            if abs(div_y) > 0:
                curr_y = rem_y
                next_y = div_y
                
            yield [int(next_x), int(next_y)]
            
            next_x = 0
            next_y = 0
    

def circle_coords(diameter = 250):
    # use speed as linear speed in pix/s
    # convert speed from linear speed in pix/s to angular speed in rad/s
    # apparently circuitpython uses relative coords so this one is broke
    radius = diameter // 2
    angular_speed = speed / radius
    theta = 0
    
    # curr_x and curr_y store the previous position to calculate the relative distance to move
    curr_x = radius * math.cos(theta)
    curr_y = radius * math.cos(theta)
    
    # step_x and step_y store the accumulated distance to move
    step_x = 0
    step_y = 0
    
    # next_x and next_y store the output to move by
    next_x = 0
    next_y = 0
    
    while True:
        theta += angular_speed * timestep
        new_x = radius * math.cos(theta)
        new_y = radius * math.sin(theta)
        step_x += new_x - curr_x  
        step_y += new_y - curr_y
        curr_x = new_x
        curr_y = new_y
        
        
        # if step has accumulated to be more than 1, then move by setting next_x and next_y
        rem_x = round(step_x % 1, 2)
        div_x = step_x // 1
        if abs(div_x) > 0:
            step_x = rem_x
            next_x = div_x
        
        rem_y = round(step_y % 1, 2)
        div_y = step_y // 1
        if abs(div_y) > 0:
            step_y = rem_y
            next_y = div_y
        
        
        yield [int(next_x), int(next_y)]
        next_x = 0
        next_y = 0
        

# mouse.move(x=-5000, y=5000)
# mouse.move(x=100, y=100)

if mode == 0:
    coords_gen = rng_coords(max_dist=jiggle_distance)

if mode == 1:
    coords_gen = circle_coords(diameter=circle_diameter)

for i in range(sleep_delay):
    led.value = False
    time.sleep(0.9)
    led.value = True
    time.sleep(0.1)

while True:
    next_x, next_y = next(coords_gen)
    mouse.move(x=next_x, y=next_y)
    time.sleep(timestep)



# layout.write()


#         led.value = True
#         layout.write(str(one))
#         mouse.click(Mouse.LEFT_BUTTON)
#         led.value = False
#         time.sleep(1.0)  # sleep timer
#         kbd.send(Keycode.BACKSPACE)
#     time.sleep(0.1)
#     kbd.send(Keycode.BACKSPACE)
#     layout.write(str(ten))
# time.sleep(0.1)


