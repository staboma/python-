import time

def countdown(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1

    print('Zaman doldu!')

# Örnek kullanım
countdown(10)  # 10 saniyelik geri sayım
