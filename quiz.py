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



print(f"Percent Grade: {int(correct_answers/15)*100:<1f}%")