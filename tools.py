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