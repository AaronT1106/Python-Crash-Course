guest = ['jesus', 'terence tao', 'jeff bezos']
print(f"{guest[0].title()} I would like to invite you to my dinner")
print(f"{guest[1].title()} I would like to invite you to my dinner")
print(f"{guest[-1].title()} I would like to invite you to my dinner")

guest.insert(0, 'tiger woods')
guest.insert(2, 'ronaldo')
guest.append('warren buffet')
print("I am sorry but i can only invite 2 people for dinner")
guest1= guest.pop()
print(f"I am sorry {guest1} but i can't invite you to dinner ")
guest2= guest.pop()
print(f"I am sorry {guest2} but i can't invite you to dinner ")
guest3=guest.pop()
print(f"I am sorry {guest3} but i can't invite you to dinner ")
guest4=guest.pop()
print(f"I am sorry {guest4} but i can't invite you to dinner ")
print(f"{guest[0]} and {guest[1]} you're still invited ")
del guest[0]
del guest[0]
print(guest)



