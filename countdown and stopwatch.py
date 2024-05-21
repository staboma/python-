import time

def countdown(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(f"Geri Sayım: {timer}", end="\r")
        time.sleep(1)
        seconds -= 1

    print('Zaman doldu!')

def stopwatch():
    start_time = time.time()
    print("Zamanlayıcı başlatıldı. Durdurmak için CTRL+C'ye basın.")
    
    try:
        while True:
            elapsed_time = time.time() - start_time
            mins, secs = divmod(elapsed_time, 60)
            hours, mins = divmod(mins, 60)
            timer = '{:02d}:{:02d}:{:02d}'.format(int(hours), int(mins), int(secs))
            print(f"Zamanlayıcı: {timer}", end="\r")
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nZamanlayıcı durduruldu.")

def main():
    choice = input("Geri Sayım (1) veya Zamanlayıcı (2) seçin: ")
    if choice == '1':
        seconds = int(input("Geri sayım süresi (saniye cinsinden) girin: "))
        countdown(seconds)
    elif choice == '2':
        stopwatch()
    else:
        print("Geçersiz seçim!")

if __name__ == "__main__":
    main()
