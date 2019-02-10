numbers=(7,4,3,8,2)
print(numbers)
convert=list(numbers)

convert.sort()
print('My sorted list is ascending:', convert)

numbers=tuple(convert)
print('This is my new tuple:',convert)
