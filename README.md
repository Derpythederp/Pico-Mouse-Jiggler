# Jiggler with Pi Pico

Ever just want to go to the take a break without being hounded by your superiors? Here's a malicious compilance hardware tool for you! 

Using a cheap RPI Pico and a bit of Circuitpython, scam any company computer without installing software into thinking you're still hard at work, without using an macros software that might set off antivirus programs.

## Installation guide

![Pi Pico H](https://static.cytron.io/image/cache/catalog/products/RPI-PICO-H/RPI-PICO-H_a-800x800.jpg)
Get your hands on a Pi Pico, its pretty common, but if you're not sure [Cytron](https://sg.cytron.io/) is a good place to start.
Follow the installation guide for [CircuitPython on Pi Pico](https://circuitpython.org/board/raspberry_pi_pico/)

Hold down BOOTSEL button and connect USB cable to computer.
Pull this repo and drag all the folders into the Pi Pico.

The next time you connect your Pi Pico, once the warning LED lights counts to 0, you'll never be idle again.

# Config fields
Do remember to change this especially the idle timing (default=10s), since I was too lazy to get a push button, it works based on a countdown.
