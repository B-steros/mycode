"""Driving a simple game framework with a dictionary object | Alta3 Research"""

def showInstructions():
    """Show the game instructions when called"""
    #print a main menu and the commands
    print('''
    RPG Game
    ========
    Commands:
     go [direction]
     get [item]
    ''')

def showStatus():
    """determine the current status of the player"""
    #print player's current location
    print('---------------------------')
    print('You are in the ' + currentRoom)
    print('To win - Get to the Garden with a key and a potion. Also... AVOID THE MONSTER!')
    #print what the player is carrying
    print('Inventory:', inventory)
    #check if there's an item in the room, if so print it
    if "item" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'])
    print("---------------------------")


#an inventory, which is inititally empty
inventory = []

#a dictionary linking a room to other rooms
rooms = {

            'Hall' : {
                  'south' : 'Kitchen',
                  'east'  : 'Dining Room',
                  'item'  : 'key'
                },

            'Kitchen' : {
                  'north' : 'Hall',
                  'item'  : 'monster',
                },
            'Dining Room' : {
                  'east' : 'Man Cave',
                  'west' : 'Hall',
                  'south' : 'Garden',
                  'item' : 'potion'
             },
            'Man Cave' : {
                'west' : 'Dining Room'
            },
            'Garden' : {
                'north' : 'Dining Room'
            }
          }

currentRoom = 'Hall'

showInstructions()

while True:
    showStatus()

    #the player MUST type something in
    #otherwise input will keep asking
    move = ''
    while move == '':
        move = input('>')


    #normalizing input:
    #.lower() makes it lower case, .split() turns it to a list
    # therefore, "get golden key" becomes ["get", "golden key"]

    move = move.lower().split(" ", 1)

    #if they type 'go' first
    if move[0] == 'go':
        #check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            currentRoom = rooms[currentRoom][move[1]]


        else:
            print('You can\'t go that way!')

    if move[0] == 'get':

        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:

            inventory.append(move[1])
            
            print(move[1] + ' got!')

            del rooms[currentRoom]['item']

        else:
            print('Can\'t get ' + move[1] + '!')

    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        print('A monster has got you... GAME OVER!')
        break
    
    if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
        break
