
def genbord(x, y):

  print("|",end="")
  for i in range(x):
    print("----", end="")
  print("|")
  for i in range(y):
    print("| ", end="")
    for j in range(x):

      print("   |",end="")
    print("\n|",end="")
    for j in range(x):
      print("----",end="")
    print("|\n",end="")

class bordgen:

  def __init__(self, dim):
    self.xmax = dim[0]
    self.ymax = dim[1]


genbord(5,5)

