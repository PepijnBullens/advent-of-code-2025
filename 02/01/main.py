def readLine(fileName):
    with open(fileName, 'r') as file:
        content = file.read().strip()
        return content

def hasRepeatingPattern(n):
    s = str(n)
    length = len(s)

    if length % 2 != 0:
        return False

    half = length // 2
    return s[:half] == s[half:]

def main():
    input = readLine('../input.txt')
    rangesArray = input.split(",")

    count = 0

    for rangeArray in rangesArray:
        split = rangeArray.split("-")
        start = int(split[0])
        end = int(split[1])

        for i in range(end - start + 1):
            if hasRepeatingPattern(start + i):
                count += start + i

    print(f"COUNT: {count}")



main()