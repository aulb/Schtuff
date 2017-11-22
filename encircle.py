NORTH = 0
EAST  = 1
SOUTH = 2
WEST  = 3
def encircle(commands):
	result = [False] * len(commands)
	
	for index, command in enumerate(commands):
		direction = NORTH
		x, y = 0, 0
		for i in range(4):
			for command_string in command:
				if command_string == 'L':
					direction = (direction - 1) % 4
				elif command_string == 'R':
					direction = (direction + 1) % 4
				else:
					if direction == NORTH:
						y += 1
					elif direction == EAST:
						x += 1
					elif direction == SOUTH:
						y -= 1
					else:
						x -= 1
			if x == 0 and y == 0: 
				result[index] = True
				break

	return result


if __name__ == '__main__':
	commands = ['GLGGLG', 'GGGG', 'GGRRRRGG']
	print(encircle(commands))
