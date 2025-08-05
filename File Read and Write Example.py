input_file = open("creatures.csv", "r") #r for read

all_creatures = []

for line in input_file:
    if '#' in line:
        continue
    line = line.strip('\n')
    line_list = line.split(',')
    all_creatures.append({"Wings":line_list[0], "Teeth":line_list[1], "Tails":line_list[2] })

total_wings = 0

for creature in all_creatures:
    total_wings += int(creature["Wings"])
    
print(total_wings)

output_file = open("wings.txt", "w")
output_file.write("total wings = " + str(total_wings) + "\n")
output_file.close()