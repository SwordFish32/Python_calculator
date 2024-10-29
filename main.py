!pip install transformers

from transformers import pipeline, set_seed
import random

number1 = input('Enter your first number:')
number2 = input('Enter your second number:')

option = input('What do you want to do?(If you do not know ask for "help"):')

# Define functions for each operation

def add(num1, num2):
  print(int(num1),"+",int(num2),"=",int(num1) + int(num2))

def subtract(num1, num2):
  print(int(num1),"-",int(num2),"=",int(num1) - int(num2))

def multiply(num1, num2):
  print(int(num1),"×",int(num2),"=",int(num1) * int(num2))

def divide(num1, num2):
  print(int(num1),"÷",int(num2),"=",int(num1) / int(num2))


# Use the function based on user input
if option == 'help':
  print('You can ask to: add')
  print('You can ask to: subtract')
  print('You can ask to: multiply')
  print('You can ask to: divide')
  print('You can ask for two random numbers: random')
  print('You can ask for chatgpt: chatgpt')
  print('You can ask for help: help')
  print('You can ask to exit: exit')
elif option == 'exit':
  print('Exiting...')
elif option == 'add':
  add(number1, number2)
  break
elif option == 'subtract':
  subtract(number1, number2)
  break
elif option == 'multiply':
  multiply(number1, number2)
  break
elif option == 'divide':
  divide(number1, number2)
  break
elif option == 'random':
  number1 = random.randint(1,10)
  number2 = random.randint(1,10)
  print(number1,"and",number2)
  break
elif option == 'chatgpt':
  generator = pipeline('text-generation', model='gpt2')
set_seed(42)

def chatbot_response(prompt):
  """Generates a response to a user prompt using the GPT-2 model."""
  response = generator(prompt, max_length=150, num_return_sequences=1)
  return response[0]['generated_text']

while True:
  user_input = input("You: ")
  if user_input.lower() == 'exit':
    break

  bot_response = chatbot_response(user_input)
  print("Bot:", bot_response)
else:
  print('invalid input')
