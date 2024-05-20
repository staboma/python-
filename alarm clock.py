import time
import datetime
import os

def set_alarm():
    alarm_time = input("Alarm zamanını HH:MM formatında girin: ")
    try:
        valid_time = datetime.datetime.strptime(alarm_time, "%H:%M")
        return alarm_time
    except ValueError:
        print("Geçersiz zaman formatı. Lütfen tekrar deneyin.")
        return set_alarm()

def play_alarm_sound():
    # For Windows, you can use winsound module
    try:
        import winsound
        frequency = 2500  # Set Frequency in Hertz
        duration = 1000   # Set Duration in milliseconds
        winsound.Beep(frequency, duration)
    except ImportError:
        # For other systems, use the os module to play a sound file
        # Ensure 'alarm.mp3' or any sound file is in the same directory or provide the full path
        os.system("afplay alarm.mp3")  # For macOS
        # os.system("mpg123 alarm.mp3") # For Linux with mpg123 installed

def main():
    alarm_time = set_alarm()
    print(f"Alarm {alarm_time} için kuruldu.")

    while True:
        current_time = datetime.datetime.now().strftime("%H:%M")
        if current_time == alarm_time:
            print("Alarm! Zamanı geldi.")
            play_alarm_sound()
            break
        time.sleep(1)

if __name__ == "__main__":
    main()
