import numpy as np

from elemental_operations import row_eo

# Partial Pivot
def partial_pivot(A):
  U = np.copy(A).astype('float64')
  Log = []
  n = len(U)
  for j in range(n):
    # find maxC for row
    p = j
    maxC = abs(U[p,p])
    for i in range(j+1,n):
      if abs(U[i,j])>maxC:
        maxC = abs(U[i,j])
        p = i
    # elemental operation Rij
    Log.append(row_eo([j,p],U,mode='Rij'))
    # elemental operation (-m)*Rij
    for i in range(j+1,n):
      m = U[i,j]/U[j,j]
      Log.append(row_eo([i,j,-m],U,mode='kRij'))
  return Log, U

def main():
  A = np.array([[2,1,2],
                [0,1,2],
                [2,1,0]])
  print('Matrix A\n',A)
  Log,U = partial_pivot(A)
  print('Matrix U\n',U)
  print('Log elemental operations\n',Log)

if __name__ == '__main__':
  main() 
