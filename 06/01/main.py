import math

def readLines(fileName):
    array = []
    
    with open(fileName, 'r') as file:
        for line in file:
            array.append(line)

    return array

def splitLines(lines):
    sizes = []
    lastRow = lines[-1]
    
    size = 1

    for i in range(len(lastRow) - 1):
        if lastRow[i] == "+" or lastRow[i] == "*" and size > 1:
            sizes.append(size - 1)
            size = 1
        size += 1
    sizes.append(size)

    return sizes



def main():
    lines = readLines('../input.txt')
    sizes = splitLines(lines)

    equations = []

    for y in range(len(lines)):
        sortedEquations = []

        for i in range(len(sizes)):
            start = sum(sizes[:i])
            end = start + sizes[i]
            sortedEquations.append(lines[y][start:end].strip())
        
        equations.append(sortedEquations)

    equations = [list(col) for col in zip(*equations)]

    count = 0

    for digits in equations:
        int_digits = [int(d) for d in digits[:-1] if d.strip()]
        if digits[-1] == "*":
            result = math.prod(int_digits)
        else:
            result = sum(int_digits)
        count += result

    print(f"COUNT: {count}")

main()