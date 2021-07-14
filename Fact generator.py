#generating a random historical fact with python
import random

#Different facts

# Jasper: It will be much easier and efficient to store these facts
# in a list rather than having them take up their own variable

a = ("The tank was first used on the fields of Somme" )
b = ("There were four different crusades, one included a friendly christian city")
c = ("The first University built in America was ,Harvard , in Cambridge ")
d = ("Turkeys were once worshipped like gods")
e = ("Napoleon was once attacked by a horde of bunnies")
f = ("The first French revloution lasted ten years, leading to Napoleon gaining power for the next 15 or so years")
g = ("The chicken did cross the road first")

#putting them into a list
vars = [a , b, c, d, e, f, g]

# Jasper: Just put the facts in the list you do not need this middle man

#making a while loop
i = 1
yes = i
g = 3
no = g

# Jasper: These variables could also use some refactoring 
# 
# Declaring the variable i as 1 then yes as i could be 
# simplified to yes = 1 and 3 to no 


#making it generate random
def main():
    print("Hello there")
    input("Say 'Yes' for a fact :")

    # Jasper: No matter what the user inputs the program will always
    # return a fact.

    print(random.sample(vars,1))
    input("Would you like another? :")
    
    # Jasper; The users answer does not matter here either since
    # the input is never checked.

    # Jasper: While loops usually have a variable that they depend on
    # in order to stop the program. For example, if I wanted to print
    # Hello 5 times this is how I would do it with a while loop:
    #
    # i = 0 # Set a variables initial value
    # while i < 5: # While this statement is true
    #   print("Hello") # Print Hello
    #   i = i + 1 # Then increment the variable so the loop does not go on forever
    #
    # The way that you are using a while loop indicates that you want to keep
    # printing facts until the user states that they do not want anymore
    # so you'll need to implement some way in order to check the input
    # of the user.

    
    # Jasper: This will produce an infinite loop since there is no case where
    # the while loop will end. The only reason that it ends is because the break
    # on line 69 is there
    while yes: 
        print(random.sample(vars, 1))
        input("Would you like another?")
        break
    # Jasper: This If statement does nothing since there is no condition where it can
    # evaluate to true or false. If we look at the statement the same way we 
    # look at a statement verbally this if statement is similar to me saying
    # "If I go" there's not enough context in order to evaluate whether that
    # statement is true or false. You have half the condition you just need
    # the other half

    # Jasper: Booleans in Python or any other language instead of using True or False
    # can also use 0 or 1. 0 being false and 1 being true, any int value that is not
    # 0 is evaluated to true and this is whats happening here. That's your little comp
    # sci lesson for today. Goes back to binary if you really want to delve deep into
    # why computers do this.
    if no:
        print("thanks for playing") 
main()

print("Good bye :) ")
