#Boolean Math
cardio_done = True
strength_done = False

workouts = cardio_done + strength_done
print(workouts)

#string Evaluation
username = ""
if username:
    print("Welcome " + username)
else:
    print("Please enter a username")