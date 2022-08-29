from dataclasses import dataclass
from typing import Tuple
import win32gui, win32ui, win32con
import numpy as np
import cv2


class Client:
    def __init__(self, name: str, rect: Tuple = (0, 0, 1912, 1110)) -> None:
        self.name = name
        self.x = rect[0]
        self.y = rect[1]
        self.w = rect[2]
        self.h = rect[3]
        self.hwnd = self.find_window()
        self.move_window(rect)
        print("Client loaded")

    def find_window(self):
        return win32gui.FindWindow(None, self.name)
    
    def move_window(self, rect: Tuple):
        x, y, w, h = rect
        win32gui.MoveWindow(self.hwnd, x, y, w, h, True)
    
    def get_screenshot(self, x, y, w, h):
        wDC = win32gui.GetWindowDC(self.hwnd)
        dc = win32ui.CreateDCFromHandle(wDC)
        cDC = dc.CreateCompatibleDC()
        dataBitMap = win32ui.CreateBitmap()
        dataBitMap.CreateCompatibleBitmap(dc, w, h)
        cDC.SelectObject(dataBitMap)
        cDC.BitBlt((0, 0), (w, h), dc, (x, y), win32con.SRCCOPY)

        signedIntsArray = dataBitMap.GetBitmapBits(True)
        im = np.frombuffer(signedIntsArray, dtype='uint8')
        im.shape = (h, w, 4)

        # free resources
        dc.DeleteDC()
        cDC.DeleteDC()
        win32gui.ReleaseDC(self.hwnd, wDC)
        win32gui.DeleteObject(dataBitMap.GetHandle())

        im = im[...,:3]
        
        im = np.ascontiguousarray(im)
        return im
 

@dataclass
class Region:
    c: Client
    x: int
    y: int
    w: int
    h: int
    scale: float = 1.0

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