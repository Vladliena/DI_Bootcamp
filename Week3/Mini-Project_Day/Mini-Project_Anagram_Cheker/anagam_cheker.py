class AnagramChecker():
    
    def __init__(self):
        path = r"C:\Users\masah\OneDrive\Documents\DI_Bootcamp\DI_Bootcamp_All\DI_Bootcamp\Week3\Mini-Project_Day\Mini-Project_Anagram_Cheker\sowpods.txt"
        with open(path, 'r') as file:
            self.text = file.read().lower().splitlines()
         
    def is_valid_word(self,word):
        main_word = word.lower()
        if word in self.text:
            return self.get_anagrams(main_word)
        else:
            return print('No such word in text')
    
    def get_anagrams(self,word):
        anagrams_list = []
        for alt in self.text:
         if sorted(word) == sorted(alt) and word != alt:
            anagrams_list.append(alt)
        return anagrams_list
        
        

