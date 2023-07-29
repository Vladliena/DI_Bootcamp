from anagam_cheker import AnagramChecker

def menu():
    print('***** Anagram Checker *****\n 1.Enter a word\n 2.Quit')
    

def user_input():
 while True:
    try:
        choice = int(input('What do you want to do? '))
        if choice == 1:
            word = input("Enter a word: ").strip()
            if len(word.split()) != 1:
                 raise ValueError("Error: Only a single word is allowed.")
            elif not word.isalpha():
                 raise ValueError("Error: Only string is allowed.")
            else:
                 return word
        elif choice == 2:
            return
    except ValueError as err:
            print(f'ERROR: {err} ')
            
def show_result(word,anagram_words):
    if anagram_words:
        anagram_str = ','.join(anagram_words)
        print (f' Your word: {word}\n this is a valid English word\n Anagrams for your word: {anagram_str}')
    else:
        print ('There is no anagrams to this word')
            
def main():
    checker = AnagramChecker()
    menu()
    choice = user_input()
    if choice == None:
        print('You quit the programm')
    else:
        anagrams = checker.is_valid_word(choice)
        show_result(choice,anagrams)
        

main()