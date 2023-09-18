import random

def throw_dice():
    return random.randint(1,6)

def player_turn(current_score,total_score):
    print("player turn")
    input("Press Enter key.")
    dice = throw_dice()
    print(f"Die scale : {dice}")
    
    if dice ==1:
        print("You lost points because you got 1.")
        return 0
    else:
        current_score+=dice
        print(f"total score(player): {total_score+current_score}")
        return current_score

def computer_turn(current_score,total_score):
    print("player turn")
    input("Press Enter key.")
    dice = throw_dice()
    print(f"Die scale : {dice}")
    
    if dice ==1:
        print("You lost points because you got 1.")
        return 0
    else:
        current_score+=dice
        print(f"total score(computer): {total_score+current_score}")
        return current_score
    
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
        
                     
if __name__ == "__main__":
    pig_dice_game()
