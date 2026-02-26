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

    count = 0

    for i in range(len(sizes)):
        isAddition = lines[-1][sum(sizes[:i])] == "+"

        total = 0

        for j in range(sizes[i]):
            store = ""

            for y in range(len(lines)):
                value = lines[y][sum(sizes[:i]) + j]
                if value.isnumeric():
                    store += value

            if isAddition and store.isnumeric():
                total += int(store)
            elif not isAddition and store.isnumeric():
                if total == 0:
                    total = int(store)
                else:
                    total *= int(store)

        count += total

    print(f"COUNT: {count}")


main()