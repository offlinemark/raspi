#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Basic code for triggering code on button press events via polling a pin."""

import RPi.GPIO as gpio
import time

PIN = 17

gpio.setmode(gpio.BCM)
gpio.setup(PIN, gpio.IN, pull_up_down=gpio.PUD_UP)

while True:
    inp = gpio.input(PIN)
    if not inp:
        print 'yeah'
    time.sleep(.2) # 0.2s is a reasonable tradeoff between responsiveness and
                   # processor work intensity
