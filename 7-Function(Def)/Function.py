# TASK 1
def draw_box():
    row = 14
    col = 10

    for i in range(row):
        for j in range(col):
            if i == 0 or i == row - 1:
                print('*', end='')
            else:
                if j == 0 or j == col - 1:
                    print('*', end='')
                else:
                    print(' ', end='')
        print()

# TASK 2
def draw_triangle():
    row = 10
    for i in range(row + 1):
        print('*' * i)



draw_box()
draw_triangle()