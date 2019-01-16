import threading
import time
import random

list = [0,0,0,0,0]

def boatthread(count):
    boat = count
    while list[boat] < 200:
        list[boat] += 1
        time.sleep(random.randrange(0, 10, 1) / 100.0)

for progress in range(5):  # der må max være 5 samtidige forespørgsler/forbindelse
    boat = threading.Thread(target=boatthread, args= (progress,))
    boat.start()

def print_boats():
    for i in range(10):
        print()
    for boat in range(5):
        progress = list[boat]
        string = ""
        for space in range(int(progress)):
            string += " "
        string += "<" + str(boat) + ">"
        print(string)
    time.sleep(0.2)

while 200 not in list:
    print_boats()

print_boats()