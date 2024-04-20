# cyclic redundancy check

def send(data, key):
    data = [int(i) for i in data]
    key = [int(i) for i in key]

    temp = []

    keyLen = len(key)

    for i in range(0, keyLen - 1):
        data.append(0)

    dataLen = len(data)

    index = 0

    while(index < keyLen):
        temp.append(data[index])
        index += 1

    while(index < dataLen):
        for i in range(0, keyLen):
            temp[i] = temp[i] ^ key[i]
        
        while(temp[0] == 0 and index < dataLen):
            temp.pop(0)
            temp.append(data[index])
            index += 1

    if(temp[0] != 0):
        for i in range(0, keyLen):
            temp[i] = temp[i] ^ key[i]
    
    temp.pop(0)

    for i in range(dataLen - keyLen + 1, dataLen):
        data[i] = temp[i - dataLen + keyLen - 1]
    
    data = [str(i) for i in data]

    return "".join(data)

def receive(data, key):
    data = [int(i) for i in data]
    key = [int(i) for i in key]

    temp = []

    keyLen = len(key)

    for i in range(0, keyLen - 1):
        data.append(0)

    dataLen = len(data)

    index = 0

    while(index < keyLen):
        temp.append(data[index])
        index += 1

    while(index < dataLen):
        for i in range(0, keyLen):
            temp[i] = temp[i] ^ key[i]
        
        while(temp[0] == 0 and index < dataLen):
            temp.pop(0)
            temp.append(data[index])
            index += 1

    if(temp[0] != 0):
        for i in range(0, keyLen):
            temp[i] = temp[i] ^ key[i]
    
    temp.pop(0)

    for i in temp:
        if i != 0:
            return False
    
    return True

data = list(input("Enter the data: "))
key = list(input("Enter the key: "))

encodedData = send(data, key)
print("Encoded data is: " + encodedData)

receivedData = list(input("Enter the data: "))
result = receive(receivedData, key)
if(result):
    print("Error free data received")
else:
    print("Data received with error")