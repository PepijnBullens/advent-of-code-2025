def readLines(fileName):
    array = []
    
    with open(fileName, 'r') as file:
        for line in file:
            array.append(line.strip())

    return array


def moveDownRecursion(beams, coords, gridHeight, lines):
    if coords[1] < 0 or coords[1] >= len(lines[0]) or coords[0] >= gridHeight:
        return 0
    if tuple(coords) in beams:
        return 0
    
    beams.add(tuple(coords))
    
    if coords[0] + 1 < gridHeight and lines[coords[0] + 1][coords[1]] == "^":
        return 1 + moveDownRecursion(beams, [coords[0] + 1, coords[1] - 1], gridHeight, lines) + moveDownRecursion(beams, [coords[0] + 1, coords[1] + 1], gridHeight, lines)
    else:
        return moveDownRecursion(beams, [coords[0] + 1, coords[1]], gridHeight, lines)


def main():
    lines = readLines('../input.txt')

    beams = set()
    start = lines[0].index("S")
    gridHeight = len(lines)
    
    count = moveDownRecursion(beams, [0, start], gridHeight, lines)

    print(f"COUNT: {count}")

main()