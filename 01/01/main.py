def readLines(fileName):
    array = []
    
    with open(fileName, 'r') as file:
        for line in file:
            array.append(line.strip())

    return array

def main():
    input = readLines('../input.txt')

    position = 50
    count = 0

    for move in input:
        dir = move[0]
        rawDistance = int(move.replace('L', '').replace('R', ''))
        distance = -rawDistance if dir == "L" else rawDistance
        position = (position + distance) % 100
        if position == 0:
            count += 1

    print(f"COUNT: {count}")


main()