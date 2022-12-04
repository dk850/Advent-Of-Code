f = open("input", "r")
input = f.read().splitlines()
input = [x.split(',') for x in input ]  # split input on , to separate it easier

count=0
for line in input:
	range0=range(int(line[0].split('-')[0]),int(line[0].split('-')[1])+1)
	range1=range(int(line[1].split('-')[0]),int(line[1].split('-')[1])+1)

	bigRange=-1
	if len(range0) > len(range1):
		bigRange=range0
		smallRange=range1
	else:
		bigRange=range1
		smallRange=range0

	if smallRange.start in bigRange or smallRange[-1] in bigRange:  # note now OR
		count += 1

print(count)
