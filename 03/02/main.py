def readLines(fileName):
    array = []
    with open(fileName, 'r') as file:
        for line in file:
            array.append(line.strip())
    return array


def makeLargestTwelve(bank):
    k = len(bank) - 12
    stack = []

    for digit in bank:
        while k > 0 and stack and stack[-1] < digit:
            stack.pop()
            k -= 1
        stack.append(digit)

    if k > 0:
        stack = stack[:-k]

    return "".join(stack[:12])


def main():
    input_data = readLines('../input.txt')
    count = 0

    for bank in input_data:
        result = makeLargestTwelve(bank)
        count += int(result)
        print(result)

    print(f"COUNT: {count}")


main()