#
# input_str = input("Enter a comma-separated list of elements for the tuple: ")
# elements = input_str.split(',')
# my_tuple = tuple(elements)
# reversed_tuple = my_tuple[::-1]
# print("Reversed Tuple:", reversed_tuple)
#
#
# my_tuple = (10, 15, 20, 25, 30)
# value = my_tuple[2]
# print("The value at index 2 is:", value)
#
#
# my_tuple = (50,)
# print("Type of my_tuple:", type(my_tuple))
# print("my_tuple:", my_tuple)



tuple1 = (1, 2)
tuple2 = (3, 4)

print("Original Tuple 1:", tuple1)
print("Original Tuple 2:", tuple2)

tuple1, tuple2 = tuple2, tuple1
print("Swapped Tuple 1:", tuple1)
print("Swapped Tuple 2:", tuple2)
