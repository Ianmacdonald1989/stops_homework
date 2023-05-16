users = {
  "Jonathan": {
    "twitter": "jonnyt",
    "lottery_numbers": [6, 12, 49, 33, 45, 20],
    "home_town": "Stirling",
    "pets": [
    {
      "name": "fluffy",
      "species": "cat"
    },
    {
      "name": "fido",
      "species": "dog"
    },
    {
      "name": "spike",
      "species": "dog"
    }
  ]
  },
  "Erik": {
    "twitter": "eriksf",
    "lottery_numbers": [18, 34, 8, 11, 24],
    "home_town": "Linlithgow",
    "pets": [
    {
      "name": "nemo",
      "species": "fish"
    },
    {
      "name": "kevin",
      "species": "fish"
    },
    {
      "name": "spike",
      "species": "dog"
    },
    {
      "name": "rupert",
      "species": "parrot"
    },
    {
      "name": "Fluffy",
      "species": "dog"
    }
  ]
  },
  "Avril": {
    "twitter": "bridgpally",
    "lottery_numbers": [12, 14, 33, 38, 9, 25],
    "home_town": "Dunbar",
    "pets": [
      {
        "name": "monty",
        "species": "snake"
      }
    ]
  }
}

# 1. Get Jonathan's Twitter handle (i.e. the string `"jonnyt"`)
print(users["Jonathan"]["twitter"])

Eriks_home_town = users["Erik"]["home_town"]
print(Eriks_home_town)

# 1. Get Jonathan's Twitter handle (i.e. the string `"jonny
# 2. Get Erik's hometown
# 3. Get the list of Erik's lottery numbers

print(users["Erik"]["lottery_numbers"])
# 4. Get the species of Avril's pet Monty
print(users["Avril"]["pets"][0]["species"])
# 5. Get the smallest of Erik's lottery numbers
Eriks_lowest_number = users["Erik"]["lottery_numbers"]
Eriks_lowest_number.sort()
print(Eriks_lowest_number[0])

# 6. Return an list of Avril's lottery numbers that are even
avrils_numbers = users["Avril"]["lottery_numbers"]
# for x in avrils_numbers:
#   if x % 2 == 0:
#     print(avrils_numbers, end="")
# if avrils_numbers[0] % 2 == 0:

even_nos = [num for num in avrils_numbers if num % 2 == 0]
print(even_nos)

# def avrils_even_numbers = users(["Avril"]["lottery_numbers"]):
#    for num in nums_list:
#          if num % 2 == 0:
#             print(num, end=' ')
    



# 7. Erik is one lottery number short! Add the number `7` to be included in his lottery numbers
# users.append ["lottery_numbers"][78]
# print(lottery_numbers)

# 8. Change Erik's hometown to Edinburgh

# 9. Add a pet dog to Erik called "fluffy"

# 10. Add another person to the users dictionary
users = {
  "pete": {
    "twitter": "petet",
    "lottery_numbers": [20, 8, 18, 10, 14],
    "home_town": "Glasgow",
    "pets": 
    {
      "name": "Rosie",
      "species": "Cat"
    },
}
}
print(users["pete"]["twitter"])
