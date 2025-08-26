# 🔢 3x3 Matrix Analyzer

A command-line tool that populates a 3x3 matrix with numbers provided by the user. After the matrix is filled, it's displayed in a formatted way, followed by a specific analysis of the data.

## Features

* **Matrix Creation**: Builds a 3x3 matrix from nine user-provided integers.
* **Formatted Display**: Prints the final matrix in a clean, grid-like format with centered values.
* **Data Analysis**: After creation, the script reports four statistics:
    1.  The sum of all even numbers.
    2.  The sum of all odd numbers.
    3.  The sum of all values in the third column.
    4.  The greatest value from the second row.

## How to Use

1.  Ensure you have Python installed.
2.  Save the code as a `.py` file (e.g., `matrix.py`).
3.  Run the script from your terminal:
    ```sh
    python matrix.py
    ```
4.  The program will prompt you to enter a value for each position in the matrix, from `[0, 0]` to `[2, 2]`.
5.  After the ninth value is entered, the script will display the formatted matrix and the results of the analysis.

### Example Session

```sh
> python matrix.py
------Matrix Creator------
Enter a value for [0, 0]5
Enter a value for [0, 1]1
Enter a value for [0, 2]4
Enter a value for [1, 0]8
Enter a value for [1, 1]2
Enter a value for [1, 2]7
Enter a value for [2, 0]3
Enter a value for [2, 1]6
Enter a value for [2, 2]9
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
--------Matrix--------
[  5  ] [  1  ] [  4  ]
[  8  ] [  2  ] [  7  ]
[  3  ] [  6  ] [  9  ]
The sum of the even values ​​entered is 20
The sum of the odd values ​​entered is 25
The sum of the values ​​in column 3 is 60
The greater value entered in row 2 is 8
```
