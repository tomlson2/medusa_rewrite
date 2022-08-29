from windowcapture import Client, Region
from vision import Needle
from time import perf_counter
from tools import hsv_range, avg_pixel

c = Client("yolkedgoblin")
r = Region(c, 1388, 477, 408, 559)
n = Needle('needles\\green.png')

while r.break_check() is not True:
    t1 = perf_counter()

    im = r.get_image()
    im = hsv_range(im, 19, 0, 0, 180, 53, 153)
    r.show_image(im)

    t2 = perf_counter()
    print(f'{round(1/(t2-t1))} fps')