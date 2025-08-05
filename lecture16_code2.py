
drinks = ["2% milk", "Diet coke, large", "strawberry milkshake"]
food = ["burger", "veggie burger"]
condiments = ["Ranch dressing", "ketchup", "wasabi"]

bag = [drinks, food, condiments]

#          0                   1                       2  
# 0 [ "2% milk", 		"Diet coke, large", "strawberry milkshake"]
# 1 ["burger", 			"veggie burger"]
# 2 ["Ranch dressing", 	"ketchup", 			"wasabi"]

'''
looks for the food(string) in the bag(list of lists) and returns the location
parameters : food(string), bag(list of lists)
return coordinates which list and at which index
'''
def find_my_food(bag, food):
    
    #do a 'for' loop over each list
    # and a 'for' loop within each list, looking for a match
    
    loc1 = 0 #todo temp value : replace once 'for' loops are done
    loc2 = 2 #todo temp value : replace once 'for' loops are done
    
    location = (loc1, loc2) # loc 1, loc2 bundled together
    print(type(location))
    
    return location

found = find_my_food(bag, "strawberry milkshake")

f1, f2 = found #unpack the tuple

print(bag[f1][f2])

