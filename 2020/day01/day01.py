from itertools import permutations as p

def main(data):
	pairs = p(data, 3)
	for i in pairs:
		if sum(i) == 2020:
			return i[0] * i[1] * i[2]

if __name__ == "__main__":
	#with open('../sample.input') as f:
	with open('../inputs/day01.input') as f:
		data = [int(line) for line in f.read().splitlines()]
		print(main(data))
