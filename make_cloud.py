"""Produces word cloud from text file, using Python.

Originally designed for producing word clouds for political party manifestos
for the UK 2015 General Election, but can be used for pretty-much anything.

Simple code, but handy to keep for next time I want to use it
"""
import sys
import random

from wordcloud import WordCloud
from matplotlib.pyplot import imshow, xticks, yticks, tight_layout


def color_func(word, font_size, position, orientation, random_state=None):
    if COLOR == 'red':
        return "rgb(%d, 0, 0)" % random.randint(60, 255)
    elif COLOR == 'green':
        return "rgb(0, %d, 0)" % random.randint(60, 255)
    elif COLOR == 'blue':
        return "rgb(0, 0, %d)" % random.randint(60, 255)

# Take the text from the file given as the first command-line argument
text = open(sys.argv[1]).read()

# Take the colour (currently only 'red', 'green' or 'blue') from the second
# command-line argument
COLOR = sys.argv[2]

# Ignore single characters, plus list of words provided in separate file
chars = [chr(i) for i in range(97, 97 + 26)]

words = []
with open('ignorewords.txt', 'r') as f:
    for line in f:
        words.append(line.strip())

ignorewords = chars + words

# Configure the word cloud generation
wc = WordCloud(background_color='white',
               # THIS MAY NEED CHANGING FOR YOUR SYSTEM
               font_path="/Library/Fonts/Arial Black.ttf",
               stopwords=ignorewords,
               width=1280, height=1280,
               prefer_horizontal=1.0)

# Actually generate the cloud
wc.generate(text)

# Display using Matplotlib
imshow(wc.recolor(color_func=color_func, random_state=3))
xticks([])
yticks([])
tight_layout()
