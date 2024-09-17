# FreeCAD CSV to STL Exporter

This project provides a Python script to automate the process of reading dimensions from a CSV file, updating a FreeCAD model, and exporting it as an STL file for 3D printing. It is designed to save time when dealing with multiple variations of a model.

## Installation

Follow these steps to get the project up and running:

1. **Clone the Repository**

   ```bash
   git clone https://github.com/filippoberti2020/freecad-csv-stl-exporter.git
   cd freecad-csv-stl-exporter
    ```
2. **Ensure you have pandas installed. Use the following command to install the required Python packages:**
   ```bash
   pip install -r requirements.txt
    ```
3. **Run the Script**
  - Open FreeCAD.
  - Go to the Python console or use the macro editor.
  - Copy and paste the script from `exporter_script.py` and execute it.

## Requirements

- **FreeCAD**: This script must be run within the FreeCAD environment or as a macro in FreeCAD. [Download FreeCAD](https://www.freecad.org/downloads.php)
- **Python Libraries**: The script uses the `pandas` library. Install it using `pip`:

  ```bash
  pip install -r requirements.txt
  ```
## Prepare Your CSV File

Your CSV file should be structured with columns for the dimensions you want to update. Example CSV file:

```csv
length,width,height
10,5,2
15,7,3
20,10,4
```

## Configure the Script

Edit the script to match the names and parameters of your FreeCAD model:

1. Open `exporter_script.py` in your text editor.
2. Replace `'YourPartName'` with the actual name of your FreeCAD part.
3. Update the `csv_file` and `output_folder` paths in the script.

## Run the Script

1. Open FreeCAD.
2. Go to the Python console or use the macro editor.
3. Copy and paste the script from `exporter_script.py` and execute it.

## Example Usage

Here’s how you might set up and run the script:

1. **Prepare the CSV File**: Save your dimensions in a CSV file, e.g., `parameters.csv`.
2. **Configure Output Folder**: Make sure you have a folder ready to store the STL files, e.g., `output`.
3. **Execute the Script**: Run the script inside FreeCAD’s Python console or as a macro.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
