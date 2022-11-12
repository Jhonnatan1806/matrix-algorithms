import numpy as np

def row_eo(data,A,mode):
  # data[0] = i
  # data[1] = j
  # swap rows i with j
  if len(data)==2 and mode == 'Rij':
    aux = np.copy(A[data[0]])
    A[data[0]] = A[data[1]]
    A[data[1]] = aux
  # data[0] = i
  # data[1] = k
  # multiply row i by k
  elif len(data)==2 and  mode == 'kRi':
    A[data[0]] = A[data[0]]*data[1]
  # data[0] = i
  # data[1] = j
  # data[2] = k
  # add row j multiplied by k times row i
  elif len(data)==3 and mode == 'kRij':
    A[data[0]] += A[data[1]]*data[2]
  return data, mode

def main():
  A = np.array([[1,2,3],
                [4,5,6],
                [7,8,9]])
  print('Matrix A\n',A)
  # mode Rij
  row_eo([0,1],A,mode='RijA')
  print('Elemental Operation R01A\n',A)
  # mode kRi
  row_eo([0,2],A,mode='kRi')
  print('Elemental Operation 2*R0A\n',A)
  # mode kRij
  row_eo([1,2,2],A,mode='kRij')
  print('Elemental Operation 2*R12A\n',A)

if __name__ == '__main__':
  main() 