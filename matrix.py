# Matrix
print('------Matrix Creator------')

matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
sum_even = sum_odd = sum_column_3 = greater_value_2 = 0

for row in range (0, 3):
	for column in range (0, 3):
		matrix[row] [column] = int(input(f'Enter a value for [{row}, {column}]'))
		
		if matrix[row] [column] %2 == 0:
			sum_even += matrix[row] [column]
		else:
			sum_odd += matrix[row] [column]
			
		sum_column_3 += matrix[row] [2]
		if matrix[1] [column] > greater_value_2:
			greater_value_2 = matrix[1] [column]
		
print('-=' * 30)
print('--------Matrix--------')

for row in range (0, 3):
	for column in range (0, 3):
		print(f'[{matrix[row][column]:^5}]', end='')
	print()
	
print(f'The sum of the even values ​​entered is {sum_even}')
print(f'The sum of the odd values ​​entered is {sum_odd}')
print(f'The sum of the values ​​in column 3 is {sum_column_3}')
print(f'The greater value entered in row 2 is {greater_value_2}')