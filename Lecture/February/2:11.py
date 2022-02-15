# 2/11

with open("pride_prejudice.txt", "r") as f:
    # text = f.read() # one big string
    # line = f.readline() # only 1 line
    lines = f.readlines() # text into lines

with open("text_file.txt", "w") as outfile:
    outfile.write("one\ntwo\nthree")
# print(text[:1000])
# print(line)
# print(lines[:10])
print(len("\n\t\\\"")) # 4

def num_passengers():
    with open("airtravel.csv", "r") as infile:
        lines = infile.readlines()
        datalines = lines[1:]
        print(datalines)

    average = 0
    average_count = 0
    for line in datalines:
        line in line.strip()
        pieces = line.split(",")
        if len(pieces) < 4:
            continue
        value = int(pieces[3])
        average += value
        average_count += 1
    print(average / average_count)

num_passengers()
