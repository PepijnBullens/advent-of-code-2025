def readLines(fileName):
    array = []
    
    with open(fileName, 'r') as file:
        for line in file:
            array.append(line.strip())

    return array

def splitLines(lines):
    ranges = []
    available = []

    switch = False
    for line in lines:
        if line == "":
            switch = True
            continue

        if switch:
            available.append(line)
        else:
            ranges.append(line)

    return [ranges, available]

def main():
    lines = readLines('../input.txt')
    [ranges, available] = splitLines(lines)

    parsedRanges = []
    for r in ranges:
        start, end = map(int, r.split("-"))
        parsedRanges.append((start, end))

    parsedRanges.sort()

    merged = []
    for start, end in parsedRanges:
        if merged and start <= merged[-1][1] + 1:
            merged[-1] = (merged[-1][0], max(merged[-1][1], end))
        else:
            merged.append((start, end))

    count = sum(end - start + 1 for start, end in merged)
    print(f"COUNT: {count}")

main()