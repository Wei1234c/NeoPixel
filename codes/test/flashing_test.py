import time

from machine import Pin
from neopixel import NeoPixel


pin = Pin(13, Pin.OUT)
np = NeoPixel(pin, 60)

np[0] = (1, 0, 0)
np[1] = (0, 1, 0)
np[2] = (0, 0, 1)
np.write()



def cycle(self, cursor_value = (0, 0, 1), wait_ms = 13, transparent = True):
    for i in range(self.n):
        old_value, self[i] = self[i], cursor_value

        self.write()
        # time.sleep_us(300)  # comment out to induce random flashing.
        self.write()

        time.sleep_ms(wait_ms)

        if transparent:
            self[i] = old_value

    self.write()



while True:
    cycle(np)
