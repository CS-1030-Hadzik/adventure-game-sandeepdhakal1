# Welcome message and introduction
print("Welcome to the Adventure Game!")  
print("Your journey begins here...")
#Asj for thr player's name
player_name= input("What is your name, adventurer?")
#Concatenate striungs to create a personalized message
print("Welcome, "+ player_name + '! your journey begains now.')
#Use an f-struing to display the same messagein a more readable way 
print(f'Welcome, {player_name}! your journey begains now.')
#Desciber the starting area 
starting_area="""
You find yourself in a dark forest. 
The sould of rustling leaves fulls the air.
A faint path lies ahead , leading deeper into the unknown...

"""
print(starting_area)

#Ask the player for their first decision
decision = input("Do you wish to make the path?(yes or no):").lower()
#Respond based on the player's decision 
if decision=='yes':
    print(f'Brave choice,{player_name}! you step onto the path and venture forward.')
elif decision =='no':
    print(player_name+',you decide to wait.pherhaps courage will find you later.')
    #Concatenation example
else:
    print('Confused, you stand still, unsure of what to do.')
    