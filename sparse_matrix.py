import os
import shutil  # for copying the files to another specific path

class SparseMatrix:
    """Base class for the whole application"""
    def __init__(self, file_path1, file_path2):
        self.full_path1 = file_path1
        self.full_path2 = file_path2
        self.file_path1 = os.path.basename(file_path1)
        self.file_path2 = os.path.basename(file_path2)
        self.file_name1 = os.path.join("sample_inputs", os.path.basename(file_path1))
        self.file_name2 = os.path.join("sample_inputs", os.path.basename(file_path2))
        self.matrix1 = {}
        self.matrix2 = {}
        self.numRows1 = 0
        self.numCols1 = 0
        self.numRows2 = 0
        self.numCols2 = 0

    def read_file(self, file_path, file_name):
        """Reads and processes a single input file containing a matrix"""
        if os.path.exists(file_path):
            os.makedirs("sample_inputs", exist_ok=True)
            matrix = {}
            numRows = numCols = 0
            shutil.copy(file_path, file_name)
            with open(file_name, "r", errors="ignore") as file:
                lines = file.readlines()

            if len(lines) < 2:
                print(f"Sorry, file path {file_path} has wrong file format")
                return None, 0, 0

            if lines[0].strip().split('=')[0] != "rows" or lines[1].strip().split('=')[0] != "cols":
                print(f"Sorry, file path {file_path} has wrong file format")
                return None, 0, 0

            try:
                numRows = int(lines[0].strip().split('=')[1])
                numCols = int(lines[1].strip().split('=')[1])
            except (IndexError, ValueError):
                print(f"Sorry, file path {file_path} has wrong file format")
                return None, 0, 0

            for line in lines[2:]:
                line = line.strip()
                if not line:
                    continue
                line = line.replace('(', '').replace(')', '')
                parts = line.split(',')
                if len(parts) != 3:
                    print(f"Sorry, file path {file_path} has wrong file format")
                    return None, 0, 0
                try:
                    row, col, val = int(parts[0]), int(parts[1]), int(parts[2])
                    matrix[(row, col)] = val
                except ValueError:
                    print(f"Sorry, file path {file_path} has wrong file format")
                    return None, 0, 0

            return matrix, numRows, numCols
        else:
            print(f"Sorry file path provided {file_name} do not exist")

    def read_files(self):
        """Reads and processes the input files containing matrices"""
        
        try:
            self.matrix1, self.numRows1, self.numCols1 = self.read_file(self.full_path1, self.file_name1)
            if self.matrix1 is None or self.numCols1 == 0 or self.numRows1 == 0:
                print(f"Sorry the file is not found {self.file_path1}\n")
                return   
        except Exception as e:
            print(f"There was an error in reading file {self.full_path1}: {e}")
            return      
    
        
        try:
            self.matrix2, self.numRows2, self.numCols2 = self.read_file(self.full_path2, self.file_name2)
            if self.matrix2 is None or self.numCols2 == 0 or self.numRows2 == 0:
                print(f"Sorry the file is not found {self.file_path2}\n")
                return
        except Exception as e:
            print(f"There was an error in reading file {self.full_path2}: {e}")
            return

    def add_matrices(self):
        """Adds 2 matrices from the input files"""
        if self.numCols1 == self.numCols2 and self.numRows1 == self.numRows2:
            result_matrix = {}
            allkeys = set(self.matrix1.keys())
            allkeys.update(self.matrix2.keys())

            for key in allkeys:
                result_matrix[key] = self.matrix1.get(key, 0) + self.matrix2.get(key, 0)

            return result_matrix
        else:
            print(f"Sorry, file path {self.file_path1} and file path {self.file_path2} have matrices of different dimensions. Dimensions must match for successful addition.")
            return None

    def subtract_matrices(self):
        """Subtracts 2 matrices from the input files"""
        if self.numCols1 == self.numCols2 and self.numRows1 == self.numRows2:
            result_matrix = {}
            allkeys = set(self.matrix1.keys())
            allkeys.update(self.matrix2.keys())

            for key in allkeys:
                result_matrix[key] = self.matrix1.get(key, 0) - self.matrix2.get(key, 0)

            return result_matrix
        else:
            print(f"Sorry, file path {self.file_path1} and file path {self.file_path2} have matrices of different dimensions. Dimensions must match for successful subtraction.")
            return None

    def multiply_matrices(self):
        """Multiplies two matrices"""
        if self.numCols1 != self.numRows2:
            raise ValueError("Number of columns of first matrix must equal number of rows of second matrix")

        result_matrix = {}

        for (i, k) in self.matrix1.keys():
            for j in range(self.numCols2):
                if (k, j) in self.matrix2:
                    if (i, j) not in result_matrix:
                        result_matrix[(i, j)] = 0
                    result_matrix[(i, j)] += self.matrix1[(i, k)] * self.matrix2[(k, j)]

        return result_matrix

    def output(self, rows, cols, result):
        """Responsible for outputting the result in a new file"""
        os.makedirs("sample_outputs", exist_ok=True)
        decoration = f"{os.path.basename(self.file_path1)}_{os.path.basename(self.file_path2)}"
        result_file = os.path.join("sample_outputs", decoration)
        with open(result_file, "w") as result_file:
            result_file.write(f"rows={rows}\n")
            result_file.write(f"cols={cols}\n")
            for (row, col), val in result.items():
                result_file.write(f"({row},{col},{val})\n")

def main():
    """This is the center of all the operations of our application"""
    print("""\nWelcome to Sparse_Matrix, do operations on matrices in just a second 
          Enter Quit to exit the application\n""")
    file1 = input("\nWrite the path of your first file containing a matrix or enter *quit* to exit program: ")
    if file1.lower() == "quit":
        print("\n Thank you for using our app, you are always welcome")
        return 
    
    file2 = input("\nWrite the path of your second file containing a matrix: ")
    operation = input("\nType in operation to use choose (add, subtract, multiply): ")

    matrix = SparseMatrix(file1, file2)
    matrix.read_files()
    

    if operation.lower() == "add":
        try:
            result = matrix.add_matrices()
            if result:
                rows = matrix.numRows1
                cols = matrix.numCols1
                matrix.output(rows, cols, result)
                print("\nAddition done successfully\n")
        except Exception as e:
            print(f"Error adding matrices: {e}")
    elif operation.lower() == "subtract":
        try:
            result = matrix.subtract_matrices()
            if result:
                rows = matrix.numRows1
                cols = matrix.numCols1
                matrix.output(rows, cols, result)
                print("\nsubtract done successfully\n")
        except Exception as e:
            print(f"Error subtracting matrices: {e}")
    elif operation.lower() == "multiply":
        try:
            result = matrix.multiply_matrices()
            rows = matrix.numRows1
            cols = matrix.numCols2
            matrix.output(rows, cols, result)
            print("\nMultiplication done successfully\n")
        except Exception as e:
            print(f"Error multiplying matrices: {e}")
    else:
        print("\n Wrong Operation. Please select among these: 'add', 'subtract', 'multiply' ")

if __name__ == "__main__":
    main()
