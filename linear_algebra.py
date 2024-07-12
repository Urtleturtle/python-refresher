import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Create matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Addition of vectors
sum_vector = a + b
print(f"Prob 1: \nSum of vectors a and b: {sum_vector}")

# Subtraction of vectors
diff_vector = a - b
print(f"Difference of vectors a and b: {diff_vector}\n")

sum_vector = A + B
print(f"Prob 2: \nSum of vectors a and b: {sum_vector}")

# Subtraction of vectors
diff_vector = A - B
print(f"Difference of vectors a and b: {diff_vector}\n")

print(f"Prob 3: \n Dot of vectors a and b: {np.dot(a,b)}\n")\

a = np.array([[1, 2, 3], [4,5,6]])
b = np.array([[7,8,9,10],[11,12,13,14],[15,16,17,18]])

print(f"Prob 4: \n Dot of vectors a and b: {np.dot(a,b)}\n")

a = np.array([1,1,2])
print(f"Prob 5: \n Magntitude = {np.sqrt(a.dot(a))}\n")

a = np.array([[1,2],[3,4]])
print(f"Prob 6\n tranpose is {np.transpose(a)}\n")