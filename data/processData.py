"""
Data processing script for tree inventory data.
Converts raw tree inventory JSON to processed CSV format.
"""

import json
import csv
import sys
from pathlib import Path

def process_tree_data(input_json, output_csv):
    """
    Process raw tree inventory JSON data into CSV format.
    
    Args:
        input_json: Path to input JSON file
        output_csv: Path to output CSV file
    """
    try:
        # Load JSON data
        with open(input_json, 'r') as f:
            data = json.load(f)
        
        # Extract tree records
        trees = data.get('data', [])
        
        if not trees:
            print("No tree data found in JSON file.")
            return
        
        # Define CSV headers
        fieldnames = [
            'Surveyor_Name',
            'Park_Location', 
            'Tree_ID',
            'Photo_URL',
            'Height_ft',
            'Latitude',
            'Longitude',
            'Accuracy',
            'UTM_Northing',
            'UTM_Easting',
            'UTM_Zone',
            'Diameter_at_Breast',
            'Tree_Spread_tip_to_1',
            'Tree_Spread_tip_to_2',
            'Tree_Condition',
            'Notes'
        ]
        
        # Write CSV file
        with open(output_csv, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            
            for tree in trees:
                row = {
                    'Surveyor_Name': tree.get('1_Surveyor_Name', [''])[0],
                    'Park_Location': tree.get('2_Park_Location', ''),
                    'Tree_ID': tree.get('3_Tree_ID', ''),
                    'Photo_URL': tree.get('4_Photo', ''),
                    'Height_ft': tree.get('5_Tree_Height_ft', ''),
                    'Latitude': tree.get('6_Location', {}).get('latitude', ''),
                    'Longitude': tree.get('6_Location', {}).get('longitude', ''),
                    'Accuracy': tree.get('6_Location', {}).get('accuracy', ''),
                    'UTM_Northing': tree.get('6_Location', {}).get('UTM_Northing', ''),
                    'UTM_Easting': tree.get('6_Location', {}).get('UTM_Easting', ''),
                    'UTM_Zone': tree.get('6_Location', {}).get('UTM_Zone', ''),
                    'Diameter_at_Breast': tree.get('7_Diameter_at_Breast', ''),
                    'Tree_Spread_tip_to_1': tree.get('8_Tree_Spread_tip_to', ''),
                    'Tree_Spread_tip_to_2': tree.get('9_Tree_Spread_tip_to', ''),
                    'Tree_Condition': tree.get('10_Tree_Condition', ''),
                    'Notes': tree.get('11_Notes_eg_mushroom', '')
                }
                writer.writerow(row)
        
        print(f"Successfully processed {len(trees)} trees.")
        print(f"Output written to: {output_csv}")
        
    except FileNotFoundError:
        print(f"Error: Input file '{input_json}' not found.")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in '{input_json}'")
        sys.exit(1)
    except Exception as e:
        print(f"Error processing data: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Default paths
    input_file = "form-1__tree-inventory.json"
    output_file = "processedTreeData.csv"
    
    # Allow command line arguments
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    if len(sys.argv) > 2:
        output_file = sys.argv[2]
    
    process_tree_data(input_file, output_file)
