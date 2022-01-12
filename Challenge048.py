#----------* CHALLENGE 48 *----------
#Ask for the name of somebody the user wants to invite to a party. After this, display the message “[name] has now been invited” 
# and add 1 to the count. Then ask if they want to invite somebody else. Keep repeating this until they no longer want to invite 
# anyone else to the party and then display how many people they have coming to the party.

count = 0
answer = 'y'
while answer == 'y':
    name = input("Enter the name of someone you want to invite to your party: ")
    print(name+" has now been invited.")
    count = count + 1
    answer = input("Do yow want to invited someone else? ")

print("The total of guests is ",count)