import random
import time

# Initial Steps to invite in the game:
print("\nKelokentoki frai chicken\n")
name = input("Tire su nombre depue de la 12: ")
print("Dime a ve " + name + "! Vamo al game")
time.sleep(2)
print("Moriremosss!\n Juguemos el ahorcaito!")
time.sleep(3)


# The parameters we require to execute the game:
def main():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    words_to_guess = ["january","border","image","film","promise","kids","lungs","doll","rhyme","damage"
                   ,"plants", "itachi"]
    word = random.choice(words_to_guess)
    length = len(word)
    count = 0
    display = '_' * length
    already_guessed = []
    play_game = ""

# A loop to re-execute the game when the first round ends:

def play_loop():
    global play_game
    play_game = input("Soporta otra vuelta? s = si, n = no \n")
    while play_game not in ["s", "n","S","N"]:
        play_game = input("Soporta otra vuelta? s = si, n = no \n")
    if play_game == "s":
        main()
    elif play_game == "n":
        print("Po rueda durisimo mmñ!")
        exit()

# Initializing all the conditions required for the game:
def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game
    limit = 5
    guess = input("Eta e tu palabra: " + display + " Adivina: \n")
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("Trata de nuevo fuap\n")
        hangman()


    elif guess in word:
        already_guessed.extend([guess])
        index = word.find(guess)
        word = word[:index] + "_" + word[index + 1:]
        display = display[:index] + guess + display[index + 1:]
        print(display + "\n")

    elif guess in already_guessed:
        print("Prueba otra letra buen ñame.\n")

    else:
        count += 1

        if count == 1:
            time.sleep(1)
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Siga boyando. " + str(limit - count) + " vida te quedan\n")

        elif count == 2:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Fuap, siga boyando. " + str(limit - count) + " vida que te quedan\n")

        elif count == 3:
           time.sleep(1)
           print("   _____ \n"
                 "  |     | \n"
                 "  |     |\n"
                 "  |     | \n"
                 "  |      \n"
                 "  |      \n"
                 "  |      \n"
                 "__|__\n")
           print("No la pegate, siga boyando. " + str(limit - count) + " vida que te quedan\n")

        elif count == 4:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("A ti hay que darte es, siga boyando. " + str(limit - count) + " ultima vida\n")

        elif count == 5:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")
            print("Adivina. Fuap, guindate lo teni\n")
            print("La palabra era:",already_guessed,word, "Etupido")
            play_loop()

    if word == '_' * length:
        print("Balbaro 99, la pegate")
        play_loop()

    elif count != limit:
        hangman()


main()


hangman()

