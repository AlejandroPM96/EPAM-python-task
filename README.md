# EPAM-python-task

## Running the project:
To run this project follow the next steps:
### Install Requirements
```
pip install -r requirements
```
### Run project
```
export FLASK_APP=application
flask run
```
## Task requirements:

In Python create an API that have next requirements:

Markup : 
* It will be using Get method  
* It will receive a parameter (a string)  
* If the string is a palindrome it will return a json containing  
    * a string (the parameter string)  
    * a boolean (true)  
    * a sorted object (listing different characters and how many time those characters are in the string)  
    * an int (the length of the string)  
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
Markup :
* If the string is not a palindrome it will return a json containing  
    * a string (the parameter string)  
    * a boolean (false)  
```
{
    ""name"": ""example"",
    ""palindrome"": false
}
```