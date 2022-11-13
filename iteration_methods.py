import numpy as np

def jacobi(A,b,x_0,i):
	# A = U+L+D
	D = np.diag(np.diag(A))
	D_inv = np.linalg.inv(D)
	U = np.triu(A)-D
	L = np.tril(A)-D
	iteration = 0
	x_k = x_0
	# x^k+1 = D'b-D'(L+U)x^k
	while iteration < i:
		Rx = np.dot(L+U,x_k) 
		x_k = np.dot(D_inv,b)-np.dot(D_inv,Rx)
		iteration += 1 
	print(x_k)

def gauss_seidel(A,x0,i):
	pass

def attached_conjugate(A,x0,i):
	pass

def main():
	# jacobi iteration method 
	A = np.array([[2,0,-1],
                [-2,-10,0],
                [-1,-1,4]])
	b = np.array([[1],
                [-12],
                [2]])
	x_0 = np.array([[0],
                [0],
                [0]])
	jacobi(A,b,x_0,2)
  

if __name__ == '__main__':
 	main() 