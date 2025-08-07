# NumPy assignment
import numpy as np
#Part 1: Create NumPy arrays
#Task 1:
array1 = np.arange (0, 21, 2)
identity_matrix = np.identity(3)
ones = np.ones((4, 4))
spaced_array = np.linspace(5, 50, 10)
#Task 2:
list_to_array = np.array([10, 20, 30, 40, 50])
rand_array = np.random.rand(3, 3)
randn_array = np.random.randn(3, 3)
randint_array = np.random.randint(1 , 100 ,(3, 3))
#Task 3:
print(f"Random normal array shape is : {randn_array.shape}")
print(f"\nRandom normal array size is : {rand_array.size}")
print(f"\nRandom normal array data type is : {randint_array.dtype}")
#Part 2: Indexing and Selection
#Task 1:
task1_array=np.array([5, 10, 15, 20, 25, 30])
print(f"\nFirst element is : {task1_array[0]}\nlast three elements are : {task1_array[-3:]}\nelements from index 1 to 4 are : {task1_array[1:5]}")
#Task 2:
task2_matix = np.arange(1, 10).reshape(3, 3)
second_row = task2_matix[1, :]
first_two_colomns = task2_matix[:, :2]
two_by_two_matrix = task2_matix[:2, :2]
#Task 3:
task3_matrix = np.arange(2,20,2).reshape(3,3)
task3_matrix += 10
task3_matrix [: , :1]*=2
#Task 4:
task4_array = np.arange(0, 30, 3)
shallow_copy = task4_array.view() 
""" The shallow copy is a view of the data and it still point to the original data , 
    if the shallow copy changed the original will change."""
deep_copy = task4_array.copy()
""" The deep copy is new array that have same elements of copied array"""
#Task 5:
arr = np.arange(10, 101, 10)
selected_indices = [0,3,5]
arr[selected_indices]
#Part 3:
#Task 1:
math_array = np.array([3, 7, 2, 9, 12, 5, 10])
print(f"\nArray is : {math_array}\nThe maximum element in the array is : {math_array.max()}, its index is {math_array.argmax()}.\nThe minimum element in the array is : {math_array.min()}, its index is {math_array.argmin()}.")
#Task 2:
given_arr = np.array([1, 2, 3, 4, 5])
print(f"\nThe square roots of the array elements are : {np.sqrt(given_arr)}\nThe exponential of the array elements are : {np.exp(given_arr)}\nThe sine of the array elements are : {np.sin(given_arr)}\nThe Logarithm of the array elements are : {np.log(given_arr)}")
