import random

accumulate_num=0


def throw_dice():
    return random.randint(1,6)

def player_turn(current_score,total_score):
    print("player turn")
    input("주사위를 굴리려면 Enter 키를 눌러주세요.")
    dice = throw_dice()
    print(f"주사위 눈금 : {dice}")
    
    if dice ==1:
        print("1이 나와서 점수를 잃었습니다.")
    else:
        current_score+=dice
        print(f"총 점수: {total_score+current_score}")
        return current_score

def computer_turn(current_score,total_score):
    print("player turn")
    input("주사위를 굴리려면 Enter 키를 눌러주세요.")
    dice = throw_dice()
    print(f"주사위 눈금 : {dice}")
    
    if dice ==1:
        print("1이 나와서 점수를 잃었습니다.")
    else:
        current_score+=dice
        print(f"총 점수: {total_score+current_score}")
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


