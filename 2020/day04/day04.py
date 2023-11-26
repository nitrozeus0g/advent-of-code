def main(data):
  required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
  required_fields2= ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
  required_fields = sorted(required_fields)
  required_fields2= sorted(required_fields2)
  correct = 0

  fields = []
  for i in data:
    if len(i) > 0:
      for j in i.split(" "):
        fields.append(j.split(":")[0])
    else:
      print(sorted(fields))
      if sorted(fields) == required_fields or sorted(fields) == required_fields2:
        correct += 1
      fields = []
  return correct

if __name__ == "__main__":
	#with open('sample.input') as f:
	with open('inputs/day04.input', 'r') as f:
		data = [str(line) for line in f.read().splitlines()]
		print(main(data))
