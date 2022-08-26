from json import load
from core import LoadNumber

class Automation():
    def __init__(self):
        self.__load_number = LoadNumber
        self.__level = ['facil', 'normal', 'dificil']
    
    def play_game(self, select_level: str):
        
        if str.lower(select_level) in self.__level:
            load_number = self.__load_number(select_level)
            load_number.set_attempt_number()
            
            while load_number.attempt_number > 0:
                load_number.assign_input_for_of_user()
                result = load_number.valid_number_if_user_number_is_correct()
                if result:
                    print("PARABENS VOCE GANHOU")
                    break
                load_number.clue()
                load_number.valid_lose_or_new_try()
                

                