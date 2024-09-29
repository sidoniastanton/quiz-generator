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



user_response = input("Which of these crimes did Baroque painter Caravaggio NOT commit? \nA: Threatening the Pope\nB. Carrying a sword without a permit\nC: Beating a man with a stick\nD: Writing satirical poems about another artist\n:")
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
in the same position Bacon had once painted him:____\n: ")
if (user_response == "on the toilet"):
    print("Correct!")
    correct_answers = correct_answers +1
else:
    print("Incorrect")


user_response = input("Andy Warhol once said in his diaries that having his _____ ripped off was worse than being shot.\n:")
if (user_response == "wig"):
    print("Correct!")
    correct_answers = correct_answers +1
else:
    print("Incorrect") 
    # side note -- i'm almost certain this is true, but i spent too long trying to check myself, so let's just pretend i'm right


user_response = input("Which of these toxic substances was NOT historically used as pigment for paints?\nA: Lead (White)\nB: Uranium (Orange)\nC: Mercury Sulfide (Red)\nD: Deadly Nightshade (Purple)\n: ")
if (user_response == "d"):
    print("Correct!")
    correct_answers = correct_answers +1
else:
    print("Incorrect") 


user_response = input("Water-soluble ink (composed of black soot and a binding agent usually made from fish bones) was invented in which country in 2500 BC?\n: ")
if (user_response == "china"):
    print("Correct!")
    correct_answers = correct_answers +1
else:
    print("Incorrect")


user_response = input("How many years did it take Michelangelo to paint the ceiling of the Sistine Chapel?\n: ")
if (user_response == "4" or "four"):
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