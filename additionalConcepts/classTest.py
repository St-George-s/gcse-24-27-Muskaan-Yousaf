import random 

for counter in range (1,11):
    childScore = random.randint(1, 100)
    if childScore < 50:
        gOrB = "Naughty"
        print("Child", counter, "score: ", childScore, "they are considered", gOrB, "so they will get nothing.")
    else:
        gOrB = "Good"
        print("Child", counter, "score: ", childScore, "they are considered", gOrB, "so they will get a present.")