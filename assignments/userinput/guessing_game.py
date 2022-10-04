def start():
    '''
    This function starts the guessing game loop logic. The function will poll and wait
    until the user inputs their guess and will exit once some conditions are met.
    '''

    answer = "panda"
    guess_count = 0
    guess_limit = 3
    guess = None
    while guess_count < guess_limit:
        guess = input("Guess an animal: ")
        guess_count += 1
        if guess == answer:
            print("Congrats you won, Go Home")
            break
        if guess == "quit":
            print("Exiting...")
            break
        else:
            print("wrong answer nerd, guess again")

    return answer


start()
