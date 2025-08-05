import random

#dictionaries and lists
#key names of dictionaries
#variables in lists and returning them, and changing variables lists

def buy_turtles(infile):
    infile = open(infile)
    
    new_turtles = []
    
    for line in infile:
        if "#" i line:
            continue
        line.strip('\n')
        line_list.line.split(",")
        new_turtles.append({"name":line_list[0]})
    
    infile.close()
    
    
    return turtles
    

def get_to_know_turtles(turtles):
    '''
    print out the information we have for each turtle:
    name: name, speed: speed, shell density: shell density, etc for what that turtle has
    parameter: list of turtle dictionaries
    return:none
    '''
    for t in turtles:
        for k, v in t.items(): # t.keys() t.values() t.items()
            print(k, ": ", v, end=" ")
        print()
        #print("Name:", t["name"], end = " ")
        #print("Shell denisity:", t.get("shell density", "not recorded"), end = " ")
        #print("hobbies:", t.get("hobbies", "living turtle life"))

def save_turtles(turtle_list):
    """
    turtle_list is a list of turtle dictionaries
    """
    with open("turtles.csv", "w") as outfile:
        outfile.write("# name, speed, shell density, hobbies \n")
        for i in range(len(turtle_list)):
            t = turtle_list[i]
            
          #  for k, v in t.items(): # t.keys() t.values() t.items()
           #     outfile.write( v, ",")
           # outfile.write("/n")
            outfile.write(t["name"] + "," + str(t["speed"]) + "," + str(t.get("shell density", " ")) +  "," + str(t.get("hobbies", " "))+"\n")
            #goal: csv with name, speed, shell density
    
    

turtles = []
# turtle1= {"name": "sue", "speed":5, "shell density": 200}

#generate 5 random turtles
names = ["sue", "terry", "becky", "jerry", "fluffy", "gary"]
ajd = ["slow", "quick","tall", "hairy", "bouncy", "funny", "self aligning"]
#speed between 0 and 100
#shell density between 2 500

for i in range(7):
    new_t = {"name": ajd[random.randint(0,6)] + "  " +names[random.randint(0,5)] }
    new_t["speed"] = random.randint(0,100)
    new_t["shell density"] = random.randint(2,500)
    #print(new_t)
    turtles.append(new_t)
    
shelly = {"name":"shelly", "speed": 34, "hobbies":"knitting"}
turtles.append(shelly)
#print(turtles)
  
#

save_turtles(turtles)


#buy_turtles("turtles.csv")

#get_to_know_turtles(turtles)