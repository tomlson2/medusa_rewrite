from dataclasses import dataclass
from client import Client
import cv2

class Region:

    def __init__(self, 
    c: Client,
    x: int,
    y: int,
    w: int,
    h: int,
    scale: float = 1.0) -> None:
        self.c = c
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.scale = scale

    def get_image(self):
        im = self.c.get_screenshot(self.x, self.y, self.w, self.h)
        return im
    
    def scale_im(self, im):
        w = int(self.w * self.scale)
        h = int(self.h * self.scale)
        im = cv2.resize(im, (w, h))
        return im
    
    def show_image(self, im):
        cv2.imshow("show_image", im)
        return True
    
    def break_check(self):
        if cv2.waitKey(1) == ord('q'):
            cv2.destroyAllWindows()
            return True