# 1. Import the numpy package under the name `np`
import numpy as np

##### DECLARING NUMPY ARRAYS #####

# 2. Use np.array(<list>) to convert the list below into a numpy array. The array should be saved in a variable. Then print both the list and the array.
a = [300, -200, 100, 0, -100, 200, -300]
np.array(a)
print(a)
print(np.array(a))
print("\n")

## The array method in numpy has an optional dtype argument which specifies the datatype each element should be. For the array above, it could be implemented using A = np.array(a, dtype=str) ##

# 3. Declare new arrays with different datatypes using the list from #2. Datatypes to use: str, float, np.int32, np.int8, np.uint32, up.uint8.
stringarray = np.array(a, dtype=str)
floatarray = np.array(a, dtype=float)
int32array = np.array(a, dtype=np.int32)
int8array = np.array(a, dtype=np.int8)
uint32array = np.array(a, dtype=np.uint32)
uint8array = np.array(a, dtype=np.uint8)
print(stringarray)
print(floatarray)
print(int32array)
print(int8array)
print(uint32array)
print(uint8array)
print("\n")


# 4. Use np.zeros(<int>) to create a array of zeroes of size 10. This should be saved in a variable. Then print the array.
arrzeros = np.zeros(10)
print(arrzeros)
print("\n")
# 5. In your array of zeroes, change the fifth 0 to a 6. (remember how indexing works in lists?) Print the array.
arrzeros[4]=6
print(arrzeros)

# 6. Use np.arange(<int>, <int>) to create an array with values ranging from 11 to 46. Print the array.
arrarange = np.arange(11, 47)
print(arrarange)


# 7. Reverse the array you created in #6. Print the array.
reverse6 = arrarange[::-1]
print(reverse6)
print("\n")



# 8. Use <array>.reshape(<int>, <int>) to turn your array from #6 into a multidimensional 6x6 array. Print the array.
print(reverse6.reshape(6, 6))
print("\n")


# 9. Use np.random.random((<int>, <int>)) to create a 10x10 array with random values. Print the array.
arrrandom10 = np.random.random((10, 10))
print(arrrandom10)
print("\n")


# 10. Use np.random.randint(<int>, <int>, size=(<int>, <int>)) to create a 3x3 array with random integers. Print the array.
arrrandom3=np.random.randint(100, size=(3, 3)) 
print(arrrandom3)
print("\n")


# 11. Use <array>.max() and <array>.min to identify the maximums and minimums of the arrays you created in #9 and #10. Print the results.
max9 = arrrandom10.max()
min9 = arrrandom10.min()
max10 = arrrandom3.max()
min10 = arrrandom3.min()
print("the max value of the array created in 9 is: ")
print(max9)
print("the min value of the array created in 9 is: ")
print(min9)
print("the max value of the array created in 10 is: ")
print(max10)
print("the min value of the array created in 10 is: ")
print(min10)
print("\n")


# 12. Use <array>.mean() to find the means of the two arrays you created in #9 and #10. Print the results.
mean9 = arrrandom10.mean()
mean10 = arrrandom3.mean()
print("the mean value of the array created in 9 is:")
print(mean9)
print("the mean value of the array created in 10 is:")
print(mean10)
print("\n")


# 13. Convert the following two lists into 2X3 arrays. (You will need to use np.array and .reshape)

a = [2, 3, 5, 7, 11, 13]
b = [3, 1, 4, 1, 5, 9]

arraya = np.array(a)
arrayb = np.array(b)
arrayashaped = arraya.reshape((2, 3))
arraybshaped = arrayb.reshape((2, 3))
print(arrayashaped)
print(arraybshaped)
print("\n")

# 14. Add the two arrays from #13 (<array> + <array>)
addedarrays = (arrayashaped + arraybshaped)
print(addedarrays)
print("\n")

# 15. Multiply both arrays from #13 by 10.
multiplieda = 10*arrayashaped
multipliedb = 10*arraybshaped
print(multiplieda)
print(multipliedb)