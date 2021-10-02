radio.onReceivedNumber(function on_received_number(receivedNumber: number) {
    
    if (receivedNumber == 0) {
        strip.setPixelColor(red, neopixel.colors(NeoPixelColors.Black))
        red += speed
        strip.setPixelColor(red, neopixel.colors(NeoPixelColors.Red))
    } else if (receivedNumber == 1) {
        strip.setPixelColor(blue, neopixel.colors(NeoPixelColors.Black))
        blue += speed
        strip.setPixelColor(blue, neopixel.colors(NeoPixelColors.Blue))
    } else {
        strip.setPixelColor(purple, neopixel.colors(NeoPixelColors.Black))
        purple += speed
        strip.setPixelColor(purple, neopixel.colors(NeoPixelColors.Purple))
    }
    
    if (blue >= track) {
        strip.showColor(neopixel.colors(NeoPixelColors.Blue))
    } else if (red >= track) {
        strip.showColor(neopixel.colors(NeoPixelColors.Red))
    } else if (purple >= track) {
        strip.showColor(neopixel.colors(NeoPixelColors.Purple))
    } else {
        
    }
    
    strip.show()
})
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    speed += 1
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    reset()
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    speed += -1
    if (speed < 1) {
        speed = 1
    }
    
})
function reset() {
    
    purple = 0
    blue = 1
    red = 2
    strip.clear()
    strip.setPixelColor(red, neopixel.colors(NeoPixelColors.Red))
    strip.setPixelColor(blue, neopixel.colors(NeoPixelColors.Blue))
    strip.setPixelColor(purple, neopixel.colors(NeoPixelColors.Purple))
    strip.show()
}

let purple = 0
let blue = 0
let red = 0
let track = 0
let speed = 0
let strip : neopixel.Strip = null
radio.setGroup(1)
strip = neopixel.create(DigitalPin.P13, 300, NeoPixelMode.RGB)
reset()
speed = 3
track = 300
basic.forever(function on_forever() {
    
})
