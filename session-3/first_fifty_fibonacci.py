l=[0,1]
for i in range(2,50):
    l.append(l[i-1]+l[i-2])
print(l)
