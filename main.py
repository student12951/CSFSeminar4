def encode(message):
    encoded_message = ""
    i = 0
    while (i <= len(message) - 1):
        count = 1
        char = message[1]
        j = i
        while (j < len(message) - 1):
            if (message[j] == message[j + 1]):
                count += 1
temp = "something"
index = len(temp) - 1
for x in temp:
    char = ""
    count = 0
    countOfNum = 0
    while (count < index):
        if (x[count] == x[count + 1]):
            char = x[count]
            countOfNum += 1

print(countOfNum);;
