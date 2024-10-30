
def pascals_triangle(n):
    triangle = [] # to store rows of triangle
    for i in range(n): # iterates n times to generate rows
        row = [1] # The first element is always 1
        if triangle: # accounts for previous rows
            last_row = triangle[-1]
            for j in range(len(last_row)-1):
                row.append(last_row[j]+last_row[j+1])
            row.append(1) # The last element is always 1
        triangle.append(row)

    max_width = len(' '. join(map(str, triangle[-1])))
    for row in triangle:
        row_str = ' '.join(map(str, row))
        print(row_str.center(max_width))    
    
pascals_triangle(5)