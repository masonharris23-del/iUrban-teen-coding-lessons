all_horses = []
KEY_NAME =[]
with open('horses.csv', 'r') as infile:

    first_line = True
    for line in infile:
        line = line.strip("\n")
        
        line_list = line.split(",")
        #print(line_list) #todo for debugging
        #line_list = line_list[:-1]
        for l in range(len(line_list)):
            #print(l)\
            
            line_list[l] = line_list[l].strip()
        #print(line_list) #todo for debugging
        
        if first_line: #first line has the key values
           # print(line_list)
            
            for key in line_list:
                KEY_NAME.append(key)
            first_line = False
            KEY_NAME[0] = KEY_NAME[0][1:]
        else:
            this_horse = {}
            for i in range(len(line_list)):
                this_horse[KEY_NAME[i] ] = line_list[i]   
           # print(this_horse)
            all_horses.append(this_horse)
        
    #print(all_horses)
    #print(KEY_NAME)
            
#make weights integers
for h in all_horses:
    h["weight"] = int(h["weight"])
print(all_horses)

#find biggest horse
biggest = ""
weight = 0
for h in all_horses:
    if h["weight"] > weight:
        biggest = h["name"]

print(biggest)
          