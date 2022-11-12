import numpy as np

from partial_pivot import partial_pivot
from elemental_operations import row_eo

def factorization_lu(A):
  n = len(A)
  P = np.eye(n)
  L = np.eye(n)
  Log,U = partial_pivot(A)
  for R in Log:
  	if R[1] == 'Rij':
  		data = R[0]
  		row_eo(data,P,mode='Rij')
  for R in reversed(Log):
  	if R[1] == 'kRij':
  		data = R[0]
  		data[2] = (-1)*data[2]
  		row_eo(data,L,mode='kRij')
  return P,L,U

def main():
  A = np.array([[2,1,2],
                [0,1,2],
                [2,1,0]])
  P,L,U = factorization_lu(A)
  if not np.array_equal(P,np.eye(len(A))):
  	print('Matrix P\n',P)
  print('Matrix A\n',A)
  print('Matrix L\n',L)
  print('Matrix U\n',U)
  
if __name__ == '__main__':
  main() 