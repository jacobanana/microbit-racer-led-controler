def on_received_number(receivedNumber):
    global game_finished, track
    if not game_finished:
        for index in range(speed):
            strip.set_pixel_color(players[receivedNumber][0],
                neopixel.colors(NeoPixelColors.BLACK))
            players[receivedNumber][0] += 1
            for p in players:
                strip.set_pixel_color(p[0], neopixel.colors(p[1]))
            strip.show()
            basic.pause(5)

        if players[receivedNumber][0] > track:
            game_finished = True
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    global speed
    speed += 1

def on_button_pressed_b():
    global speed
    speed += -1
    if speed < 1:
        speed = 1

def reset():
    global players
    players = [[0, NeoPixelColors.RED],
        [1, NeoPixelColors.BLUE],
        [2, NeoPixelColors.PURPLE]]
    strip.clear()
    for q in players:
        strip.set_pixel_color(q[0], neopixel.colors(q[1]))
    strip.show()

input.on_button_pressed(Button.A, on_button_pressed_a)
input.on_button_pressed(Button.B, on_button_pressed_b)
input.on_button_pressed(Button.AB, reset)


game_finished: bool = False
speed = 10
track = 300
strip: neopixel.Strip = neopixel.create(DigitalPin.P13, 300, NeoPixelMode.RGB)
players: List[List[number]] = [[0, NeoPixelColors.RED],
    [0, NeoPixelColors.BLUE],
    [0, NeoPixelColors.PURPLE]]
radio.set_group(1)
reset()

def on_forever():
    global game_finished
    for r in players:
        if r[0] >= track:
            strip.show_color(neopixel.colors(r[1]))
            basic.pause(100)
    if game_finished:
        game_finished = False
        soundExpression.happy.play()
basic.forever(on_forever)
