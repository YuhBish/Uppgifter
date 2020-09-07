import random
min = 1
max = 100
roll_again = "yes"

while roll_again == "yes" or print("too bad"):
  print("Rolling")
  print (random.randint(min, max))

  roll_again = input("Again?")

