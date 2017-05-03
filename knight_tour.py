from __future__ import print_function

square = 8
filled = 0
moveX = [-2, -2, 2, 2, -1, 1, -1, 1]
moveY = [-1, 1, -1, 1, -2, -2, 2, 2]

def set_filed():
	filled += 1
	return filled-1

def remove_filled():
	filled -=1
	return -1

def valid_move (x, y, box):
  return (x >= 0 and x < square and y >= 0 and y < square and box[x][y] == -1)

def print_box(box):
  for i in range(square):
    for j in range(square):
      print(box[i][j],)
    print()

def solve_util(x, y, box):
	if filled == square*square:
		return True
	for i in range(8):
		if valid_move(x+moveX[i], y+moveY[i], box):
			box[x+moveX[i]][y+moveY[i]] = set_filled()
			if (solve_util(x+moveX[i], y+moveY[i], box)):
				return True
			else :
				box[x+moveX[i]][y+moveY[i]] = remove_filled()
			
def solve(box):
	box[0][0] = set_filled()
	if(solve_util(0, 0, box)):
		print_box(box)
		return True
	print("No Solution Exist!!")
	return False

def main():
	box = [[-1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1]]
	solve(box)
	return True
