import random

accumulate_num=0


def throw_dice():
    return random.randint(1,6)

def player_turn():
    return

def computer_turn():
    return

def pig_dice_game():
    player_score = 0
    computer_score = 0
    
    while player_score<50 and computer_score<50:
        player_score+=player_turn(0,player_score)
        if player_score>=50:
            print("player win")
            break
        computer_score+=computer_turn(0,computer_score)
        if computer_score>=50:
            print("computer win")
            break                


