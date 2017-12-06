def count(coins, n):
	# Check for impossibility
	table = [[0 for column in range(len(coins))] for row in range(n + 1)]

	for column in range(len(coins)): table[0][column] = 1

	for row in range(1, n + 1):
		for column, coin in enumerate(coins):
			x = table[row - coin][column] if row - coin >= 0 else 0

			y = table[row][column - 1] if column >= 1 else 0

			table[row][column] = x + y

		for t in table:
			print(t)
		print()

	return table[row][column]

def space_efficient_count(coins, n):
	table = [0 for column in range(n + 1)]
	table[0] = 1

	for coin in coins:
		for i in range(coin, n + 1):
			table[i] += table[i - coin] # table[i - coin] will exist atleast 0

		# print(table)	

	return table[n]


if __name__ == '__main__':
	# We know how many different ways can you make 5 with coins 1 and 2
	# Now introduce 3, 5 - 3 => 2 how many different ways can you make 2 with 3 coins?
	print(count([1,2,3], 5))
	print(space_efficient_count([1,2,3],5))
