import FreeCAD
import Part
import pandas as pd
import os

# Define your FreeCAD document
doc = FreeCAD.ActiveDocument

def update_model(length, width, height):
    # Example of updating parameters (assuming your model uses named parameters)
    doc.getObject('YourPartName').Length = length
    doc.getObject('YourPartName').Width = width
    doc.getObject('YourPartName').Height = height
    doc.recompute()

def export_as_stl(file_path):
    # Export the part to STL
    import Mesh
    part = doc.getObject('YourPartName')
    Mesh.export([part], file_path)

def process_csv(csv_file, output_folder):
    # Read the CSV file
    df = pd.read_csv(csv_file)

    for index, row in df.iterrows():
        # Update model with new dimensions
        length = row['length']
        width = row['width']
        height = row['height']
        update_model(length, width, height)

        # Export the updated model to an STL file
        stl_file_path = os.path.join(output_folder, f'model_{index}.stl')
        export_as_stl(stl_file_path)

        print(f"Exported {stl_file_path}")

# Path to your CSV file
csv_file = '/path/to/your/parameters.csv'
# Folder where you want to save the STL files
output_folder = '/path/to/your/output/folder'

process_csv(csv_file, output_folder)
