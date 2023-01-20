import random

# List of all the people
people = ["Liam Mucha", "Jenny", "Martin", "Philip", "Matheo", "Ervan", "Aleksander", "Markus", "Loke A", "Mohammed", "Liam A", "Lukas"]

# Number of groups
num_groups = 4

# Create an empty list to store the groups
groups = [[] for i in range(num_groups)]

# Assign fixed people to the groups
fixed_people = ["Nicholas", "Rafael", "Jens", "Leander", "Anton", "Theodor", "Oscar", "William I"]
for i in range(num_groups):
    groups[i].extend(fixed_people[i*2:i*2+2])

# Shuffle the remaining people
random.shuffle(people)

# Assign remaining people to the groups
for i, person in enumerate(people):
    groups[i % num_groups].append(person)

# Print the groups
for i, group in enumerate(groups):
    print(f"Runar {i+1}: {group}")

