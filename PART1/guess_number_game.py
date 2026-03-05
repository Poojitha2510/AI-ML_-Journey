#design a small game
#problem statement first we decide a number then ask user to guess the number if the guess number is less than number then habe to increase and if greater then decrese
number=57
def play_single_game():

    guess=int(input("enter the guess number"))

    if guess==number:
        print("guess is correct")
    elif guess<number:
        print("you have guessed the small number")
    else:
        print("you have guessed the big number")
while True:
    play_single_game()

    playAagain=input("do you want to play again")
    if playAagain=="No":
        break
    
