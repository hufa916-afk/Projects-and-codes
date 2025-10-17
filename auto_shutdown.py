import psutil, os, time

idle_time = 0

while True:
    if psutil.cpu_percent() < 10:  
        idle_time += 1
    else:
        idle_time = 0

    if idle_time == 300:  # 5 minutes = 300 seconds
        print("System idle too long. Shutting down...")
        os.system("shutdown /s /t 10" if os.name == "nt" else "shutdown now")
    time.sleep(1)
