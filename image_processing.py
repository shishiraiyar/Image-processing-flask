from PIL import Image
import numpy as np
from math import sqrt

kernel_gauss = [[1 / 16, 1 / 8, 1 / 16], [1 / 8, 1 / 4, 1 / 8], [1 / 16, 1 / 8, 1 / 16]]
kernel_mean = [[1/9, 1/9, 1/9], [1/9, 1/9, 1/9], [1/9, 1/9, 1/9]]

im1 = Image.open("rose_half.jpg")
image = np.asarray(im1)


def greyscale(img):
    img2 = np.copy(img)
    for row in range(len(img)):
        for column in range(len(img[row])):
            red = img[row][column][0]
            green = img[row][column][1]
            blue = img[row][column][2]
            grey = 0.299 * red + 0.587 * green + 0.114 * blue
            img2[row][column][0] = grey
            img2[row][column][1] = grey
            img2[row][column][2] = grey
        print(f"Processing row : {row}")
    return img2


def convolution(img, kernel):
    img2 = np.copy(img)
    for row in range(1, len(img) - 1):
        for column in range(1, len(img[row]) - 1):
            red_new = 0
            green_new = 0
            blue_new = 0
            for i in [0, 1, 2]:
                for j in [0, 1, 2]:
                    red_new += kernel[i][j] * img[row + i - 1][column + j - 1][0]
                    green_new += kernel[i][j] * img[row + i - 1][column + j - 1][1]
                    blue_new += kernel[i][j] * img[row + i - 1][column + j - 1][2]

                    red_new = checkIntensity(red_new)
                    green_new = checkIntensity(green_new)
                    blue_new = checkIntensity(blue_new)

            img2[row][column][0] = red_new
            img2[row][column][1] = green_new
            img2[row][column][2] = blue_new
        # print(f"Processing row : {row}")
    Image.fromarray(image).save("lol.png")
    return img2

def checkIntensity(intensity):
    if intensity>255:
        return 255
    if intensity<0:
        return 0
    return intensity

def sobel(img):
    kernel_edge_ver = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]
    kernel_edge_hor = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
    img2 = np.copy(img)
    for row in range(1, len(img) - 1):
        for column in range(1, len(img[row]) - 1):
            val_ver = 0
            val_hor = 0
            for i in [0, 1, 2]:
                for j in [0, 1, 2]:
                    val_ver += kernel_edge_ver[i][j] * img[row + i - 1][column + j - 1][0]
                    val_hor += kernel_edge_hor[i][j] * img[row + i - 1][column + j - 1][0]
            new_val = sqrt(val_ver ** 2 + val_hor ** 2)
            if new_val > 255:
                new_val = 255
            if new_val < 0:
                new_val = 0

            img2[row][column][0] = new_val
            img2[row][column][1] = new_val
            img2[row][column][2] = new_val
        print(f"Processing row : {row}")
    return img2

# sfkdsklf = convolution(image, kernel_mean)
# Image._show(Image.fromarray(sfkdsklf))

# grey_img = greyscale(image)
# Image._show(Image.fromarray(grey_img))

# mean_blurred = convolution(grey_img, kernel_mean)
# Image._show(Image.fromarray(mean_blurred))

# gaussian_blurred = convolution(grey_img, kernel_gauss)
# Image._show(Image.fromarray(gaussian_blurred))

# twice_gaussian_blurred = convolution(gaussian_blurred, kernel_gauss)
# Image._show(Image.fromarray(twice_gaussian_blurred))

# edge_detection = sobel(twice_gaussian_blurred)
# Image._show(Image.fromarray(edge_detection))



