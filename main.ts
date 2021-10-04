radio.onReceivedNumber(function on_received_number(receivedNumber: number) {
    
    if (!game_finished) {
        for (let index = 0; index < speed; index++) {
            strip.setPixelColor(players[receivedNumber][0], neopixel.colors(NeoPixelColors.Black))
            players[receivedNumber][0] += 1
            for (let p of players) {
                strip.setPixelColor(p[0], neopixel.colors(p[1]))
            }
            strip.show()
            basic.pause(5)
        }
        if (players[receivedNumber][0] > track) {
            game_finished = true
        }
        
    }
    
})
function reset() {
    
    players = [[0, NeoPixelColors.Red], [1, NeoPixelColors.Blue], [2, NeoPixelColors.Purple]]
    strip.clear()
    for (let q of players) {
        strip.setPixelColor(q[0], neopixel.colors(q[1]))
    }
    strip.show()
}

input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    speed += 1
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    speed += -1
    if (speed < 1) {
        speed = 1
    }
    
})
input.onButtonPressed(Button.AB, reset)
let game_finished = false
let speed = 10
let track = 300
let strip = neopixel.create(DigitalPin.P13, 300, NeoPixelMode.RGB)
let players = [[0, NeoPixelColors.Red], [0, NeoPixelColors.Blue], [0, NeoPixelColors.Purple]]
radio.setGroup(1)
reset()
basic.forever(function on_forever() {
    
    for (let r of players) {
        if (r[0] >= track) {
            strip.showColor(neopixel.colors(r[1]))
            basic.pause(100)
        }
        
    }
    if (game_finished) {
        game_finished = false
        soundExpression.happy.play()
    }
    
})
