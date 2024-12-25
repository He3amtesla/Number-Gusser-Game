from src.utils.validate_input import validate_input
from game_logic.random_num import randint
from game_logic.hint_generator import give_user_hint
from game_logic.scorer import score
from game_logic.qusstion_user import qussiton_g

def main():
    score_user = score()
    randnum = randint(0, 100)
    
    while True:   
        input_user = input("Guess from 1 to 100 numbers: ")
        if input_user == 'q':
            break
        
        if not validate_input(input_user) :
            continue
        
        input_user = int(input_user)
        
        if give_user_hint(randnum, input_user):
            score_user.decrement_score(1)
            continue
    
        print ("Well done, you guessed right, Your score: ", score_user.get_score())
        anwser_user = input("Do you want to play again? (yes --type-> y ,no --type->  n): ")
        if qussiton_g(anwser_user):
            score_user = score()
            randnum = randint(0, 100)
            continue
        else:
            print ("Thanks for play, bye T_T")
            break
        
        
if __name__ == "__main__":
    main()
    
    
#MohammadHesam Pourakbar