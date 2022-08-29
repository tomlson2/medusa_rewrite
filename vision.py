import cv2
import numpy as np

class Model:

    def find(self, model):
        pass


class Needle:
    def __init__(self, needle_path: str = None) -> None:
        self.needle = cv2.imread(needle_path)
        self.w = self.needle.shape[1]
        self.h = self.needle.shape[0]
        self.method = cv2.TM_CCOEFF_NORMED

    def scale_im(self, size=0.2):
        self.w = int(self.w * size)
        self.h = int(self.h * size)
        self.needle = cv2.resize(self.needle, (self.w, self.h))

    def find(self, haystack_im, threshold=0.7):
        res = cv2.matchTemplate(haystack_im, self.needle, self.method)
        max = np.amax(res)

        locations = np.where(res >= threshold)
        locations = list(zip(*locations[::-1]))

        if not locations:
            return np.array([], dtype=np.int32).reshape(0, 4)

        rectangles = []

        for loc in locations:   
            rect = [int(loc[0]), int(loc[1]), self.w, self.h]
            rectangles.append(rect)
            rectangles.append(rect)
        
        rectangles, _ = cv2.groupRectangles(rectangles, 1, 0.5)

        return rectangles
