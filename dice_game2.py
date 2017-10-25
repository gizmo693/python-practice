import random

def start_up():
    print("How many players are playing the game?")
    try:
        return int(input("Enter number of players: "))
    except NameError:
        print("You must enter a valid number of players")
        start_up()

def name_player(d):
    count=0
    player_list=[]
    while count < d:
        name = input("Enter name of player "+str(count+1)+":")
        player_object={'Name':name,'Dice 1':0,'Dice 2':0,'high_scorer':False}
        player_list.append(player_object.copy())
        count=count+1
    return player_list

def dice():
    return random.randint(1,6)
    
def game(players):
    count=0
    d=len(players)
    while count < d:
        player_object = players[count]
        n = player_object['Name']
        raw_input(n + " press Enter to roll the dice:")
        d1 = dice()
        d2 = dice()
        player_object['Dice1']= d1
        player_object['Dice2']= d2
        print('Dice 1 = '+str(d1)+'\tDice 2 = '+str(d2)+'\tTotal:'+str(d1+d2))
        count=count+1

def tie_break(tied_players):
    game(tied_players)
    results(tied_players)

def results(players):
    winning_player=""
    high_score=0
    count=0
    tied_players=[]
    while count < len(players):
        player_object = players[count]
        d1 = player_object['Dice1']
        d2 = player_object['Dice2']
        total = d1 + d2
        if total >= high_score:
            high_score = total
        count=count +1
    
    count=0
    while count < len(players):
        player_object = players[count]
        d1 = player_object['Dice1']
        d2 = player_object['Dice2']
        total = d1 + d2
        if total >= high_score:
            high_score = total
            tied_players.append(player_object.copy())

        count=count+1
    len(tied_players) 
    
    
    if len(tied_players) == 1:
         print ("\n\nWell done "+tied_players[0]['Name'])
    else:
        print "More than one player has the high score. Press enter to start the Tie Break"
        tie_break(tied_players)     
     
def main():
    c = start_up()
    player_list=name_player(c)
    game(player_list)
    results(player_list)
   

main()