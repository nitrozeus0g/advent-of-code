def main(data):
	ret = 0
	for full in data:
		full = full.split(' ')
		policy_range = full[0].split('-')
		policy_letter = full[1][0]
		password = full[2]
		#check = password.count(policy_letter)
		if password[int(policy_range[0])-1] == policy_letter and password[int(policy_range[1])-1] != policy_letter:
			ret += 1
		elif password[int(policy_range[0])-1] != policy_letter and password[int(policy_range[1])-1] == policy_letter:
			ret += 1
	return ret

if __name__ == "__main__":
	#with open('../sample.input') as f:
	with open('../inputs/day02.input') as f:
		data = [str(line) for line in f.read().splitlines()]
		print(main(data))

