n = int(input("Enter n: "))
socks = input("Enter space separated values: ")

# List of Socks from Strings
temp_socks = []
for sock in socks.split():
    # convert individual sock elements from string > int
    temp_socks.append(int(sock))

socks = temp_socks
pair = 0

socks_set = list(set(socks))

for value in socks_set:
    pair += socks.count(value) / 2

while len(socks) != 0:
    t = socks.pop()
    if t in socks:
        pair += 1
        socks.remove(t)
    else:
        continue
print (pair)