def displayPathtoPrincess(n,grid):
  princess = findPrincess(grid)
  if princess == 'top_left':
    for i in range(0,(n/2)):
      print('UP')
    for i in range(0,(n/2)):
      print('LEFT')
    
  elif princess == 'top_right':
    for i in range(0,(n/2)):
      print('UP')
    for i in range(0,(n/2)):
      print('RIGHT')

  elif princess == 'bottom_left':
    for i in range(0,(n/2)):
      print('DOWN')
    for i in range(0,(n/2)):
      print('LEFT')

  elif princess == 'bottom_right':
    for i in range(0,(n/2)):
      print('DOWN')
    for i in range(0,(n/2)):
      print('RIGHT')


def findPrincess(grid):
    possible_positions = { 'top_left':grid[0][0],
                           'top_right':grid[0][-1],
                           'bottom_left':grid[-1][0],
                           'bottom_right':grid[-1][-1]}
    return possible_positions.keys()[possible_positions.values().index('p')]

n = 3
grid = [['-','-','-'],['-','m','-'],['p','-','-']]

displayPathtoPrincess(n,grid)