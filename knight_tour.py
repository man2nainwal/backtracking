from __future__ import print_function

square = 8

def valid_move (x, y, box):
  return (x >= 0 and x < square and y >= 0 and y < square and box[x][y] == -1)

def print_box(box):
  for i in range(square):
    for j in range(square):
      print(box[i][j],)
    print()
    

