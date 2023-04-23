import random

num_decisions = 5 * 365 * 50 # Total number of decisions made in a lifetime
num_right_decisions = 5 * 365 * 50 // 2 # Number of right decisions made in a lifetime (assuming equal probability)
num_wrong_decisions = num_right_decisions # Number of wrong decisions made in a lifetime (assuming equal probability)

right_decisions = 0
wrong_decisions = 0
age = 25

while right_decisions < num_right_decisions and wrong_decisions < num_wrong_decisions:
    decision = random.choice(["right", "wrong"])
    if decision == "right":
        right_decisions += 1
    else:
        wrong_decisions += 1
    age += 1

print("At age", age, "you surpassed the number of", num_right_decisions, "right decisions and made", right_decisions, "right decisions and", wrong_decisions, "wrong decisions so far.")
