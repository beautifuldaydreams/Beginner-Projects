import random
word = ""


def find_word():
    with open("sowpods.txt", "r") as f:
        words = f.readlines()
        global word
        index = random.randint(0, len(words)-1)
        word = words[index].strip()
    return word


def play():
    global word
    find_word()
    guessed_words = []
    guessed_letters = []
    guessed = False
    tries = 6
    print("Welcome to Hangman!")
    empty_str = ("_"*len(word))
    print(empty_str)

    while guessed is False and tries > 0:
        guess = input("Please enter a letter or a word:").strip().upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You have already guessed this letter. Try again.")
            elif guess not in word:
                print("Bad luck. This letter is not in the word.")
                tries -= 1
                print("You have {} tries left.".format(tries))
                guessed_letters.append(guess)
            else:
                print("Yay! the letter", guess, " is in the word!")
                guessed_letters.append(guess)
                word_completion = list(empty_str)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_completion[index] = guess
                empty_str = "".join(word_completion)
                print(empty_str)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You have already guessed this word, please try again.")
            elif guess != word:
                print("Try again, this word is incorrect.")
                tries -= 1
                print("You have {} tries left.".format(tries))
                guessed_words.append(guess)
            else:
                guessed = True
                break
        else:
            print("Your input was invalid.")
    if guessed is True:
        print("Hooray! You won the game!")
    else:
        print("Yikes man. Big Yikes. The word was {}".format(word))


def main():
    play()
    while input("Do you what to play again? Enter (y/n)").upper() == "Y":
        play()


if __name__ == '__main__':
    main()
