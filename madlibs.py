story_template = "Bro it’s {adjective} May and the heat is literally acting like a {noun} 😭. We stepped outside for {number} minutes and instantly started {verb_ing} like {animal_plural}. The sun said “today I will be {adjective2}” and we all just accepted our {adjective3} fate. Someone suggested going to {place}, but the road itself felt like {food} on a pan. Meanwhile {name} showed up with a {thing} thinking it would fix everything 💀. End result: we’re all {adjective4}, drinking {drink}, and questioning our {noun2}."

# Beginning of the game
print("========================================")
print("   WELCOME TO THE TIME-TRAVEL MAD LIB!  ")
print("========================================\n", "Story Template: ")
print(story_template, "\n")

# Inputs from user
adjective = input("Enter a adjective here: ")
noun = input("Enter a noun here: ")
number = input("Enter a number here: ")
verb_ing = input("Enter a verb_ing here: ")
animal_plural = input("Enter a animal_plural here: ")
adjective2 = input("Enter a adjective2 here: ")
adjective3 = input("Enter a adjective3 here: ")
place = input("Enter a place here: ")
food = input("Enter a food here: ")
name = input("Enter a name here: ")
thing = input("Enter a thing here: ")
adjective4 = input("Enter a adjective4 here: ")
drink = input("Enter a drink here: ")
noun2 = input("Enter a noun2 here: ")

# User story
madlib = f"Bro it’s {adjective} May and the heat is literally acting like a {noun} 😭. We stepped outside for {number} minutes and instantly started {verb_ing} like {animal_plural}. The sun said “today I will be {adjective2}” and we all just accepted our {adjective3} fate. Someone suggested going to {place}, but the road itself felt like {food} on a pan. Meanwhile {name} showed up with a {thing} thinking it would fix everything 💀. End result: we’re all {adjective4}, drinking {drink}, and questioning our {noun2}."

# output of the midlab story
print("\n" + "-" * 40)
print("         GENERATING YOUR STORY...        ")
print(madlib)
print("\n" + "=" * 40)
