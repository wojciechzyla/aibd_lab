
from app import hello
from app import extract_sentiment
from app import text_contain_word
from app import bubble_sort
import pytest


def test_hello():
    got = hello("Aleksandra")
    want = "Hello Aleksandra"

    assert got == want

testdata1 = ["I think today will be a great day"]

@pytest.mark.parametrize('sample', testdata1)
def test_extract_sentiment(sample):

    sentiment = extract_sentiment(sample)

    assert sentiment > 0

testdata2 = [
    ('There is a duck in this text', 'duck', True),
    ('There is nothing here', 'duck', False)
    ]

@pytest.mark.parametrize('sample, word, expected_output', testdata2)
def test_text_contain_word(sample, word, expected_output):

    assert text_contain_word(word, sample) == expected_output


testdata3 = [
    ([1,23,26,37,50,100,340,900],[1,23,26,37,50,100,340,900]),
    ([900,340,100,50,37,26,23,1],[1,23,26,37,50,100,340,900]),
    ([37,100,1,900,23,340,26,50],[1,23,26,37,50,100,340,900])
    ]

@pytest.mark.parametrize('sample, expected', testdata3)
def test_bubble_sort(sample, expected):

    assert bubble_sort(sample) == expected