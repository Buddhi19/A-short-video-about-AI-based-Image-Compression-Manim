import cv2
import numpy as np

import os
import sys

main_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(main_dir)

path = os.path.join(main_dir, "Data","1.jpg")

def blur_and_save_image():
    img = cv2.imread(path)
    blurred = cv2.GaussianBlur(img, (65,65), 0)
    cv2.imwrite(os.path.join(main_dir, "Data","1_blurred.jpg"), blurred)

def convert_image_to_black_and_white():
    img = cv2.imread(path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(os.path.join(main_dir, "Data","1_bw.png"), gray)

def print_image_values():
    img = cv2.imread(path)
    # convert the image to grayscale
    b,g,r = cv2.split(img)
    # resize the image to 8x8 pixels
    small = cv2.resize(r, (8,8))
    print(small)

def convert_to_YVU():
    img = cv2.imread(path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
    y,u,v = cv2.split(img)
    cv2.imwrite(os.path.join(main_dir, "Data","1_y.jpg"), y)
    cv2.imwrite(os.path.join(main_dir, "Data","1_u.jpg"), u)
    cv2.imwrite(os.path.join(main_dir, "Data","1_v.jpg"), v)

def convert_to_RGB():
    img = cv2.imread(path)
    b,g,r = cv2.split(img)
    zeros = np.zeros_like(b)
    b = cv2.merge((b,zeros,zeros))
    g = cv2.merge((zeros,g,zeros))
    r = cv2.merge((zeros,zeros,r))
    cv2.imwrite(os.path.join(main_dir, "Data","1_r.png"), r)
    cv2.imwrite(os.path.join(main_dir, "Data","1_g.png"), g)
    cv2.imwrite(os.path.join(main_dir, "Data","1_b.png"), b)



if __name__ == "__main__":
    convert_to_RGB()