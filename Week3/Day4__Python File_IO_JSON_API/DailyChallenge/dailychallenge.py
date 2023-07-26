from collections import Counter
import string
from stop_words import get_stop_words


# Part I
# First, we will analyze a simple string, like “A good book would sometimes cost as much as a good house.”

# Create a class called Text that takes a string as an argument and store the text in a attribute.
# Hint: You need to manually copy-paste the text, straight into the code

# Implement the following methods:
# a method to return the frequency of a word in the text (assume words are separated by whitespace) return None or a meaningful message.
# a method that returns the most common word in the text.
# a method that returns a list of all the unique words in the text.



class Text:
    def __init__(self,text='A good book would sometimes cost as much as a good house'):
        self.text = text
        
    def words_number_and_common(self):
       freq = Counter(self.text.lower().split()).most_common()
       return print(freq)
    
    def unique_words(self):
        unique_words = list(set(self.text.lower().split(' ')))
        return print(unique_words)
    
    def new_text(self):
        with open('the_stranger.txt','r') as file:
         self.text = file.read().replace('\n', '')
        return self.text

       
text1 = Text()
text1.words_number_and_common()
text1.unique_words()
text1.new_text()


# Part II
# Then, we will analyze a text coming from an external text file. Download the_stranger.txt file.

# Implement a classmethod that returns a Text instance but with a text file:

#     >>> Text.from_file('the_stranger.txt')
# Hint: You need to open and read the text from the text file.


# Now, use the provided the_stranger.txt file and try using the class you created above.



# Bonus:
# Create a class called TextModification that inherits from Text.

# Implement the following methods:
# a method that returns the text without any punctuation.
# a method that returns the text without any english stop-words (check out what this is !!).
# a method that returns the text without any special characters.
# Note: Feel free to implement/create any attribute, method or function needed to make this work, be creative :)

class TextModification(Text):
    
    def __init__(self,text):
        super().__init__(text)
        self.text = text
        
    def no_punctuation(self):
        self.text = self.text.translate(str.maketrans('', '', string.punctuation))
        return print(self.text)
    
    def remove_stop_words(self):
        stop_words = list(get_stop_words('en'))
        new_list = [word for word in self.text.split(' ') if not word in stop_words]
        return print(*new_list)
    
    def delete_special_characters(self):
        normal_string=list(ch for ch in self.text.split(' ') if ch.isalnum())
        return print(*normal_string)
    
text2 = TextModification(text1.text)
text2.no_punctuation()
text2.remove_stop_words()
text2.delete_special_characters()


