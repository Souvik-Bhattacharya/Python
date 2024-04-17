# Go-Back-N
import random

frames = int(input("Enter no of frames: "))
windows = int(input("Enter the window size: "))

index = 1
transmissions = 0

while(index <= frames):
    count = 0
    for i in range(index, index + windows):
        if i > frames:
            break
        print(f"Frame {i} is sent!")
        transmissions += 1
    for i in range(index, index + windows):
        if i > frames:
            break
        flag = random.randint(1, 10) % 2
        if flag == 0:
            print(f"Frame {i} is acknowledged!")
            count += 1
        else:
            print(f"Frame {i} is not acknowledged")
            print(f"Resending frames from frame {i}")
            break
    index += count
print(f"Total no of transmissions is {transmissions}")