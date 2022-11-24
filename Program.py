from sense_hat import SenseHat
import time

s = SenseHat()
s.low_light = True

green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255,255,255)
nothing = (0,0,0)
pink = (255,105, 180)

def  creeper():
    G = green
    Y = yellow
    B = blue
    W = white
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

images = [creeper]
count = 0

while True: 
    s.set_pixels(images[count % len(images)]())
    time.sleep(.75)
    count += 1
