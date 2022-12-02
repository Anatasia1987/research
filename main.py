# import turtle
import turtle
from logics import *
import composition 
import random

# this just removes the animation delay
turtle.delay(0)

def main():
    # how do we get it to just do one function from the compositions file?
    # we'd need to list the compositions
    #    set up a blank list
    comps = []
    
    # then, FOR each function in the compositions module
    for func in dir():
        # if the function name starts with "composition"
        if func.startswith("composition"):
            # add it to the list
            comps.append(func)
    
    # now, we can pick a random composition from the list
    #    and run it
    #    we'll use the random module
    #    and the random.choice() function
    #    to pick a random item from the list

    # pick a random composition
    comp = random.choice(comps)
    # run it
    
    

    # pause the screen for 2 second
    turtle.exitonclick()
    main()


# this little snippet of code makes sure that the main() function is called directly (this is useful for testing later)
if __name__ == "__main__":
        main()
    


# exit the program when the user clicks on the screen
