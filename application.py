from flask import Flask
from flask import request

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

def isPalindrome(word:str):
    """Check if the word sent is a palindrome

    Examples of palindrome words:
    analina
    noon

    Args: 
        word: string
    
    Return:
        bool: True if the word is palindrome or False if not
    """
    reversed_word = word[::-1]
    return True if reversed_word == word else False

def makeSortedArray(word:str):
    """Creates the sorted array of the frequency of characters in the palindrome word

    Args: 
        word: string
    
    Return:
        dict: The object with the sorted keys in descending order with the frequency of the letter
    """
    letters = list(word)
    letter_count = {}
    for letter in letters:
        if letter not in letter_count:
            letter_count[letter] = 1
        else:
            letter_count[letter] += 1
    sorted_array = {_letter: count for _letter, count in sorted(letter_count.items(), key=lambda item: item[1], reverse=True)}
    return sorted_array

@app.route("/palindrome")
def getPalindrome():
    """
    The endpoint for checking if a word is palindrome or not

    **Example request**
        .. sourcecode:: http

            GET /palindrome?word=anilina
            HOST: example.com
            ACCEPT: application/json

    Example Response:
    {
        "name": "anilina",
        "palindrome": true,
        "sorted": {
            "a": 2,
            "i": 2,
            "l": 1,
            "n": 2
        },
        "length": 7
    }
    """
    word = request.args.get('word')
    is_palindrome = isPalindrome(word)
    if is_palindrome:
        return {"name":word, "palindrome": is_palindrome, "sorted":  makeSortedArray(word), "length": len(word)}, 200
    else:
        return {"name":word, "palindrome": is_palindrome}