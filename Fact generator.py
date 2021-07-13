#generating a random historical fact with python
import random

#Different facts
a = ("The tank was first used on the fields of Somme" )
b = ("There were four different crusades, one included a friendly christian city")
c = ("The first University built in America was ,Harvard , in Cambridge ")
d = ("Turkeys were once worshipped like gods")
e = ("Napoleon was once attacked by a horde of bunnies")
f = ("The first French revloution lasted ten years, leading to Napoleon gaining power for the next 15 or so years")
g = ("The chicken did cross the road first")

#putting them into a list
vars = [a , b, c, d, e, f, g]

#making a while loop
i = 1
yes = i
g = 3
no = g

#making it generate random
def main():
    print("Hello there")
    input("Say 'Yes' for a fact :")
    print(random.sample(vars,1))
    input("Would you like another? :")
    while yes:
        print(random.sample(vars, 1))
        input("Would you like another?")
        break
    if no:
        print("thanks for playing")
main()

print("Good bye :) ")