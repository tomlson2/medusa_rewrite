import cv2
import numpy as np

def hsv_range(im, h1, s1, v1, h2, s2, v2):
    hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
    lower = np.array([h1, s1, v1])
    upper = np.array([h2, s2, v2])
    mask = cv2.inRange(hsv, lower, upper)
    result = cv2.bitwise_and(im, im, mask = mask)
    return result

def avg_pixel(im):
    im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    avg_row = np.average(im, axis=0)
    avg_pixel = np.average(avg_row, axis=0)
    return avg_pixel


def draw_rectangles(im, rectangles):
    for x, y, w, h in rectangles:
        pt1 = (x, y)
        pt2 = (x + w, y + h)
        cv2.rectangle(im, pt1, pt2, (0, 255, 0), cv2.LINE_4)