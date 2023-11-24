def main(data):
  required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
  required_fields = sorted(required_fields)
  correct = 0

if __name__ == "__main__":
	with open('sample.input') as f:
	#with open('inputs/day04.input') as f:
		data = [str(line) for line in f.read().splitlines()]
		print(main(data))
