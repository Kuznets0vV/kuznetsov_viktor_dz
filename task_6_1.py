with open('6.txt') as f:
    data = []
    for line in f:
        sp_line = line.split()
        data.append((sp_line[0], sp_line[5].replace('"', ''), sp_line[6]))
print(data)