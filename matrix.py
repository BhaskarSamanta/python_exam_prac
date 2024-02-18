rows = int(input("Enter the number of rows:"))
cols = int(input("Enter the number of columns:"))
def create_matrix(rows,cols):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            element = int(input(f"Enter element at position ({i+1}, {j+1}) : "))
            row.append(element)
        matrix.append(row)
    return matrix

print("----------First Matrix---------")
my_matrix1 = create_matrix(rows,cols)

print("----------Second Matrix---------")
my_matrix2 = create_matrix(rows,cols)

print("First Matrix : ")
print(my_matrix1)

print("Second Matrix : ")
print(my_matrix2)

def addition(matrix1, matrix2):
    add_matrix = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            ele_sum = matrix1[i][j] + matrix2[i][j]
            row.append(ele_sum)
        add_matrix.append(row)
    return add_matrix
sum_matrix = addition(my_matrix1, my_matrix2)
print("Sum of the two matrix is : \n",sum_matrix)


def subtraction(matrix1, matrix2):
    sub_matrix = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            ele_sub = matrix1[i][j] - matrix2[i][j]
            row.append(ele_sub)
        sub_matrix.append(row)
    return sub_matrix
subMatrix = subtraction(my_matrix1, my_matrix2)
print("Subtraction of the two matrix is : \n",subMatrix)


def multiplication(matrix1, matrix2):
    product_matrix = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            element_sum = sum(matrix1[i][k] * matrix2[k][j] for k in range(len(matrix2)))
            row.append(element_sum)
        product_matrix.append(row)

    return product_matrix

pro_matrix = multiplication(my_matrix1, my_matrix2)
print("Multiplication of the two matrix is : \n", pro_matrix)




        
        
            