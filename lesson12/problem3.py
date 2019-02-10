import random
ROWS=3
COLS=3


values=[0,0,0],[0,0,0],[0,0,0]
for r in range(ROWS):
    for c in range(COLS):
        values[r][c]=random.randint(1,4)
print(values)


for row in values:
    total=0.0
    for cell in row:
        total+=cell
    print("Total is:", total)

col0_total=values[0][0]+values[1][0]+values[2][0]
print('Total of column 0 is:', col0_total)
col1_total=values[1][0]+values[1][1]+values[1][2]
print('Total of column 1 is:',col1_total)
col2_total=values[2][0]+values[2][1]+values[2][2]
print('The total of column 2 is: ',col2_total)
