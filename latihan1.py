kata_rahasia = "python"
tebakan_benar = ""

while True:
    tebak = input("Guess a letter: ").lower() 
    
    if not tebak.isalpha() or len(tebak) != 1:
        print("inser the majigcal letter")
        continue

    if tebak in kata_rahasia:
        print(f"Yes! '{tebak}'thats the one.")
        tebakan_benar += tebak
    else:
        print(f"No, '{tebak}' is not in the secret word '{kata_rahasia}'.")
