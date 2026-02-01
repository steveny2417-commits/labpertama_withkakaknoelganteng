def updateText(secret_word, guessed_letters):
    display = ""
    for char in secret_word:
        if char.lower() in guessed_letters:
            display += char + " "
        else:
            display += "_ "
    return display.strip()

def main_game(secret_word):
    guessed_letters = []
    chances = 6
    secret_word_lower = secret_word.lower()

    print("--- Selamat Datang di Hangman! ---")
    
    while chances > 0:
        current_display = updateText(secret_word, guessed_letters)
        print(f"\nKata: {current_display}")
        print(f"Sisa kehidupan : {chances}")
        if "_" not in current_display:
            print(f"Selamat! Anda menang! Kata rahasianya adalah: {secret_word}")
            return

        
        guess = input("tebak dulu le : ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print(" satu huruf saja!")
            continue

        if guess in guessed_letters:
            print(f"cari huruf lain lah huruv '{guess}' udh ada bang 🗿")
            continue

        guessed_letters.append(guess)

        if guess in secret_word_lower:
            print(f"nice , huruf  '{guess}' ada di dalam kata!")
        else:
            chances -= 1
            print(f"Maaf, huruf '{guess}' tidak ada.")

    
    print(f"\ntetot anda kalah!. Katanya adalah: {secret_word}")


main_game("Indonesia")
  