import numpy as np
def main_menu(choice):
    if choice == '1': #add matrices
        matrix1 = create_matrix(input("Enter size of first matrix:"))
        matrix2 = create_matrix(input("Enter size of second matrix:"))
        sum = add_matrices(matrix1, matrix2)
        #figure out how to return it
        return sum
    elif choice == "2":
        matrix = create_matrix(input("Enter matrix size:"))
        const = float(input("Enter constant:"))
        return multiply_matrix_const(matrix, const)
    elif choice == '3': #multiply matrices
        matrix1 = create_matrix(input("Enter size of first matrix:"))
        matrix2 = create_matrix(input("Enter size of second matrix:"))
        return multiply_two_ms(matrix1, matrix2)
    elif choice == '4': # transpose a matrix
        print("""\n1. Main diagonal
2. Side diagonal
3. Vertical line
4. Horizontal line""")
        option = input("Your choice:")
        matrix = create_matrix(input("Enter matrix size:"))
        return transpose(matrix,option)
    elif choice == '5':
        matrix = create_matrix(input("Enter matrix size:"))
        return determinant(matrix)
    elif choice == '6':
        matrix = create_matrix(input("Enter matrix size:"))
        return inverse(matrix)
    elif choice == "0":
        pass
def add_matrices(matrix1, matrix2): #also requires dimensions but they can be calculated
    rows1 = len(matrix1)
    cols1 = len(matrix1[0])
    rows2 = len(matrix2)
    cols2 = len(matrix2[0])
    if rows1 == rows2 and cols1 == cols2:
        sum = matrix1 + matrix2
        return sum
    else:
        return "The operation cannot be performed."
def create_matrix(dim, num=0): #takes matrix dimensions and number of matrices to be created
    dim = dim.split()
    rows = int(dim[0])
    cols = int(dim[1])
    matr = []
    if num == 1:
        number = " first"
    elif num == 2:
        number = " second"
    elif num == 0:
        number = ""
    print(f"Enter{number} matrix:")
    for i in range(rows):
        entry = input().split()
        r = [float(i) for i in entry] #creates a floats matrix
        matr.append(r)
    matr = np.array(matr)
    return matr
def multiply_two_ms(matrix1, matrix2):
    #num1 and 2 matrix dimensions
    try:
        product = matrix1.dot(matrix2)
        return product
    except Exception:
        return "The operation cannot be performed."
def multiply_matrix_const(matrix, const):
    prod = matrix * const
    return prod
def transpose(matrix, option):
    row = len(matrix)
    cols = len(matrix[0])
    new = [[0 for j in range(cols)] for i in range(row)]
    if option == '1': #main diagonal
        t = np.transpose(matrix)
        return t
    elif option == '2':
        for i in range(row):
            for j in range(cols):
                new[i][j] = matrix[-j - 1][-i - 1]
        return new
    elif option == '3':
        for i in range(row):
            for j in range(cols):
                new[i][j] = matrix[i][-j - 1]
        return new
    elif option == '4':
        for i in range(row):
            for j in range(cols):
                new[i][j] = matrix[-i - 1][j]
        return new
def determinant(matrix):
    d = np.linalg.det(matrix)
    return d
def inverse(matrix):
    matr = np.linalg.inv(matrix)
    return matr
while True:
    print("""\n1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
6. Inverse matrix
0. Exit""")
    user_choice = input("Your choice:")
    if user_choice == "0":
        break
    else:
        result = main_menu(user_choice)
        if type(result) is np.ndarray or type(result) is list:
            print("The result is:")
            for i in result:
                print(*i)
        else:
            print(result)
