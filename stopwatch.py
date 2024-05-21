import time

def stopwatch():
    start_time = time.time()
    print("Zamanlayıcı başlatıldı. Durdurmak için CTRL+C'ye basın.")
    
    try:
        while True:
            elapsed_time = time.time() - start_time
            mins, secs = divmod(elapsed_time, 60)
            hours, mins = divmod(mins, 60)
            timer = '{:02d}:{:02d}:{:02d}'.format(int(hours), int(mins), int(secs))
            print(timer, end="\r")
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nZamanlayıcı durduruldu.")

# Örnek kullanım
stopwatch()
