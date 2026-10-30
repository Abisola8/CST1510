"""## Task 8: Pure Python EDA: Dataset Metadata
Ask for dataset name, rows, and columns. Print:
- dataset name in quotes
- rows and columns
- total cells (rows × columns)

**Example Output:**
```
"sales.csv"
Rows: 120
Columns: 8
Cells: 960
```"""

dataset_name = input("Enter dataset name: ")
rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))

total_cells = rows * columns

print(f"Dataset: {dataset_name} \nRows: {rows} \nColumns: {columns} \nCells: {total_cells}")