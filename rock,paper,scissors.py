import random

def get_user_choice():
    choices = {"1": "taş", "2": "kağıt", "3": "makas"}
    print("Seçiminizi yapın:")
    print("1: Taş")
    print("2: Kağıt")
    print("3: Makas")
    choice = input("Seçiminizi girin (1, 2, veya 3): ")
    while choice not in choices:
        print("Geçersiz seçim. Lütfen tekrar deneyin.")
        choice = input("Seçiminizi girin (1, 2, veya 3): ")
    return choices[choice]

def get_computer_choice():
    choices = ["taş", "kağıt", "makas"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Berabere!"
    elif (user_choice == "taş" and computer_choice == "makas") or \
         (user_choice == "kağıt" and computer_choice == "taş") or \
         (user_choice == "makas" and computer_choice == "kağıt"):
        return "Kazandınız!"
    else:
        return "Kaybettiniz!"

def play_game():
    print("Taş, Kağıt, Makas Oyununa Hoşgeldiniz!")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"Sizin seçiminiz: {user_choice}")
    print(f"Bilgisayarın seçimi: {computer_choice}")

    result = determine_winner(user_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    play_game()
