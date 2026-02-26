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
        original = position

        dir = move[0]
        rawDistance = int(move.replace('L', '').replace('R', ''))
        distance = -rawDistance if dir == "L" else rawDistance
        new_position = original + distance

        if dir == "R":
            zeros = (original + rawDistance) // 100
        else:
            adjusted = original if original > 0 else 100
            zeros = (rawDistance - adjusted) // 100 + 1 if rawDistance >= adjusted else 0
        
        position = new_position % 100

        count += zeros

    print(f"COUNT: {count}")


main()