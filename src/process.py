def process(words: list[str]):
	connections = [[0 for i in range(len(words))] for i in range(len(words))]

	for indexa, a in enumerate(words):
		for indexb, b in enumerate(words):
			if a == b:
				continue
			elif a[-1] == b[0]:
				connections[indexa][indexb] = 1

	picked = []

	while len(picked) < len(connections):
		temp = len(picked)

		picked = pick(connections, picked)

		if len(picked) == temp:
			break

	word = words[picked[0]]

	for i in picked[1:]:
		word += words[i][1:]

	return word


def pick(connections: list[list[int]], picked: list[int]):
	pick = None

	if picked == []:
		for i, start in enumerate(connections):
			if i in picked:
				continue

			count = 0
			for j, end in enumerate(start):
				if j in picked:
					continue
				count += end

			if count >= 1 and (pick == None or count < pick[1]):
				pick = (i, count)
	else:
		for i, end in enumerate(connections[picked[-1]]):
			if i in picked:
				continue

			if end >= 1 and (pick == None or end < pick[1]):
				pick = (i, end)

	if pick != None:
		picked.append(pick[0])

	return picked
