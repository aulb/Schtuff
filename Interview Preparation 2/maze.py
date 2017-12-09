Implement a function to generate a maze.

from random import randint
import enum
class Condition(enum):
	CLEAR = 0
	RIGHT = 1
	BOTTOM = 2

class Direction(enum):
	RIGHT = 0
	LEFT = 1
	UP = 2
	DOWN = 3

# Create maze from top left to bottom right
def generate_maze(row, col):
	if row < 0 or col < 0: return []
	
	# create a fresh matrix of all zeroes
	maze = [[0 for _ in range(col)] for _ in range(row)]
	
def get_direction(condition=Condition.CLEAR):
direction = randint(1, 10)
if 1 <= direction <= 4: 
if Condition.CLEAR: return Direction.RIGHT
elif Condition.RIGHT: return Direction.DOWN
else: return Direction.RIGHT
elif 5 <= direction <= 8: 
if Condition.CLEAR: return Direction.DOWN
elif Condition.RIGHT: return Direction.DOWN
else: return Direction.RIGHT
elif direction == 9: 
if Condition.CLEAR: return Direction.LEFT
elif Condition.RIGHT: return Direction.DOWN
else: return Direction.UP
else: 
if Condition.CLEAR: return Direction.UP
elif Condition.RIGHT: return Direction.DOWN
else: return Direction.RIGHT

def create_key(cell):
	return ‘{},{}’.format(cell[0], cell[1])

def create_path(maze):
	# [[i, j]]
path = {‘0,0’: True}
visited_rows = [0 for _ in range(len(maze))]

# randomly pick direction
	current_cell = [0, 0]
	condition = Condition.CLEAR
	while current_cell != [len(maze) - 1, len(maze[0]) - 1]:
new_direction = get_direction(condition)
if new_direction == Direction.RIGHT:
	# check if we can go right
	if current_cell[1] + 1 <= len(maze[0]) - 1:
	current_cell[1] += 1
	path.append(current_cell[:])
if new_direction == Direction.LEFT:
	# check if we can go right
	if current_cell[1] - 1 >= 0:
	current_cell[1] -= 1
	path.append(current_cell[:])
if new_direction == Direction.UP:
	# check if we can go right
	if current_cell[0] - 1 >= 0:
	current_cell[0] -= 1
	path.append(current_cell[:])
if new_direction == Direction.DOWN:
	# check if we can go right
	if current_cell[0] + 1 <= len(maze) - 1:
	current_cell[0] += 1
	path.append(current_cell[:])

	
	
	return path
	

def draw_wall(maze, path):
	pass
