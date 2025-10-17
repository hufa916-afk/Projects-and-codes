import psutil
import time
import platform
import os

# Function to play alert sound
def play_alert():
    system = platform.system()
    
    if system == "Windows":
        import winsound
        winsound.Beep(1000, 1000)  # Frequency, Duration(ms)
    
    elif system == "Linux" or system == "Darwin":  # macOS = Darwin
        # You can replace 'say' with 'aplay' or 'paplay' if using a custom sound file
        os.system('say "Warning, high memory usage!"')  # macOS voice alert
        # Example for sound file: os.system('aplay /path/to/sound.wav') or paplay
    
    else:
        print("\a")  # Fallback beep

# Monitor RAM usage
while True:
    ram_usage = psutil.virtual_memory().percent
    print(f"Current RAM Usage: {ram_usage}%")
    
    if ram_usage > 90:
        print("⚠ High RAM usage detected! Playing alert...")
        play_alert()
    
    time.sleep(5)  # Check every 5 seconds
