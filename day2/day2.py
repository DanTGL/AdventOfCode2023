import re

def part1(games):
    pattern = re.compile(r'(\d+) (red|blue|green)')

    result = 0

    for idx, game in enumerate(games, 1):
        valid = True
        for match in re.finditer(pattern, game):
            count, color = int(match.group(1)), match.group(2)

            if not ((color == 'red' and count <= 12) or (color == 'green' and count <= 13) or (color == 'blue' and count <= 14)):
                valid = False
                break
        
        if valid:
            result += idx

    
    return result

def part2(games):
    pattern = re.compile(r'(\d+) (red|blue|green)')

    result = 0

    for idx, game in enumerate(games, 1):
        min_red, min_blue, min_green = 0, 0, 0

        for match in re.finditer(pattern, game):
            count, color = int(match.group(1)), match.group(2)

            match color:
                case 'red':
                    min_red = max(min_red, count)
                
                case 'blue':
                    min_blue = max(min_blue, count)
                
                case 'green':
                    min_green = max(min_green, count)

        result += min_red * min_blue * min_green

    return result


if __name__ == '__main__':
    with open('day2/input') as f:
        user_input = f.readlines()
    
    print(part2(user_input))