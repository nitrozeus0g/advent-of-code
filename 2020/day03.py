import numpy as np

def main(data):
	ret = [0,0,0,0,0]
	slope1 = 1
	slope3 = 3
	slope5 = 5
	slope7 = 7
	down2 = 1
	count = 1
	for e, i in enumerate(data):
		if e == 0: continue
		i = i * count
		if i[slope1] == '#':
			ret[0] += 1
		if i[slope3] == '#':
			ret[1] += 1
		if i[slope5] == '#':
			ret[2] += 1
		if i[slope7] == '#':
			ret[3] += 1
		if e % 2 == 0:
			if i[down2] == '#':
				ret[4] += 1
			down2 += 1
		count += 1
		slope1 += 1
		slope3 += 3
		slope5 += 5
		slope7 += 7

	ret = [i for i in ret if i != 0]
	return np.prod(ret)
	#return ret

if __name__ == "__main__":
	#with open('sample.input') as f:
	with open('inputs/day03.input') as f:
		data = [str(line) for line in f.read().splitlines()]
		print(main(data))
