
"""
clean_usernames removes the 3 leading and trailing # on usernames
parameters: list of usernames (strings)
returns: list of usernames(strings) without #
preconditions / postconditions: none

"""

def clean_usernames(names):
    clean = names               #make a copy of the list
    for n in range(len(names)): #run once for each word in the list
        fix_name = ""            #make an empty string
        for i in range(3,len(names[n])-3):#for every letter in the name (except first 3 and last 3)
            fix_name += names[n][i] #add that letter to my new string
        clean[n] = fix_name     #add that string to the clean list
    
    return(clean)

usernames = ["###Glegodile###", "###Jimmy###", "###Flapjack###", "###Winston###"]  #todo get user input
#print(clean_usernames(usernames))