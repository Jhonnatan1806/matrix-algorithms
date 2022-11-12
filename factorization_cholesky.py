import numpy as np

def factorization_cholesky(A):
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
  A = np.array([[4,0,1],
                [0,4,1],
                [1,1,4]])
  L = factorization_cholesky(A)
  print('Matrix A\n',A)
  print('Matrix L\n',L)
  print('Matrix L.L^t\n',np.dot(L,np.transpose(L)))
  
if __name__ == '__main__':
  main() 