import random

# Constants
DECISIONS_PER_DAY = 5
DAYS_PER_YEAR = 365
AGE_OF_RETIREMENT = 50

# Initialize variables
age = 0
right_decisions = 0
wrong_decisions = 0
total_decisions = 0
right_decision_ratio = 0.5

# Loop through each year of the person's life
while age < AGE_OF_RETIREMENT:
    # Calculate the number of decisions to make this year
    decisions_this_year = DECISIONS_PER_DAY * DAYS_PER_YEAR
    
    # Loop through each decision and make a random choice
    for i in range(decisions_this_year):
        # Update the right and wrong decision counts
        if random.random() < right_decision_ratio:
            right_decisions += 1
        else:
            wrong_decisions += 1
        
        # Update the total decision count
        total_decisions += 1
        
        # Check if the person has made more wrong decisions than right decisions
        if wrong_decisions > right_decisions:
            print(f"You're done at age {age}. You made {right_decisions} right decisions and {wrong_decisions} wrong decisions.")
            quit()
    
    # Increase the ratio of right decisions every 3 years
    if age % 3 == 0 and age > 0:
        right_decision_ratio += 0.05
    
    # Increment the age
    age += 1

# Print the final results
print(f"At age {age}, you made {right_decisions} right decisions and {wrong_decisions} wrong decisions.")
