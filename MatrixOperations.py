import numpy as np

# Function to take matrix input
def get_matrix(name):
    rows = int(input(f"\nEnter rows for Matrix {name}: "))
    cols = int(input(f"Enter columns for Matrix {name}: "))

    print("Enter the elements row-wise:")

    matrix = []

    for i in range(rows):
        row = list(map(float, input(f"Row {i+1}: ").split()))
        matrix.append(row)

    return np.array(matrix)


# Main Program
while True:

    print("\n" + "=" * 40)
    print("      MATRIX OPERATIONS TOOL")
    print("=" * 40)

    print("1. Addition")
    print("2. Subtraction")
    print("3. Matrix Multiplication")
    print("4. Transpose")
    print("5. Determinant")
    print("6. Inverse")
    print("0. Exit")

    choice = input("\nEnter your choice: ")

    try:

        # Addition
        if choice == "1":

            A = get_matrix("A")
            B = get_matrix("B")

            print("\nAddition Result:")
            print(A + B)

        # Subtraction
        elif choice == "2":

            A = get_matrix("A")
            B = get_matrix("B")

            print("\nSubtraction Result:")
            print(A - B)

        # Matrix Multiplication
        elif choice == "3":

            A = get_matrix("A")
            B = get_matrix("B")

            print("\nMultiplication Result:")
            print(np.dot(A, B))

        # Transpose
        elif choice == "4":

            A = get_matrix("A")

            print("\nTranspose:")
            print(A.T)

        # Determinant
        elif choice == "5":

            A = get_matrix("A")

            print("\nDeterminant:")
            print(round(np.linalg.det(A), 4))

        # Inverse
        elif choice == "6":

            A = get_matrix("A")

            if np.linalg.det(A) == 0:
                print("\nInverse does not exist (Singular Matrix)")
            else:
                print("\nInverse:")
                print(np.linalg.inv(A))

        # Exit
        elif choice == "0":

            print("\nThank you for using Matrix Operations Tool!")
            break

        else:
            print("\nInvalid Choice!")

    except Exception as e:
        print("\nError:", e)