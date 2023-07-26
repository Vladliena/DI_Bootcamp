# 🌟 Exercise 1 – Random Sentence Generator
# Instructions
# Description: In this exercise we will create a random sentence generator. We will do this by asking the user how long the sentence should be and then printing the generated sentence.

# Hint : The generated sentences do not have to make sense.

# Download this word list

# Save it in your development directory.

# Create a function called get_words_from_file. This function should read the file’s content and return the words as a collection. What is the correct data type to store the words?

# Create another function called get_random_sentence which takes a single parameter called length. The length parameter will be used to determine how many words the sentence should have. The function should:
# use the words list to get your random words.
# the amount of words should be the value of the length parameter.

# Take the random words and create a sentence (using a python method), the sentence should be lower case.

# Create a function called main which will:

# Print a message explaining what the program does.

# Ask the user how long they want the sentence to be. Acceptable values are: an integer between 2 and 20. Validate your data and test your validation!
# If the user inputs incorrect data, print an error message and end the program.
# If the user inputs correct data, run your code.

import random

def get_all_words(file_text):
    with open(file_text, 'r') as f_object:
     word_lst = f_object.read().split()
    return word_lst

def random_sentence(lenght):
    words = get_all_words('sowpods.txt')
    random_sentence = ' '.join(random.choices(words, k=lenght))
    return print(random_sentence.lower())

def main():
    print('We will generate a sentence for you')
    try:
        lenght = int(input('Tell me the lenght of sentence 2-20: '))
        if 2 <= lenght >= 20:
            raise ValueError
        else:
            return random_sentence(lenght)
    except ValueError:
        print('write number 2-20')
    
    
main()

# 🌟 Exercise 2: Working With JSON
# Instructions
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""


# Access the nested “salary” key from the JSON-string above.
# Add a key called “birth_date” to the JSON-string at the same level as the “name” key.
# Save the dictionary as JSON to a file.

import json

data = json.loads(sampleJson)

def add_keys_nested_dict(list):
    try:
     list["company"]["employee"]["birth_date"] = "1993,07,14"
     json_file = "my_file.json"
     salary_value = data["company"]["employee"]["payable"]["salary"]
     with open(json_file, 'w') as file_obj:
      json.dump(list, file_obj)
      return print(salary_value)
    except KeyError:
        print('The specified key does NOT exist')
        

add_keys_nested_dict(data)








