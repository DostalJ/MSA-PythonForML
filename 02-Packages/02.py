##########
# ploting
##########
import matplotlib.pyplot as plt
# from matplotlib.style import use
# use('ggplot')

# zjednodusena syntaxe pro tvoreni listu
x = [0.1*d for d in range(10)]
y = [f(d) for d in x]

plt.plot(x, y, linewidth=5, color='b')
plt.show()

plt.scatter(x, y, marker='o', color='r', linewidths=6)
plt.show()

#######
# NumPy
#######
import numpy as np

A = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])

# transpose
A.T
A.transpose()
np.transpose(A)

np.linalg.inv(A) # inverze
np.linalg.pinv(A) # pseudoinverze
np.linalg.matrix_power(A, 2) # mocnina matice

B = np.array([[0.1,0.1,0.1],
              [0.01,0.01,0.01],
              [1,1,1]])

B*A # elementwise
np.matrix(A)*np.matrix(B) # in matric manner
np.matmul(A, B) # in matric manner

A[0,1] # indexing
