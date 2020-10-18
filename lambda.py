people = [                                  # this is a list
    {"name": "ash", "pokemon": "pikachu"},  # these are
    {"name": "rocko", "pokemon": "onyx"},   # dictionaries inside
    {"name": "oak", "pokemon": "tauros"}    # this list
]

# def f(person):                              # sort people by name (alphabetical order)
    # return person["name"]

# people.sort(key=f)

people.sort(key=lambda person: person["name"])

print(people)
