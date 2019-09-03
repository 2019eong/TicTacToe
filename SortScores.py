infile = open("scores.txt", "r")
outfile = open("sorted.txt", "w")
d = []
for line in infile:
    temp = line.split()
    d.append((temp[1], temp[0]))
d.sort(reverse=True)
for a, b in d:
    print(b + "\t" + a, file=outfile)
outfile.close()