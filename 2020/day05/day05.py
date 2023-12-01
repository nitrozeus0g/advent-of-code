def main(data):
  lo = 0
  hi = 127
  clo = 0
  chi = 7
  for i in data: # F=lower, B=upper, L=lower, R=upper
    print(data[-1])
    break
    if i == 'F': hi = (lo+hi)//2
    if i == 'B': lo = (lo+hi)//2+1
    if i == 'L': chi = (clo+chi)//2
    if i == 'R': clo = (clo+chi)//2+1

if __name__ == "__main__":
  with open('sample.input') as f:
  #with open('inputs/day0x.input') as f:
    data = [line for line in f.read().splitlines()]
    for i in data:
      print(main(i))

