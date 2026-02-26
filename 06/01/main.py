def readLines(fileName):
    array = []
    
    with open(fileName, 'r') as file:
        for line in file:
            array.append(line.strip())

    return array

def splitLines(lines):
    sizes = []
    lastRow = lines[-1]
    size = 1

    for i in range(len(lastRow)):
        if i == 0:
            continue

        if lastRow[i] == "+" or lastRow[i] == "*":
            sizes.append(size - 1)
            size = 0

        size += 1

    return sizes



def main():
    lines = readLines('../test-input.txt')
    sizes = splitLines(lines)

    for y in range(len(lines)):
        for x in range(len(lines[y])):
            numbers = []

                numbers.append(lines[y][x + sizes[]])

            print(numbers)

main()