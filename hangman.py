import random

# List of words to choose from
word_list = ["python", "programming", "hangman", "challenge", "openai", "artificial", "intelligence"]

def choose_word():
    return random.choice(word_list)

def display_word(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def play_hangman():
    word = choose_word()
    guessed_letters = set()
    attempts = 6  # Number of allowed wrong guesses

    print("Adam Asmaca Oyununa Hoşgeldiniz!")
    print("Bir kelime seçildi. Haydi başlayalım!")

    while attempts > 0:
        print(f"Kalan tahmin hakkınız: {attempts}")
        print(display_word(word, guessed_letters))

        guess = input("Bir harf tahmin edin: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Lütfen sadece bir harf giriniz.")
            continue

        if guess in guessed_letters:
            print(f"'{guess}' harfini zaten tahmin ettiniz.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(f"Tebrikler! '{guess}' harfi kelimede var.")
            if all(letter in guessed_letters for letter in word):
                print(f"Tebrikler! Kelimeyi buldunuz: {word}")
                break
        else:
            print(f"Maalesef! '{guess}' harfi kelimede yok.")
            attempts -= 1

    if attempts == 0:
        print(f"Kaybettiniz! Kelime: {word}")

if __name__ == "__main__":
    play_hangman()
