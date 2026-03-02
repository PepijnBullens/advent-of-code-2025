def readLines(fileName):
    array = []
    
    with open(fileName, 'r') as file:
        for line in file:
            array.append(line.strip())

    return array


def countTimelines(coords, gridHeight, lines, memo):
    if coords[1] < 0 or coords[1] >= len(lines[0]) or coords[0] >= gridHeight:
        return 1
    
    key = tuple(coords)
    if key in memo:
        return memo[key]
    
    if coords[0] + 1 < gridHeight and lines[coords[0] + 1][coords[1]] == "^":
        result = countTimelines([coords[0] + 1, coords[1] - 1], gridHeight, lines, memo) + countTimelines([coords[0] + 1, coords[1] + 1], gridHeight, lines, memo)
    else:
        result = countTimelines([coords[0] + 1, coords[1]], gridHeight, lines, memo)
    
    memo[key] = result
    return result


def main():
    lines = readLines('../input.txt')

    memo = {}
    start = lines[0].index("S")
    gridHeight = len(lines)
    
    count = countTimelines([0, start], gridHeight, lines, memo)

    print(f"COUNT: {count}")

main()