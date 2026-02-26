def readLines(fileName):
    array = []
    
    with open(fileName, 'r') as file:
        for line in file:
            array.append(line.strip())

    return array

def findIndex(array):
    best_first = 0
    best_second = 1
    best_value = 10 * array[0] + array[1]
    
    for i in range(len(array) - 1):
        max_after_idx = i + 1
        for j in range(i + 2, len(array)):
            if array[j] > array[max_after_idx]:
                max_after_idx = j
        
        value = 10 * array[i] + array[max_after_idx]
        if value > best_value:
            best_value = value
            best_first = i
            best_second = max_after_idx
    
    return [best_first, best_second]

def main():
    input = readLines('../input.txt')

    count = 0

    for bank in input:
        index = findIndex([int(numeric_string) for numeric_string in bank])
        count += 10 * int(bank[index[0]]) + int(bank[index[1]])
    
    print(f"COUNT: {count}")

main()