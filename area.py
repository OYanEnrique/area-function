#Area Calculator Function

def area(width, length):
	a = width * length
	print(f'The area of ​​a plot of land is {width} x {length} is {a}m².')
	
print('------Area calculator------')

width = float(input('Enter the width:\n'))
length = float(input('Enter the length:\n'))

area(width, length)