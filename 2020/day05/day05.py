def main(data):

if __name__ == "__main__":
	with open('sample.input') as f:
	#with open('inputs/day0x.input') as f:
		data = [str(line) for line in f.read().splitlines()]
		print(main(data))

