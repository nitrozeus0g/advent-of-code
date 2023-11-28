import re

def main(data):
  required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
  required_fields = sorted(required_fields)
  eye_color = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
  correct = 0

  fields = []
  for i in data:
    if len(i) > 0:
      for j in i.split(" "):
        tmp = j.split(":")

        if tmp[0] == 'byr':
          if len(tmp[1]) != 4 or tmp[1].isnumeric() == False: continue
          if int(tmp[1]) < 1920 or int(tmp[1]) > 2002: continue

        if tmp[0] == 'iyr':
          if len(tmp[1]) != 4 or tmp[1].isnumeric() == False: continue
          if int(tmp[1]) < 2010 or int(tmp[1]) > 2020: continue

        if tmp[0] == 'eyr':
          if int(tmp[1]) < 2020 or int(tmp[1]) > 2030: continue

        # WRONGGGGG maybe idk #########
        if tmp[0] == 'hcl':
          #print(tmp)
          if tmp[1][0] != '#' or len(tmp[1]) != 7 or tmp[1][1:].isnumeric() == False: continue
          if tmp[1][1:]:
            if not re.match(r'[a-f0-9]{6}', tmp[1][1:]): continue
          print(re.match(r'[a-f0-9]{6}', tmp[1][1:]))

        if tmp[0] == 'hgt':
          height = tmp[1][:-2]
          metric = tmp[1][-2:]
          if metric == 'cm':
            if int(height) < 150 or int(height) > 193: continue
          if metric == 'in':
            if int(height) < 59 or int(height) > 76: continue

        if tmp[0] == 'ecl':
          if tmp[1] not in eye_color: continue

        if tmp[0] == 'pid':
          if len(tmp[1]) != 9 or tmp[1].isnumeric() == False or int(tmp[1]) <= 0: continue

        if tmp[0] == 'cid': continue

        else:
          fields.append(j.split(":")[0])

    else:
      #print(sorted(fields))
      if sorted(fields) == required_fields:
        correct += 1
      fields = []
  return correct

if __name__ == "__main__":
  #with open('sample.input') as f:
  with open('inputs/day04.input', 'r') as f:
    data = [str(line) for line in f.read().splitlines()]
    print(main(data))
