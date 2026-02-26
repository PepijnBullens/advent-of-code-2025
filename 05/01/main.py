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

    def inAnyRange(value):
        for start, end in parsedRanges:
            if start <= value <= end:
                return True
            if start > value:
                break
        return False

    count = sum(1 for a in available if inAnyRange(int(a)))

    print(f"COUNT: {count}")

main()