#Working code
import os
import matplotlib.pyplot as plt
import numpy as np
import cv2

imgs=[]
# dictionary of hand signs
hand_signs = {
    '1': '1.jpg',
    '2': '2.jpg',
    '3': '3.jpg',
    '4': '4.jpg',
    '5': '5.jpg',
    '6': '6.jpg',
    '7': '7.jpg',
    '8': '8.jpg',
    '9': '9.jpg',
    'a': '10.jpg',
    'b': '11.jpg',
    'c': '12.jpg',
    'd': '13.jpg',
    'e': '14.jpg',
    'f': '15.jpg',
    'g': '16.jpg',
    'h': '17.jpg',
    'i': '18.jpg',
    'j': '19.jpg',
    'k': '20.jpg',
    'l': '21.jpg',
    'm': '22.jpg',
    'n': '23.jpg',
    'o': '24.jpg',
    'p': '25.jpg',
    'q': '26.jpg',
    'r': '27.jpg',
    's': '28.jpg',
    't': '29.jpg',
    'u': '30.jpg',
    'v': '31.jpg',
    'w': '32.jpg',
    'x': '33.jpg',
    'y': '34.jpg',
    'z': '35.jpg'
}

# function to display hand sign image for a letter
def show_hand_sign(letter):
    if letter in hand_signs:
        img1 = cv2.imread(hand_signs[letter])
        print(hand_signs[letter])
        print(img1)
        # Resize the images to the same width
        width = 300
        height = int(width * img1.shape[0] / img1.shape[1])
        img1 = cv2.resize(img1, (width, height))
        imgs.append(img1)

# get input from user
word = input("Enter a word: ")

# iterate through letters in the word and display corresponding hand sign images side by side
for letter in word:
    show_hand_sign(letter.lower())


result = np.hstack(imgs)

# Display the result
plt.imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
plt.show()