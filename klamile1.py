with open('Format_Source.txt', 'r') as f:
    first = f.readlines()

l = []
def read_till_coordinates(first):
    for i in first[:19]:
        l.append(i)
        #print(i)
    return str(l)
def read_end(first):
    for i in first[33:35]:
        l.append(i)
        #print(i)
    return str(l)
read_till_coordinates(first)
read_end(first)

with open('outputtrial1.txt','w') as f1:
    for i in l:
        f1.write(i)

