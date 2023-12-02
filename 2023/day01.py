def part1(data):
  ret = 0
  for i in data:
    x = [x for x in i if x.isnumeric() == True]
    y = str(x[0]) + str(x[-1])
    y = int(y)
    ret += y
  return ret

def part2(data):
  ret = 0
  for i in data:
    nums = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
        }
  return ret

if __name__ == "__main__":
  with open("sample.input", "r") as f:
  #with open("inputs/day01.input", "r") as f:
    data = [str(line) for line in f.read().splitlines()]
    #print(part1(data))
    print(part2(data))
