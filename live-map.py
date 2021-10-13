import cv2
import numpy as np
import time
import pyautogui
import pytesseract as tess
from PIL import Image
import re
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import keyboard

bottom_left = (4300, 0)
bottom_right = (14416, 0)
top_left = (4300, 10100)
top_right = (14416, 10100)

normized_bot_l = (bottom_left[0] - 4300, bottom_left[1])
normized_bot_r = (bottom_right[0] - 4300, bottom_right[1])
normized_top_l = (top_left[0] - 4300, top_left[1])
normized_top_r = (top_right[0] - 4300, top_right[1])

print(normized_bot_l)
print(normized_bot_r)
print(normized_top_l)
print(normized_top_r)

# 1581, 30  bot_left_co
# 1581, 0   top_left_co
# 1919, 0   top_right_co
# 1919, 30  bot_right_co

def screenshot():
    image = pyautogui.screenshot(region=(1665, 19, 238, 16))    
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    cv2.imwrite("image.png", image)

def get_coordinates(last_x, last_y):
    img = Image.open("image.png")
    text = tess.image_to_string(img)
    coordinates = text.split(" ")
    x = "-1"
    y = "-1"

    if len(coordinates) >= 1:
        p = re.findall("[0-9]+,[0-9]+", coordinates[0])
        if p:
            [x] = p[:1]
            x = x.replace(",", ".")
            num_x = 0
            try:
                num_x = float(x)
                if len(last_x) < 2 or (abs(num_x - last_x[len(last_x) - 1]) < 500 and abs(num_x - last_x[len(last_x) - 2]) < 500):
                    last_x.insert(0, num_x)
            except ValueError:
                pass
    if len(coordinates) >= 2:
        p = re.findall("[0-9]+,[0-9]+", coordinates[1])
        if p:
            [y] = p[:1]
            y = y.replace(",", ".")
            num_y = 0
            try:
                num_y = float(y)
                if len(last_y) < 2 or (abs(num_y - last_y[len(last_y) - 1]) < 500 and abs(num_y - last_y[len(last_y) - 2]) < 500):
                    last_y.insert(0, num_y)
            except ValueError:
                pass
    
    if len(last_x) > 2:
        last_x.pop()
    if len(last_y) > 2:
        last_y.pop()

    return (last_x, last_y)

def show_img(plt, ax, fig, point, x, y):
    point.remove()
    point, = ax.plot(x, y, "o", c="red", ms=10)
    fig.canvas.draw()
    plt.pause(0.3)
    return point


def init():
    last_x = []
    last_y = []
    start_x = float(input("start x: "))
    start_y = float(input("start y: "))
    last_x.append(start_x)
    last_x.append(start_x)
    last_y.append(start_y)
    last_y.append(start_y)
    return last_x, last_y


def main():
    img = mpimg.imread("map_full.png")
    fig = plt.figure()
    plt.imshow(img)
    ax = fig.gca()
    fig.show()

    last_x, last_y = init()
    [start_x] = last_x[:1]
    [start_y] = last_y[:1]
    point, = ax.plot(start_x/10116*1260, start_y/10100*1260, "o", c="red")
    
    while(not keyboard.is_pressed("f1")):
        screenshot()
        [before_x] = last_x[:-1]
        [before_y] = last_y[:-1]
        last_x, last_y = get_coordinates(last_x, last_y)
        [x] = last_x[:-1]
        x -= 4300
        [y] = last_y[:-1]

        if before_x - 4300 != x or before_y != y:
            x_plot = (x / 10116) * 1260
            y_plot = (y / 10100) * 1260
            y_plot = 1260 - y_plot

            point = show_img(plt, ax, fig, point, x_plot, y_plot)
            print(str(last_x) + ",   " + str(last_y))
        plt.pause(0.1)



if __name__ == "__main__":
    main()