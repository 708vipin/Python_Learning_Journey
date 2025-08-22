secret_word = "giraffe"
guess = ""
attempt = 0
attempt_limit = 3
out_of_attempts = False

while guess != secret_word and not(out_of_attempts):
    if attempt < attempt_limit:
        guess = input("Enter your guess: ")
        attempt += 1
    else:
        out_of_attempts = True
        

if out_of_attempts:
    print("Out of Guesses, YOU LOSE!")  
else:
    print("You win!")  
