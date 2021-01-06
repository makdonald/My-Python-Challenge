import random
import time

player_cards = []
croupier_cards = []
blackjack = 21
player_credit = 100_000
end_game = False
busts = False
busts_cr = False
end_croupier =False
end_player = False
#win = False
#lost = False
#draw = False
time.sleep(2)
player_name = input("\n\tHello my friend, what is your name?\n\n\t")

cards = [1,2,3,4,5,6,7,8,9,10,10,10,10,11,
        1,2,3,4,5,6,7,8,9,10,10,10,10,11,
        1,2,3,4,5,6,7,8,9,10,10,10,10,11,
        1,2,3,4,5,6,7,8,9,10,10,10,10,11,
]
time.sleep(2)
print(f"\n\tHello {player_name} and WELCOME TO.....\n")
time.sleep(1)
print(''' ||||     |||      |||  ||  ||   ||    |||||          |||||   ||     |||    |||||   || |||          ||   |||    ||||   || |||''')
time.sleep(1)
print('''||       |   |    ||    ||  |||  ||   ||   ||         ||__||  ||    |   |   ||      |||             ||  |   |  ||      ||| ''')
time.sleep(1)
print('''||       |||||     ||   ||  || | ||   ||   ||         ||  ||  ||    |||||   ||      |||             ||  |||||  ||      |||  ''')
time.sleep(1)
print(''' ||||    |   |   |||    ||  ||  |||    |||||          |||||   ||||| |   |   |||||   || |||        |||   |   |   ||||   || |||
         ''')
time.sleep(2)

# Help will be activated on press
help_me = input("\n\tIf you want see the rules press 'h' if not press anything else :")
if help_me == "h":
    print('''
    *************************************************************************************************************************************************
    
    It's simplfy version of "Blackjack". You will play against croupier. Player needs to get 21 points or be close to 21 points but not to exceed it.
    At the beginning player and croupier receive two cards (Cropier shows only one card).
    Next player make a decision if want another card (hit) or not (stand)
    When the player don't exceed 21 points and decided to stand, croupier start playing. Croupier shows a second card which was hidden
    and next takes a card one by one until he will have more than 16 points. If he has more than 16 he finishes the game and count the points.
    The winner is a player who has 21 points or who is the closest to 21. Enjoy!!!

    **************************************************************************************************************************************************
    ''')
    input("\n\tPress 'Enter' to continue....\n\t")
else:
    pass

while player_credit > 0 and end_game == False:
    time.sleep(2)
    game_credit = float(input(f"\n\tYou have ${player_credit:,} so how much do you want bet? :"))
    time.sleep(2)
    print(f"\n\tYou bet ${game_credit:,} so let's play\n")
    
    # first round: croupier and player takes 2 cards
    croupier_cards.append(cards.pop(random.choice(cards)))
    croupier_cards.append(cards.pop(random.choice(cards)))
    player_cards.append(cards.pop(random.choice(cards)))
    player_cards.append(cards.pop(random.choice(cards)))

    time.sleep(2)
    print("\n\tCroupier's first card has a value equal to {} points \n\tand you have {} points, missing to blackjack {}\n"
    .format(croupier_cards[0],sum(player_cards),blackjack-sum(player_cards)) )

    # if you have a black jack at the start or you busts
    if sum(player_cards) == blackjack:
        time.sleep(2)
        print("\n\tYou have a blackjack so don't take another card and wait for croupier\n")
        end_player = True
    elif sum(player_cards) > blackjack:
        time.sleep(2)
        print("\n\tYou have busts!!!\n")
        busts = True
        #end_player = True
        #break
    else:
        pass

    # rounds for player
    #print(end_player) # bug: sometimes end_player is TRUE and skip if statement
    if end_player == False:# and busts == False:
        time.sleep(2)
        hit_or_stand = input("\n\tPress 'h' if you want hit or 's' if you want stand: ")
    
        time.sleep(2)
        while hit_or_stand.lower() == "h":
            player_cards.append(cards.pop(random.choice(cards)))
            time.sleep(2)
            print(f"\n\tYou take card and you have {sum(player_cards)}\n")
            if sum(player_cards) == blackjack:
                time.sleep(2)
                print("\n\tYou have a blackjack so don't take another card and wait for croupier\n")
                end_player = True
                break
            elif sum(player_cards) > blackjack:
                time.sleep(2)
                print("\n\tYou have busts!!!\n")
                busts = True
                break
            else:
                time.sleep(2)
                hit_or_stand = input("\n\tPress 'h' if you want hit or 's' if you want stand: ")
    else:
        pass
    # rounds for croupier
    #print(busts) # bug: sometimes busts ==TRUE and skip while loop
    while sum(croupier_cards) < 17 and busts != True: 
        croupier_cards.append(cards.pop(random.choice(cards)))
        end_croupier = True
        time.sleep(2)
        print(f"\n\tCroupier take card with {croupier_cards[-1]} points and has {sum(croupier_cards)}")
        if sum(croupier_cards) == blackjack:
            time.sleep(2)
            print("\n\tCroupier has a blackjack!!!")
            end_croupier = True
            break
        elif sum(croupier_cards) > blackjack:
            time.sleep(2)
            print("\n\tCroupier busts")
            busts_cr = True
            break
        #else:
            #end_croupier = True
    print(f"\n\tYou have {sum(player_cards)} points and Croupier has {sum(croupier_cards)} points")
        # scores
    if sum(player_cards) <= 21 and sum(croupier_cards) <= 21: #end_player == True: #and end_croupier == True:
        if sum(player_cards) > sum(croupier_cards):
            time.sleep(2)
            print(f"\n\tYou have won {player_name} - {sum(player_cards)} \n\tCroupier - {sum(croupier_cards)}")
            player_credit += game_credit
        elif sum(player_cards) == sum(croupier_cards):
            time.sleep(2)
            print("\n\tIt's a draw, no one loose!!!")
        elif sum(player_cards) < sum(croupier_cards):
            time.sleep(2)
            print("\n\tYou have lost")
            player_credit -= game_credit
    elif sum(player_cards) <= blackjack and sum(croupier_cards) > blackjack:
        time.sleep(2)
        print("\n\tYou won")
        player_credit += game_credit
    elif sum(player_cards) > blackjack and sum(croupier_cards) <= blackjack:
        time.sleep(2)
        print("\n\tCroupier won")
        player_credit -= game_credit
    next_game = input("\n\tDo you want play again (y/n)?: ")
    if next_game == "y":
        print("\n\tGreat. Order another pint and back to the table")
        player_cards.clear()
        croupier_cards.clear()
    else:
        time.sleep(2)
        print(f"\n\tThank you for game. You have won ${player_credit}. CONGRATULATION!!!\n")
        end_game = True
        break
    
#  you have no money
if player_credit == 0:
    time.sleep(2)
    print("\n\tOops!!!! You have no money! Also you are drunk. Go home and take some sleep. Tommorow is Python with Thomas\n\t")



    