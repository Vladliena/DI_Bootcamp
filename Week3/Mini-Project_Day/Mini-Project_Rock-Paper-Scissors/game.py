import random

class Game:
    
    list_of_choices = ['rock','scissors','paper']
    
    def __init__(self):
     self.result = {
        'draw' : 0,
        'win' : 0,
        'loss' : 0
    }
        
    def get_user_item(self):
         try:
            while True:
              user_choice = input('rock,scissors or paper?')
              if user_choice != 'rock' or user_choice != 'scissors' or user_choice != 'paper':
                raise ValueError ('You used the wrong word')
              else:
                 break
         finally:
             return user_choice
             
    def get_computer_item(self):
        computer_action = random.choice(Game.list_of_choices)
        return computer_action
    
    def get_game_result(self,user_action,computer_action):
        if user_action == computer_action:
         self.result['draw'] += 1
         return 'draw'
        elif user_action == "rock":
         if computer_action == "scissors":
            self.result['win'] += 1
            return 'win'
         else:
            self.result['loss'] += 1
            return 'loss'
        elif user_action == "paper":
         if computer_action == "rock":
            self.result['win'] += 1
            return 'win'
         else:
            self.result['loss'] += 1
            return 'loss'
        elif user_action == "scissors":
         if computer_action == "paper":
            self.result['win'] += 1
            return 'win'
         else:
            self.result['loss'] += 1
            return 'loss'
        return self.result
            
    def play(self):
        user = self.get_user_item()
        computer = self.get_computer_item()
        game_result = self.get_game_result(user,computer)
        print(f'{user} {game_result} {computer}')
        return game_result
        
