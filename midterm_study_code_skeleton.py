#### Midterm 141
#Name:
#Instructions: start in the main guard on line 99, and fill in the functions as needed.
# If you start with A1 and B1 and work your way down, you'll be going from easiest to hardest
#  (but you can skip around as needed)
# you'll find under each function (TODOs B through F) some pseudocode to help you
# Each function (TODOs B through F) is worth 15 points
# Each of the 12 A TODOs are worth 2 points
# Everyone gets 1 free point for putting their name on their file :-)


#TODO B1
#write the function that matches this doc string
'''
list_as_string takes a list and makes a string from the values
#and their labels
parameters: a list of 3 items: food, water, and happy
return: a string formatted like this: "food: 1 water: 1 happy: 1"
#where the numbers match the values in the list
'''


#TODO C1
'''
day_passes represents a day passing in the turtle's life and it getting
#hungrier, thirstier, and sadder
parameters: the turtle's state list
return: none
'''

    
    #TODO C2
    #for each of the turtle's states, reduce the value by a random number
    #between 2 and 5
    
 
    
    #TODO C3
    #print "turtle is now...food: 2 water: 4 happy: 3" (but with the currently correct numbers) (hint: use list_as_string!) 
  
    
#TODO D1
'''
turtle_care represents taking care of the turtle by giving it food or water. 
parameters:
    the index integer of what you're updating (0 for food and 1 for water),
    the turtle's state list
    the supply list
return: how many food or water were given in total
'''

    #TODO D2
    #until the turtle's food/water(whatever is at the passed in index) reaches 10 AND
    #you still have some food/water in your supplies
    #increase the turtle's food/water by 1 and reduce the supply food/water by 1

        
        
    #TODO D3
    #return the total number of food or water which was given to the turtle
    

#TODO E1
'''
walk_turtle takes a turtle on a walk.
    The turtle likes walking down stairs! Turtle will draw a staircase going down and to the right.
    
parameters: a turtle object facing right
return: none
''' 

    #TODO E2
    #have the turtle walk down one stair of side and height 21
    
    #TODO E3
    #Have it walk down a random number of stairs (between 2 stairs and 10 stairs)
    
  
    #TODO E4
    #for extra credit, use a nested loop to do the above


#TODO F1
'''
forage represents foraging for supplies and finding a random amount

parameters: a supply list
return: none
'''

   
   #TODO F2 print "foraging..."
    
   
   #TODO F3 
   #choose a random index position in the supply list and add a random value
    #between 4 and 10 (inclusive)
    
'''
main is called by the main guard and runs a loop asking the user what task they want to do and then doing that.
After each task, the loop runs again, allowing the user to pick another task to execute.
Some user tasks will require function calls, which should happen inside the main loop, and then the loop will continue. 

parameters: a supply list and a turtle state list
return: none
'''

def main():
       
    #TODO A5
    #Put this input statement inside a while loop that'll run
    #until the user types 'q'
    # input("type 't' to talk to the turtle, 's' to check supply levels, 'n' for next day, 'c' to care for the turtle, 'w' to walk the turtle, 'f' to forage for supplies, and 'q' to quit ") #provided, don't change
        
        
        #TODO A6
        #if user types t, then send the turtle's state list to list_as_string() (TODO B1) and print the return
       
        #TODO A7
        #if user types s, then send the turtle's supply list to list_as_string() (TODO B1) and print the return
        
        
        #TODO A8
        #if the user types n, then call day_passes() (TODO C1) and pass in the turtle state list
       
        #TODO A9
       
        #if the user types c, then first give the turtle food and then water.
            #use turtle_care (TODO D1) to give the food and water
            #and print out : "fed : 3 times" where the number is how many times you fed it (return value from turtle_care)
            #and print out : "watered : 3 times" where the number is how many times you watered it (return value from turtle_care)
  
        
        #TODO A10
        #if the user types w, then the turtle takes a walk and becomes happy
       
            #TODO A10.1
            #create a turtle
          
            #TODO A10.2
            #send the turtle on a walk using walk_turtle() (TODO E1)
       
         
            #TODO A10.3
            #add 5 to the turtle's happy value (index position 2 on the turtle state list)
           
      
            #TODO A10.4
            # comment out the line below to run turtle.exitonclick() so the window closes when you click
    
        
        #TODO A11
        #if the user types f, then go foraging
        
    
            #TODO A11.1
            #go foraging using forage() (TODO F1)
       
    
            #TODO A11.2
            #then have a day pass using day_passes()
            
            
            #TODO A11.3       
            #then print out the new supply list using list_as_string()
      
            
        #TODO A12
        #if the user types q then print goodbye
        
        
         
        #TODO A13
        #if the user prints anything else, print "I didn't understand. Please try again" . Please print this exactly (copy & paste the string).
      
    pass

"""
Summary: we use the main guard to separate the functions from the running of the functions.
This makes importing & testing easier!

"""
if __name__ == "__main__":
    
    #TODO A1 we'll be using turtles and random. Use the right import statements here in the main guard.
    
    #TODO A2
    #make a list to store the turtle's state, which will have 3 values
    #to store how much food, water, and happy the turtle has.
    #start the turtle with 5 of each
   
    
    #TODO A3
    #make a list to store your suppplies, which will have 3 values to
    #store how much food, water, and happy brand treats you have.
    #start the list with 4 of each.
    
    
    #TODO A4 Call the main function and pass in the turtle state list
    #and the supplies list
   
    
    pass
    
