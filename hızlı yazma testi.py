import time
import random

def get_random_word():
    words = ["python", "programming", "coding", "keyboard", "speed", "accuracy", "challenge", "test", "performance", "skill"]
    return random.choice(words)

def typing_test():
    print("Hızlı Yazma Testine Hoş Geldiniz!")
    print("Verilen kelimeyi mümkün olduğunca hızlı ve doğru bir şekilde yazın.")
    print("Başlamak için 'enter' tuşuna basın...")
    input()
    
    num_words = 5
    correct_words = 0
    total_time = 0
    
    for _ in range(num_words):
        word = get_random_word()
        print(f"Yazılması gereken kelime: {word}")
        
        start_time = time.time()
        user_input = input("Kelimeyi yazın: ")
        end_time = time.time()
        
        time_taken = end_time - start_time
        total_time += time_taken
        
        if user_input == word:
            correct_words += 1
            print(f"Doğru! Süre: {time_taken:.2f} saniye")
        else:
            print(f"Yanlış! Doğru kelime '{word}' idi. Süre: {time_taken:.2f} saniye")
    
    accuracy = (correct_words / num_words) * 100
    average_time = total_time / num_words
    
    print("\nTest Tamamlandı!")
    print(f"Doğru Yazılan Kelimeler: {correct_words}/{num_words}")
    print(f"Doğruluk Oranı: {accuracy:.2f}%")
    print(f"Ortalama Süre: {average_time:.2f} saniye")

if __name__ == "__main__":
    typing_test()

