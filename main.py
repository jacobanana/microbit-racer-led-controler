def on_received_number(receivedNumber):
    global red, blue, purple
    if receivedNumber == 0:
        strip.set_pixel_color(red, neopixel.colors(NeoPixelColors.BLACK))
        red += speed
        strip.set_pixel_color(red, neopixel.colors(NeoPixelColors.RED))
    elif receivedNumber == 1:
        strip.set_pixel_color(blue, neopixel.colors(NeoPixelColors.BLACK))
        blue += speed
        strip.set_pixel_color(blue, neopixel.colors(NeoPixelColors.BLUE))
    else:
        strip.set_pixel_color(purple, neopixel.colors(NeoPixelColors.BLACK))
        purple += speed
        strip.set_pixel_color(purple, neopixel.colors(NeoPixelColors.PURPLE))
    if blue >= track:
        strip.show_color(neopixel.colors(NeoPixelColors.BLUE))
    elif red >= track:
        strip.show_color(neopixel.colors(NeoPixelColors.RED))
    elif purple >= track:
        strip.show_color(neopixel.colors(NeoPixelColors.PURPLE))
    else:
        pass
    strip.show()
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    global speed
    speed += 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    reset()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global speed
    speed += -1
    if speed < 1:
        speed = 1
input.on_button_pressed(Button.B, on_button_pressed_b)

def reset():
    global purple, blue, red
    purple = 0
    blue = 1
    red = 2
    strip.clear()
    strip.set_pixel_color(red, neopixel.colors(NeoPixelColors.RED))
    strip.set_pixel_color(blue, neopixel.colors(NeoPixelColors.BLUE))
    strip.set_pixel_color(purple, neopixel.colors(NeoPixelColors.PURPLE))
    strip.show()


purple = 0
blue = 0
red = 0
track = 0
speed = 0
strip: neopixel.Strip = None
radio.set_group(1)
strip = neopixel.create(DigitalPin.P13, 300, NeoPixelMode.RGB)
reset()
speed = 3
track = 300

def on_forever():
    pass
basic.forever(on_forever)
