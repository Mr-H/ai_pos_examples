exemplars = []
file = open("train.txt", 'r');
for line in file:
    data = tuple([wrd.lower() for wrd in line.split()])
    print(data)
    #exemplars += [ (data[0::1], data[0::2]), data[0::3] ]
file.close()

print(exemplars[0::1])
