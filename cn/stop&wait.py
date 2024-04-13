size = int(input("Enter no of frames: "))

frames = []

for i in range(0, size):
    frames.append(int(input(f"Enter the frame {i}: ")))

index = 0

while(index < size):
    print(f"Frame {index + 1} is sent")
    ack = int(input("Waiting for acknowledgement: "))
    if(ack == index + 2):
        print(f"Acknowledgement is received for next frame {index + 2}")
        index += 1
    else:
        print(f"Acknowledgement is not received for next frame {index + 2}")
        print(f"Resending frame {index + 1}")

print("No more frames avilable!")