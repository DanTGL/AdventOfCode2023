import regex as re

def part1(lines):
    sum = 0
    
    for line in lines:
        digits = list(filter(lambda c: c.isdigit(), line))

        first, last = digits[0], digits[-1]
        sum += int(first + last)
    
    return sum

def part2(lines):
    sum = 0
    
    numbers = [
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]

    pattern = re.compile(rf'([1-9]|{"|".join(numbers)})')
    print(pattern)

    sum = 0

    for line in lines:
        digits = list(int(digit) if digit.isdigit() else numbers.index(digit) + 1 for digit in re.findall(pattern, line, overlapped=True))

        first, last = digits[0], digits[-1]

        sum += (first * 10) + last

    return sum

if __name__ == '__main__':
    with open('day1/input') as f:
        user_input = f.readlines()
    
    print(part2(user_input))