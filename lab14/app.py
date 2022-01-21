from textblob import TextBlob
from typing import List

def hello(name):
    output = f'Hello {name}'
    return output


def extract_sentiment(text):
    text = TextBlob(text)

    return text.sentiment.polarity

def text_contain_word(word: str, text: str):
    return word in text

def bubble_sort(numbers: List):
    for _ in range(len(numbers)):
        changes = False
        for i in range(len(numbers)-1):
            if numbers[i]>numbers[i+1]:
                numbers[i+1], numbers[i] = numbers[i], numbers[i+1]
                changes = True
        if not changes:
            break
    return numbers
