from wordcloud import WordCloud
from matplotlib.pyplot import *
import sys
import random

COLOR = 'blue'

def color_func(word, font_size, position, orientation, random_state=None):
    if COLOR == 'red':
        return "rgb(%d, 0, 0)" % random.randint(60, 255)
    elif COLOR == 'green':
        return "rgb(0, %d, 0)" % random.randint(60, 255)
    elif COLOR == 'blue':
        return "rgb(0, 0, %d)" % random.randint(60, 255)


text = open(sys.argv[1]).read()

# Ignore single characters, plus list of words
chars = [chr(i) for i in range(97, 97+26)]
ignorewords = chars + ["a","about","above","after","again","against","all","am","an","and","any","are","aren't","as","at","be","because","been","before","being","below","between","both","but","by","can't","cannot","could","couldn't","did","didn't","do","does","doesn't","doing","don't","down","during","each","few","for","from","further","had","hadn't","has","hasn't","have","haven't","having","he","he'd","he'll","he's","her","here","here's","hers","herself","him","himself","his","how","how's","i","i'd","i'll","i'm","i've","if","in","into","is","isn't","it","it's","its","itself","let's","me","more","most","mustn't","my","myself","no","nor","not","of","off","on","once","only","or","other","ought","our","oursourselves","out","over","own","same","shan't","she","she'd","she'll","she's","should","shouldn't","so","some","such","than","that","that's","the","their","theirs","them","themselves","then","there","there's","these","they","they'd","they'll","they're","they've","this","those","through","to","too","under","until","up","very","was","wasn't","we","we'd","we'll","we're","we've","were","weren't","what","what's","when","when's","where","where's","which","while","who","who's","whom","why","why's","with","won't","would","wouldn't","you","you'd","you'll","you're","you've","your","yours","yourself","yourselves"]

wc = WordCloud(background_color='white', font_path="/Library/Fonts/Arial Black.ttf", stopwords=ignorewords, width=1280, height=1280, prefer_horizontal=1.0).generate(text)
imshow(wc.recolor(color_func=color_func, random_state=3))
xticks([])
yticks([])
tight_layout()