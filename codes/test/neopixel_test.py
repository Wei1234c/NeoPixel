import machine
import math
from neo_pixel import NeoPixel, Element


pin_np = machine.Pin(13, machine.Pin.OUT)
np = NeoPixel(pin = pin_np, n = 60, bpp = 3, timing = True, start_idx = 15)

np[0] = (1, 0, 0)
np[1] = (0, 1, 0)
np[2] = (0, 0, 1)
np[3] = (0, 1, 1)
np[4] = (1, 1, 0)
np[5] = (4, 1, 0)

base = 2
n = 5
colors = [(0, 0, base ** i) for i in range(n)]
element = Element(n = n, colors = colors, transparent = True)
element.dimm(1)

while True:
    np.cycle(element = element, wait_ms = 13)
    # np.cycle(wait_ms = 13)

