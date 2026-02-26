def readLines(fileName):
    array = []
    
    with open(fileName, 'r') as file:
        for line in file:
            array.append(line.strip())

    return array

def main():
    lines = readLines('../input.txt')

    lines = [list(line) for line in lines]

    count = 0

    cases = [
        [-1, -1],
        [-1, 0],
        [-1, 1],

        [0, -1],
        [0, 1],

        [1, -1],
        [1, 0],
        [1, 1]
    ]

    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x] != "@":
                continue

            rollCount = 0

            for newY, newX in cases:
                if y + newY >= 0 and y + newY < len(lines) and x + newX >= 0 and x + newX < len(lines[y]) and lines[y + newY][x + newX] == "@":
                    rollCount += 1

            if rollCount < 4:
                count += 1

    print(f"COUNT: {count}")



main()