import machine
import utime



led_red = machine.pin(15, machine.pin.OUT)
led_yellow = machine.pin(14, machine.pin.OUT)
led_green = machine.pin(13, machine.pin.OUT)

while True;


  led_red.value(1)
  utime.sleep(5)
  led_yellow.value(1)
  utime.sleep(2)
  led_red.value(0)
  led_yellow.value(0)
  led_green.value(1)
  utime.sleep(5)
  led_green.value(1)
  utime.sleep(5)
  led_yellow.value(0)
