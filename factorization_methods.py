import numpy as np

from partial_pivot import partial_pivot
from elemental_operations import row_eo

def palu(A):
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

def cholesky(A):
  n = len(A)
  L = np.zeros((n, n),float)
  for j in range(n):
    # summation \sum_{k=0}^{j} l_{j,k}^2
    summation = 0
    for k in range(j):
      summation += pow(L[j,k],2)
    # where l_{j,j} = \sqrt{a_{j,j}-\sum_{k=0}^{j} l_{j,k}^2}
    L[j,j] = np.sqrt(A[j,j]-summation)
    for i in range(j+1,n):
      # summation \sum_{k=0}^{j} l_{i,k}*l_{j,k}
      summation=0
      for k in range(j):
        summation += L[i,k]*L[j,k]
    # where l_{i,j} = \fracc{{a_{i,j}-\sum_{k=0}^{j} l_{i,k}*l_{j,k}}{l_{j,j}}
      L[i,j] = (A[i,j]-summation)/L[j,j]
  return L

def main():
  # PA = LU factorization
  A = np.array([[2,1,2],
                [0,1,2],
                [2,1,0]])
  P,L,U = palu(A)
  if not np.array_equal(P,np.eye(len(A))):
    print('Matrix P\n',P)
  print('Matrix A\n',A)
  print('Matrix L\n',L)
  print('Matrix U\n',U)
  # cholesky factorization
  A = np.array([[4,0,1],
                [0,4,1],
                [1,1,4]])
  L = cholesky(A)
  print('Matrix A\n',A)
  print('Matrix L\n',L)
  print('Matrix L.L^t\n',np.dot(L,np.transpose(L)))
  
  
if __name__ == '__main__':
  main() 