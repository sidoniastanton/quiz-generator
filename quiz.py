'''
Sidonia Stanton
September 25
Quiz Generator
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


user_response = input("Francis Bacon's lover, George Dyer, was found dead two days before\n\
the biggest art showing of Bacon's life. Dyer had died in the same position\n\
Bacon had once painted him:____\n: ")
if (user_response == "on the toilet"):
    print("Correct!")
    correct_answers = correct_answers +1
else:
    print("Incorrect")


user_response = input("Andy Warhol once said in his diaries that having his _____ ripped\n\
off was worse than being shot.\n:")
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


user_response = input("Water-soluble ink (composed of black soot and a\n\
binding agent usually made from fish bones) was invented in\n\
which country in 2500 BC?\n: ")
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


user_response = input("A popular pigment during the Pre-Raphaelite era was Mummy Brown,\nfamous for never drying and being made from ground-up:____\n:")
if (user_response == "mummies" or "egyptian mummies"):
    print("Correct!")
    correct_answers = correct_answers +1
else:
    print("Incorrect")


user_response = input("Which Botticelli painting is known for including 500 identifiable plant species? \n: ")
if (user_response == "birth of venus" or "the birth of venus"):
    print("Correct!")
    correct_answers = correct_answers +1
else:
    print("Incorrect")


user_response = input("This artist is considered the first female painter who was permitted to depict female nudity\n: ")
if (user_response == "lavinia fontana"):
    print("Correct!")
    correct_answers = correct_answers +1
else:
    print("Incorrect")             


user_response = input("It's theorized that Artemisia Gentileschi studied ____'s \n\
notes on anatomy to ensure the spurts of blood were accurate in her\n\
depiction of Judith Beheading Holophernes\n: ")
if (user_response == "galileo" or "galileo galilei"):
    print("Correct!")
    correct_answers = correct_answers +1
else:
    print("Incorrect")   


user_response = input("What creature is Sepia ink harvested from?\n: ")
if (user_response == "cuttlefish"):
    print("Correct!")
    correct_answers = correct_answers +1
else:
    print("Incorrect")


user_response = input("The Black Paintings is a series of 14 dark and disturbing paintings by Francisco Goya.\n\
What were they painted on?\nA: Wooden floorboards\nB: Lamb hide\nC: Human skin\nD: His dining room walls\n: ")
if (user_response == "d"):
    print("Correct!")
    correct_answers = correct_answers +1
else:
    print("Incorrect")


user_response = input("Ruthie Tompson, born in Portland, Maine, went on to become a Disney Legend\n\
for her work on such films as \"Snow White and the Seven Dwarves\" and \"Mary Poppins\".\n\
 How old was she when she died in 2021?\nA: 101\nB: 105\nC: 111\nD: 114\n: ")
if (user_response == "c"):
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