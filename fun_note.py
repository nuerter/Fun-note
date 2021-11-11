import random
input("Press Enter")
input("Introduction")
input("*You are currently attending a class in high school.")
input("*Your thoughts: 'Day in and day out... the same thing over and over again.'")
input("'This world ... is rotten' - *you think")
input("You look out the window and you see a small object falling, seemingly out of nowhere.")
input("*class is over. You head out of the building and go looking for the object you saw earlier.")
input("You find it and it's a notebook.")
input("'Death Note... Directly translated, a notebook of death...'")
input("*starts reading 'How to use it... The human whose name is written in this note...shall die?'")
input("*smirks with distrust 'Kudaranai...'")
input("*some time later...")
input("*opens the notebook")
print("\n\n\n\n\n\n\n\n\n")
print("~~~~~~~~~~~~~~~~~~~~DEATH NOTE~~~~~~~~~~~~~~~~~~")
print("\n\n")
input("Play this before you continue https://youtu.be/6LKrpwbAJ8U?t=595")
print("\n")

name = input("WRITE A NAME HERE       ")
name = name.lower().strip()
if name == "ivan":
    exit()
else:
    input("*30seconds later..")
print()
causes = ["heart attack", "stabbed", "ran over by truck", "car crash"]
print(name + "'s" + " cause of death is : " + (random.choice(causes)))
print()

second_name = input("WRITE A NAME HERE       ")
second_name = second_name.lower().strip()
if second_name == "ivan":
    exit()
else:
    input("*30seconds later..")
print()
causes = ["heart attack", "stabbed", "ran over by truck", "car crash"]
print(second_name + "'s" + " cause of death is : " + (random.choice(causes)))
print()

third_name = input("WRITE A NAME HERE       ")
third_name = third_name.lower().strip()
if third_name == "ivan":
    exit()
else:
    input("*30seconds later..")
print()
causes = ["heart attack", "stabbed", "ran over by truck", "car crash"]
print(third_name + "'s" + " cause of death is : " + (random.choice(causes)))
print()
input("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("                  END")
