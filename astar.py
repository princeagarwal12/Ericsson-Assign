import pygame
import math
from queue import PriorityQueue

## Declaring the parameters 
WIDTH = 700
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("A* Path Finding Algorithm")

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165 ,0)
GREY = (128, 128, 128)
BLUE = (64, 224, 208)

## The Spot class represents a Spot/Node point on grid 
class Spot:
	def __init__(self, row, col, width, total_rows):
		self.row = row
		self.col = col
		self.x = row * width
		self.y = col * width
		self.color = WHITE
		self.neighbors = []
		self.width = width
		self.total_rows = total_rows

	## Function to get the position of any spot/node
	def get_pos(self):
		return self.row, self.col

	## Functions to check any particular spot/node type
	def is_closed(self):
		return self.color == RED

	def is_open(self):
		return self.color == YELLOW

	def is_barrier(self):
		return self.color == BLACK

	def is_start(self):
		return self.color == ORANGE

	def is_end(self):
		return self.color == BLUE

	def is_tree(self):
		return self.color == GREEN 

	def reset(self):
		self.color = WHITE

	## Functions to change the type/color of spots/nodes 
	def make_start(self):
		self.color = ORANGE

	def make_closed(self):
		self.color = RED

	def make_open(self):
		self.color = YELLOW

	def make_barrier(self):
		self.color = BLACK

	def make_tree(self):
		self.color = GREEN

	def make_end(self):
		self.color = BLUE

	def make_path(self):
		self.color = PURPLE

	## Function to create the Window for GUI
	def draw(self, win):
		pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

	## Function to find the neighbors of any spot/node 
	def update_neighbors(self, grid):
		self.neighbors = []

		if self.row > 0 and not grid[self.row - 1][self.col].is_barrier(): ## UP
			self.neighbors.append(grid[self.row - 1][self.col])

		if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier(): ## DOWN
			self.neighbors.append(grid[self.row + 1][self.col])

		if self.col > 0 and not grid[self.row][self.col - 1].is_barrier(): ## LEFT
			self.neighbors.append(grid[self.row][self.col - 1])

		if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_barrier(): ## RIGHT
			self.neighbors.append(grid[self.row][self.col + 1])

	def __lt__(self, other):
		return False

## Function to find the H_score based on Manhattan distance
def h(p1, p2):
	x1, y1 = p1
	x2, y2 = p2
	return abs(x1 - x2) + abs(y1 - y2)

## Function to make the path
def reconstruct_path(came_from, current, draw):
	while current in came_from:
		current = came_from[current]
		print(current.get_pos(), sep=",")
		#if current.is_tree():
		#	print("tree")
		#else:
		current.make_path()
		draw()

## Function for the main A* algo considering the tree nodes as well
def algorithm(draw, grid, start, end):
	count = 0
	open_set = PriorityQueue()
	open_set.put((0, count, start))
	came_from = {} ## to capture the last spot/node of every other spot/node

	## To initialise G_scores of all spots with infinity except start node
	g_score = {spot: float("inf") for row in grid for spot in row}
	g_score[start] = 0
	
	## To initialise T_score (Tree weightage) of all tree spots/nodes 
	t_score = {}
	for row in grid:
		for spot in row:
			if spot.color == GREEN:
				t_score[spot] = -1
			else:
				t_score[spot] = 0

	## --------------------------------------------------------------------
	## To calculate the F_Score for all spots using: [F = G + H + T]
	## --------------------------------------------------------------------
	f_score = {spot: float("inf") for row in grid for spot in row}
	f_score[start] = h(start.get_pos(), end.get_pos())

	open_set_hash = {start}

	## Keep iterating till open set is NULL
	while not open_set.empty():
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()

		current = open_set.get()[2]
		open_set_hash.remove(current)

		if current == end:
			reconstruct_path(came_from, end, draw)
			end.make_end()
			return True

		for neighbor in current.neighbors:
			## consider g-score and t-score together for neighbor spot to find optimised path
			temp_g_score = g_score[current] + 1 + t_score[current]   

			if temp_g_score < g_score[neighbor]:
				came_from[neighbor] = current
				g_score[neighbor] = temp_g_score + t_score[neighbor]
				f_score[neighbor] = temp_g_score + h(neighbor.get_pos(), end.get_pos())
				if neighbor not in open_set_hash:
					count += 1
					open_set.put((f_score[neighbor], count, neighbor))
					open_set_hash.add(neighbor)
					neighbor.make_open()

		draw()

		if current != start:
			current.make_closed()

	return False

## Function to make the grids
def make_grid(rows, width):
	grid = []
	gap = width // rows
	for i in range(rows):
		grid.append([])
		for j in range(rows):
			spot = Spot(i, j, gap, rows)
			grid[i].append(spot)

	return grid

## Function to create grids
def draw_grid(win, rows, width):
	gap = width // rows
	for i in range(rows):
		pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
		for j in range(rows):
			pygame.draw.line(win, GREY, (j * gap, 0), (j * gap, width))

## Function to update the window everytime 
def draw(win, grid, rows, width):
	win.fill(WHITE)

	for row in grid:
		for spot in row:
			spot.draw(win)

	draw_grid(win, rows, width)
	pygame.display.update()

## Function to get the mouse click position
def get_clicked_pos(pos, rows, width):
	gap = width // rows
	y, x = pos

	row = y // gap
	col = x // gap

	return row, col

def main(win, width):
	ROWS = 50
	grid = make_grid(ROWS, width)

	start = None
	end = None

	run = True
	while run:
		draw(win, grid, ROWS, width)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

			## When mouse left-button clicked, create a start node 
			if pygame.mouse.get_pressed()[0]: # LEFT
				pos = pygame.mouse.get_pos()
				row, col = get_clicked_pos(pos, ROWS, width)
				spot = grid[row][col]
				if not start and spot != end:
					start = spot
					start.make_start()

				elif not end and spot != start:
					end = spot
					end.make_end()

				elif spot != end and spot != start:
					spot.make_barrier()

			## When mouse right-button clicked, create a end node
			elif pygame.mouse.get_pressed()[2]: # RIGHT
				pos = pygame.mouse.get_pos()
				row, col = get_clicked_pos(pos, ROWS, width)
				spot = grid[row][col]
				spot.reset()
				if spot == start:
					start = None
				elif spot == end:
					end = None

			## When mouse middle-button clicked, create a tree node
			elif pygame.mouse.get_pressed()[1]: # MIDDLE
				pos = pygame.mouse.get_pos()
				row, col = get_clicked_pos(pos, ROWS, width)
				spot = grid[row][col]
				if spot != end and spot != start:
					spot.make_tree()

			## When Spacebar pressed, start the algorithm and when C pressed, clear the grid
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE and start and end:
					for row in grid:
						for spot in row:
							spot.update_neighbors(grid)

					algorithm(lambda: draw(win, grid, ROWS, width), grid, start, end)

				if event.key == pygame.K_c:
					start = None
					end = None
					grid = make_grid(ROWS, width)

	pygame.quit()

main(WIN, WIDTH)