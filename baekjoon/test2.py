import sys
nums_squared_generator = (num ** 2 for num in range(100))

print(list(nums_squared_generator))
print(sys.getsizeof(nums_squared_generator))  # 128