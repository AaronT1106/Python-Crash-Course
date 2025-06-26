guest = ['jesus', 'terence tao', 'jeff bezos']
print(f"{guest[0].title()} I would like to invite you to my dinner")
print(f"{guest[1].title()} I would like to invite you to my dinner")
print(f"{guest[-1].title()} I would like to invite you to my dinner")
#adding a print statement to show who can't make it
print(f"{guest[0]} can't make the dinner.")
guest[0] = 'david goggins'


print(f"{guest[0].title()} I would like to invite you to my dinner")
print(f"{guest[1].title()} I would like to invite you to my dinner")
print(f"{guest[-1].title()} I would like to invite you to my dinner")