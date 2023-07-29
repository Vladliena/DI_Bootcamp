from game import Game

    
          
def get_user_menu_choice():
 user_choices = ['New Game','Show scores','Quit']
 while True:
        choice = input("Enter your choice: ")
        if choice in user_choices:
            return choice
        else:
            print('You did a mistake')
        
def print_results(results):
    print("Game Results:")
    print(f"Wins: {results['win']}")
    print(f"Losses: {results['loss']}")
    print(f"Draws: {results['draw']}")
    print("Thanks for playing!")
        
def main():
    game = Game()
    while True:
        choice_main = get_user_menu_choice()
        if choice_main == 'New Game':
             game.play()
        elif choice_main == 'Show scores':
            print_results(game.result)
        elif choice_main == 'Quit':
            break

main()