# # SparseMatrix Application

## Description

The SparseMatrix application allows you to perform operations (addition, subtraction, multiplication) on two sparse matrices provided as input files. The matrices are stored in a specific format in text files, and the results of operations are output to a new file.

## File Format

The input files should be formatted as follows:

rows=<number_of_rows>
cols=<number_of_columns>
(row,col,value)
(row,col,value)


## Usage

1. Ensure your input files are correctly formatted and located in the specified paths.
2. Run the application and provide the paths to the input files and the desired operation.

## Installation

1. Clone the repository or download the script.
   ```
   ```
3. Ensure Python is installed on your system. python3 is recommended

## Running the Application

Run the application by executing the script:

```sh
python sparse_matrix.py
```

You will be prompted to provide the paths to the input files and the desired operation (add, subtract, multiply).


Example

Write the path of your first file containing a matrix:
path/to/first_matrix.txt

Write the path of your second file containing a matrix:
path/to/second_matrix.txt

Type in operation to use (add, subtract, multiply):
add


## Output
The result will be saved in the sample_outputs directory with a file name derived from the input file names.

Error Handling
The application checks for:

Correct file format.
Existence of the input files.
Dimension compatibility for matrix operations.
If there are any errors, appropriate messages will be displayed.

##License  
This project is licensed under the MIT License - see the LICENSE file for details.

## Author
Imanzi Kabisa Placide



