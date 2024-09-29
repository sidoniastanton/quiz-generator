'''
Sidonia Stanton
September 25
Quiz Generator
'''

'''
**DELETE BEFORE SUBMITTING**
topic: art history
'''

correct_answers = 0

print("Welcome to Sid's Art History Quiz!")

user_response = input("What kind of paint was Vincent Van Gogh known to use? \nA: Acrylic\nB: Tempura\nC: Oil\nD:Watercolor\n:")
user_response = user_response.lower().strip()

if (user_response == "c"):
    print("Correct!")
    correct_answers = correct_answers +1
else:
    print("Incorrect")



user_response = input("Which of these crimes did Baroque painter Caravaggio not commit? \nA: Threatening the Pope\nB. Carrying a sword without a permit\nC: Beating a man with a stick\nD: Writing satirical poems about another artist\n:")
user_response = user_response.lower().strip()

if (user_response == "a"):
    print("Correct!")
    correct_answers = correct_answers +1
else:
    print("Incorrect")



user_response = input("Michelangelo preferred ____ over painting.\n:")
user_response = user_response.lower().strip()

if (user_response == "sculpting"):
    print("Correct!")
    correct_answers = correct_answers +1
else:
    print("Incorrect")


user_response = input("Francis Bacon's lover, George Dyer, was found dead two days before the biggest art showing of Bacon's life. Dyer had died\n\
in the same position Bacon had once painted him: ")
if (user_response == "on the toilet"):
    print("Correct!")
    correct_answers = correct_answers +1
else:
    print("Incorrect")


percent_correct = (correct_answers/15)*100
print(f"Your score: {int(correct_answers)} / 15")
print(f"Percent Grade: {int(percent_correct):<1.0f}%")

if (percent_correct<=59): 
   grade = "F"
elif (60 <= percent_correct <= 69):
    grade = "D"
elif (70<=percent_correct<=79):
    grade = "C"
elif (80<=percent_correct<=89):
    grade = "B"
elif (90<=percent_correct<=100):
    grade = "A"

print(f"Letter Grade: {grade}")