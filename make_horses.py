import random
with open('horses.csv', 'a') as outfile:
    ##name, color, weight, hoof size, hands, price
    name2 = ["Sugar","Horsey", "NoName", "Spirit", "Dusty", "Sunshine", "Dash", "Magic", "Jasper", "Rebel", "Scout", "Star", "Willow", "Lucky", "Chance"]
    name1 = ["Baby", "Pretty", "Lovely", "Considerate", "Constant", "Content", "Wild", "Cool", "Cooperative", "Swift", "Corny", "McHorseFace"]

    for i in range(50):
        this_horse = random.choice(name1) + " " + random.choice(name2)+ ","
        
        this_horse += random.choice(["gray", "black", "bay", "chestnut", "dun", "sorrel", "pinto", "Champagne", "Perlino", "Cremello", "Chocolate Palomino", "Liver Chestnut", "Silver Dapple Grey"]) + ","

        this_horse += str(random.randint(50, 3000)) + ","
        this_horse += str(random.randint(1, 10)) + ","
        this_horse += str(random.randint(5, 21)) + ","
        this_horse += "$" +str(random.randint(5, 5000))+ "\n"
                        
    #print(this_horse)
        outfile.write(this_horse)



          