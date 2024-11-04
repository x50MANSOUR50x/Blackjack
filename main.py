from random import choice
from os import system
from time import sleep

#        Ace                             King Queen Jack
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10,  10,   10]

system('cls')
game_on = input("Do you want to play a game of Blackjack? Type 'y' or 'n':\n").lower()

while(game_on == 'y'):
        system('cls')
        
        computer_cards = [choice(cards), choice(cards)]
        player_cards = [choice(cards), choice(cards)]

        print(".------.            _     _            _    _            _")
        print("|A_  _ |.          | |   | |          | |  (_)          | |")
        print("|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __")
        print("| \  /|K /\  |     | '_ \| |/ _' |/ __| |/ / |/ _' |/ __| |/ /")
        print("|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   <")
        print("\'-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\")
        print("      |  \/ K|                            _/ |")
        print("      '------'                           |__/")

        print(f"Your cards: { player_cards }, current score: { sum(player_cards) }")
        print(f"Computer's first card: { computer_cards[0] }")

        while(input("Type 'y' to get another card, type 'n' to pass:\n") == 'y'):
            player_cards.append(choice(cards))
            computer_cards.append(choice(cards))

            print(f"Your cards: { player_cards }, current score: { sum(player_cards) }")
            print(f"Computer's first card: { computer_cards[0] }")

            if(sum(computer_cards) >= 21):
                  if((sum(computer_cards) - 10) >= 21 and 11 in computer_cards):
                       break
                  elif(11 not in computer_cards):
                       break
            if(sum(player_cards) >= 21 ):
                  if((sum(player_cards) - 10) >= 21 and 11 in player_cards):
                       break  
                  elif(11 not in player_cards):
                       break        

        if(sum(player_cards) > 21):
            if(11 in player_cards):
                player_cards[player_cards.index(11)] = 1
        if(sum(computer_cards) > 21):
            if(11 in computer_cards):
                computer_cards[computer_cards.index(11)] = 1
        
        print(f"Your final hand: { player_cards }, final score: { sum(player_cards) }")
        print(f"Computer's final hand: { computer_cards }, final score: { sum(computer_cards) }\n")
   

        if(sum(player_cards) == sum(computer_cards)):
             print("You Draw")
        elif(sum(player_cards) == 21):
             print("You won!")
        elif(sum(computer_cards) == 21):
             print("You Lost!")
        elif(sum(player_cards) > 21):
             print("You went over. You Lost!")
        elif(sum(computer_cards) > 21):
             print("The computer went over. You Won!")
        elif(sum(player_cards) > sum(computer_cards)):
             print("You won!")
        elif(sum(computer_cards) > sum(player_cards)):
             print("You Lose!")

        if(input("\nDo you want to play a game of Blackjack? Type 'y' or 'n':\n").lower() == 'n'):
             game_on = False
             
system('cls')
print("Thank you for playing Blackjack !!!")
sleep(3)
system('cls')
             
            
                  
    




















# print('''
# .------.            _     _            _    _            _
# |A_  _ |.          | |   | |          | |  (_)          | |
# |( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
# | \  /|K /\  |     | '_ \| |/ _' |/ __| |/ / |/ _' |/ __| |/ /
# |  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   <
# '-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
#       |  \/ K|                            _/ |
#       '------'                           |__/
#
# ''')
