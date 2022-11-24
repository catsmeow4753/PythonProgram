from sense_hat import SenseHat
import time

s = SenseHat()
s.low_light = True

green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255, 255, 255)
nothing = (0, 0, 0)
pink = (255, 105, 180)

def creeper():
    G = green
    O = nothing
    logo = [
    G, G, G, G, G, G, G, G,
    G, O, O, G, G, O, O, G,
    G, O, O, G, G, O, O, G,
    G, G, G, G, G, G, G, G,
    G, G, G, O, O, G, G, G,
    G, G, O, O, O, O, G, G,
    G, G, O, G, G, O, G, G,
    G, G, G, G, G, G, G, G,
    ]
    return logo
    
def light():
    W = white
    logo = [
    W, W, W, W, W, W, W, W,
    W, W, W, W, W, W, W, W,
    W, W, W, W, W, W, W, W,
    W, W, W, W, W, W, W, W,
    W, W, W, W, W, W, W, W,
    W, W, W, W, W, W, W, W,
    W, W, W, W, W, W, W, W,
    W, W, W, W, W, W, W, W,
    ]
    return logo
    
def boom():
    R = red
    logo = [
    R, R, R, R, R, R, R, R,
    R, R, R, R, R, R, R, R,
    R, R, R, R, R, R, R, R,
    R, R, R, R, R, R, R, R,
    R, R, R, R, R, R, R, R,
    R, R, R, R, R, R, R, R,
    R, R, R, R, R, R, R, R,
    R, R, R, R, R, R, R, R,
    ]
    return logo

images = [creeper, creeper, creeper, light, creeper, light, creeper, light, boom, boom]
count = 0

while True: 
    s.set_pixels(images[count % len(images)]())
    time.sleep(0.5)
    count += 1
