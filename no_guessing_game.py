import random #"random" a python module imported

def greet(name):
    print("Welcome " , name)
greet("Overwatch") #"greet()" function being called

print("\nSelect one of the options below 👇🏿") #highlighting options for the user to select
print("1. Play game")
print("2. Help")
print("3. Exit")

choice = input("Enter your choice: ") #User enters desired choice

if choice == "1": #User chooses no 1
    print("Starting the game")

    def play_game(): # a function "play_game" is defined
# Use of "random" that was imported at the start
#Game below is sets secret_numbers to random
#changing after every run
       secret_number = random.randint(1, 10) 

       for r in range(3):
           guess = int(input("Guess a number: "))

           attempts_left = 2-r #calculates no. of attempts left

           if guess == secret_number:
               print("Correct guess")
               break
           elif guess > secret_number:
               print('Too high')
               print(
                     'Attempts left: ',
                      attempts_left
                    )

           elif guess < secret_number:
               print('Too low')
               print('Attempts left: ', attempts_left)
       else:
         print("wrong guess")
         print("Game over")
         print(
  	       "The secret number was: " ,
	       secret_number
	      )
    play_game() #function is called

elif choice == "2": #User selects choice 2 which is help menu
    print("Help menu:")

    def help_menu(): #help menu function is defined
       print("Guess the correct number between 1 and 10")
       print("You have 3 choices")
    help_menu() #help menu function is called

elif choice == "3":
       print("Exiting program") #The program exists upon choice 3
else:
       print("Invalid choice") #User enters anything that is invalid
