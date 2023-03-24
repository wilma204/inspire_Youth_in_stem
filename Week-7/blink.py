import machine
import time


led_Pin=machine.Pin(2, machine.Pin.OUT)
while True:
    led_Pin.value(1)
    print("Turning ON again...")
    time.sleep(1)
    led_Pin.value(0)
    print("Turning OFF again...")
    time.sleep(1)
    