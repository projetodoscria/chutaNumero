from random import randrange


class LoadNumber():

    def __init__(self, level):
        self.__random_number = randrange(100)  # Inicializa uma váriavel no metódo construtor com um número randomico de 1 a 100
        self.__attempt_number = None
        self.__user_number = None
        self.__level = level

    @property
    def attempt_number(self):
        return self.__attempt_number

    def assign_input_for_of_user(self) -> int:
        self.__user_number = int(input("Chute um numero: \n"))
        return self.__user_number
        
    def valid_number_if_user_number_is_correct(self) -> bool:
        return self.__random_number == self.__user_number

    def valid_lose_or_new_try(self):
        
        if self.__attempt_number > 0:
            print(f"Voce ainda tem {self.__attempt_number - 1} tentativas!")
            self.__attempt_number = self.__attempt_number - 1
            
            if self.__attempt_number == 0:
                print(f"Voce Perdeu, o numero era {self.__random_number}")

    def clue(self):
        
        if self.__user_number > self.__random_number:
            print("Digite um numero menor")
        else:
            print("Digite um numero maior")

        
        

    def set_attempt_number(self):
        levels = {
            'Facil': 10,
            'Normal': 5,
            'Dificil': 3,
        }

        for key, value in levels.items():
            if str.lower(key) == str.lower(self.__level):
                self.__attempt_number = value
                break
                
                
    