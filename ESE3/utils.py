import cv2
import numpy as np
from PIL import Image

def convert_to_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def apply_canny(image):
    return cv2.Canny(image, 100, 200)

def apply_blur(image):
    return cv2.GaussianBlur(image, (11, 11), 0)

def apply_sharpen(image):
    kernel = np.array([[0, -1, 0], [-1, 5,-1], [0, -1, 0]])
    return cv2.filter2D(image, -1, kernel)

def apply_emboss(image):
    kernel = np.array([[0, -1, -1], [1, 0, -1], [1, 1, 0]])
    return cv2.filter2D(image, -1, kernel)

def plot_histogram(image):
    color = ('b', 'g', 'r')
    hist_data = {}
    for i, col in enumerate(color):
        hist = cv2.calcHist([image], [i], None, [256], [0, 256])
        hist_data[col] = hist
    return hist_data
