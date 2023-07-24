# Exercise 1 : Call History
# Instructions
# Create a class called Phone. This class takes a parameter called phone_number. When instantiating an object create an attribute called call_history which value is an empty list.

# Add a method called call that takes both self and other_phone (i.e another Phone object) as parameters. The method should print a string stating who called who, and add this string to the phone’s call_history.

# Add a method called show_call_history. This method should print the call_history.

# Add another attribute called messages to your __init__() method which value is an empty list.

# Create a method called send_message which is similar to the call method. Each message should be saved as a dictionary with the following keys:
# to : the number of another Phone object
# from : your phone number (also a Phone object)
# content

# Create the following methods: show_outgoing_messages(self), show_incoming_messages(self).

# Test your code !!!

class Phone:
    messages = []
    
    def __init__(self,phone_number):
        self.number = phone_number
        self.call_history = []
        
    def call(self,other_phone):
        call = f'{other_phone.number} called {self.number}'
        print(call)
        self.call_history.append(call)
        
    def show_call_history(self):
        for call in self.call_history:
            print(call)
            
    def send_message(self,to_number,content):
        message = {
            'from':self.number,
            'to':to_number.number,
            'content':content
        }
        Phone.messages +=[message]
        
    def show_outgoing_messages(self):
        for message in Phone.messages:
            if message['from'] == self.number :
                print(f"To: {message['to']}\n message: {message['content']}")
                
    
    def show_incoming_messages(self):
        for message in Phone.messages:
            if message['to'] == self.number :
                print(f"From: {message['from']}\n message: {message['content']}")
            
        
    
        
call1 = Phone(111111)
call2 = Phone(222222)

call2.call(call1)
call1.show_call_history()

call1.send_message(call2,'Hello my friend')
call1.send_message(call2,'Please call my friend')
call2.send_message(call1,'Will call you latter')
call1.show_outgoing_messages()
call2.show_incoming_messages()