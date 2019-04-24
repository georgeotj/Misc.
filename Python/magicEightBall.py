# Magic Eight Ball
# This little script will take a question and will provide a Yes, No, Maybe, or Other response.

import random

def response(question):
    rng = random.randint(1,8)
    response = "Uh..."
    if rng == 1:
        response = "Yes"
    elif rng == 2:
        response = "No"
    elif rng == 3:
        response = "It is decidedly so"
    elif rng == 4:
        response = "Ask again later"
    elif rng == 5:
        response = "Don't count on it"
    elif rng == 6:
        response = "Concentrate and ask again"
    elif rng == 7:
        response = "Very doubtful"
    elif rng == 8:
        response = "Maybe"
    return response

print("Hello and welcome to the magic eight ball.")
question = input("You may now ask the magic eight ball a question ")
print(response(question))
