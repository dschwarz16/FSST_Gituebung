"""
Backend for the FSST Gituebung project.
This module contains the backend logic for the project, handling the number generation and comparing
"""


import random

def generate_number():
    """
    Generates a random number between 1 and 100
    :return: int
    """
    return random.randint(1, 100)

if __name__ == "__main__":
    number = generate_number()
    print ("Welcome to the number guessing game!, I have selected a number between 1 and 100.")
    print ("But you can't guess it yet")

