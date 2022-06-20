'''
userName = input("Enter your name: ")
# print("Hey" + userName)

userGrade = input("What grade are you in? ")
print("Hey " + userName + ", " + userGrade + " is a lame grade")

userYear = int(input("What year were you born? "))
userAge = 2022 - userYear
print(str(userAge) + " is so young!")
'''

# Create your own Madlibs
# Have at least 5 inputs

noun = input("Please give me a noun: ")
verb = input("Please give me a verb: ")
adjective = input("Please give me a adjective: ")
noun2 = input("Please give me a noun: ")
adverb = input("Please give me a adverb: ")

print(noun + " was walking to a store to " + verb + " a " + adjective + " snack. " + noun2 + " steals his snack and "  + adverb + " ran away." )