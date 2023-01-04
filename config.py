# Speed of mouse movement, in pix/s, only applies to circle
speed = 1000
# timestep is 1/frequency of update in s, 0.01s = 10 ms is 100 updates per second
timestep = 0.01
# mode, 0 is rng, 1 is circle
mode = 0
# delay before jiggler starts in seconds
sleep_delay = 10
# rng jiggler config
jiggle_distance = 50
no_timesteps = 10 # how many timesteps before it changes direction, e.g if timestep is 0.01 and no_timestep is 100, every 1s it will change direction
# circle jiggler config
circle_diameter = 500
