import os
import random
import time

MAC = ("%02x:%02x:%02x:%02x:%02x:%02x" % (
    random.randint(0, 255),
    random.randint(0, 255),
    random.randint(0, 255),
    random.randint(0, 255),
    random.randint(0, 255),
    random.randint(0, 255)
    ))

Interface =input("Interface=")

def main():
    os.system("ip link set " + Interface + " " + MAC)
    time.sleep(3600)
    main()
main()