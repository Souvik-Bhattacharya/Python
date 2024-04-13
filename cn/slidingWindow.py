size = int(input("Enter no of frames: "))

window = int(input("Enter window size: "))

frames = []

for i in range(0, size):
    frames.append(int(input(f"Enter the frame {i + 1}: ")))

for i in range(0, size):
    if((i + 1) % window == 0):
        print(f"Frame {i + 1} is sent: {frames[i]}")
        print("Acknowledgement is received for above frames")
    else:
        print(f"Frame {i + 1} is sent: {frames[i]}")

print("Acknowledgement is received for above frames")

print("No more frames avilable!")