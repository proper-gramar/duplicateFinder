# https://www.geeksforgeeks.org/measure-similarity-between-images-using-python-opencv/
# python program to check a given library for duplicates, and remove them.
import cv2
import os
import shutil

# 11/7/2020 - Conceptually works, can tell if image[0] & image[1] are duplicates or unique
# facing index out of bounds error - line 47
# Data structure needs to be changed for faster runtime



# finding histograms
# histograms are graphs of a distribution of data designed to show centering, dispersion(spread),
# and shape(relative frequency) of the data. Histograms provide a visual display of large amounts of data

# store each histogram in a dictionary, compare data in O(log N)?

# storing in list/array for time being...
image_array = []


def main():
    filepath = 'images'
    # storing our serialized photos
    looper(filepath)

    # comparing photos
    for histogram in image_array:
        # terrible conversion. string of the converted int + 1
        compare(histogram, image_array)


def image_to_histogram(image_name):
    i = 0
    # takes string file name as argument
    image = cv2.imread(image_name)
    # gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    histogram = cv2.calcHist(image, [0], None, [256], [0, 256])
    # stores key as int converted to string, converts, then increments.
    # compare method may have to convert for key referencing
    image_array.append(histogram)
    while len(image_array) > i+1:
        for histogram in image_array:
            compare(histogram, image_array[i+1])
            i += 1


# compares photos for similarity
def compare(base_image, compare_image):
    c1, c2 = 0, 0

    # calculate Euclidean Distance between photos
    # base photo
    i = 0
    while i < len(base_image):
        c1 += (base_image[i]) ** 2
        i += 1
    c1 = c1 ** (1 / 2)

    # compare photo
    i = 0
    while i < len(compare_image):
        c2 += (compare_image[i]) ** 2
        i += 1
    c2 = c2 ** (1 / 2)

    if c1 == c2:
        print("images are duplicates")
    else:
        print("images are different")


def looper():
    # loops through directory to serialize photos
    for file in os.listdir("images"):
        if file.lower().endswith(('.png', '.jpg')):
            image_name = "images/" + str(file)
            image_to_histogram(image_name)


filepath = 'images'
looper()

