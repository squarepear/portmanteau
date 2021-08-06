import os, random

def process(words: list[str], createCSV = False):
	connections = [[0 for i in range(len(words))] for i in range(len(words))]

	csv = open("log.csv", "w") if createCSV else None

	if createCSV:
		csv.write(f"words,{','.join(words)}")

	for indexa, a in enumerate(words):
		if createCSV:
			csv.write(f"\n{a},")

		for indexb, b in enumerate(words):
			if a == b:
				if createCSV:
					csv.write(",")
				continue

			match = 0

			size = (len(a) if len(a) <= len(b) else len(b))
			for i in range(size - 1, 0, -1):
				if a[-i:] == b[:i]:
					# print(f"{a[-i:]} == {b[:i]} -- {words[indexa]} {words[indexb]} {i}")
					connections[indexa][indexb] = i
					match = i
					break
			
			if createCSV:
				csv.write(f"{match},")
	

	if createCSV:
		csv.close()

	picked = []
	sizes = []

	while len(picked) < len(connections):
		temp = len(picked)

		picked, size = pick(connections, picked)

		if len(picked) == temp:
			break

		sizes.append(size)

	word = words[picked[0]]

	for i in range(1, len(picked)):
		# print(f"{words[picked[i-1]]} {words[picked[i]]} {sizes[i]}")
		word += words[picked[i]][sizes[i]:]

	return word


def pick(connections: list[list[int]], picked: list[int]):
	size = 0
	picks = []

	if picked == []:
		for i, start in enumerate(connections):
			if i in picked:
				continue

			count = 0
			for j, end in enumerate(start):
				if j in picked:
					continue
				count += end

			if count >= 1 and (picks == [] or count < size):
				picks = [[i, end]]
				size = count
	else:
		for i, end in enumerate(connections[picked[-1]]):
			if i in picked:
				continue

			if end >= 1 and end >= size:
				if end > size:
					picks = [[i, end]]
					size = end
				else:
					picks.append([i, end])


	if picks != []:
		pick = random.choice(picks)

		picked.append(pick[0])

		return picked, pick[1]
	
	return picked, 0
