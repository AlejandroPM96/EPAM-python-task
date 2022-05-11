# EPAM-python-task

## Task requirements:

In Python create an API that have next requirements:

: It will be using Get method\n
: It will receive a parameter (a string)\n
: If the string is a palindrome it will return a json containing\n
: a string (the parameter string)\n
: a boolean (true)\n
: a sorted object (listing different characters and how many time those characters are in the string)\n
: an int (the length of the string)\n
```
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
```
: If the string is not a palindrome it will return a json containing\n
: a string (the parameter string)\n
: a boolean (false)\n
```
{
    ""name"": ""example"",
    ""palindrome"": false
}
```