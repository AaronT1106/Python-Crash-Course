guest = ['jesus', 'terence tao', 'jeff bezos']
print(f"{guest[0].title()} I would like to invite you to my dinner")
print(f"{guest[1].title()} I would like to invite you to my dinner")
print(f"{guest[-1].title()} I would like to invite you to my dinner")

print("I found a bigger table to invite more people!")

guest.insert(0, 'tiger woods')
guest.insert(2, 'ronaldo')
guest.append('warren buffet')
print(guest)