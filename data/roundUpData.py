"""
Round up numeric tree metrics to standardized values.
"""

import csv
import sys
from pathlib import Path

def round_up_metrics(input_csv, output_csv):
    """
    Round up tree metrics (height, diameter, spreads) to nearest whole number.
    
    Args:
        input_csv: Path to input CSV file with processed data
        output_csv: Path to output CSV file with rounded values
    """
    try:
        # Read input CSV
        rows = []
        with open(input_csv, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            fieldnames = reader.fieldnames
            
            for row in reader:
                # Round numeric fields
                numeric_fields = [
                    'Height_ft',
                    'Diameter_at_Breast',
                    'Tree_Spread_tip_to_1',
                    'Tree_Spread_tip_to_2',
                    'Accuracy',
                    'UTM_Northing',
                    'UTM_Easting'
                ]
                
                for field in numeric_fields:
                    if field in row and row[field]:
                        try:
                            value = float(row[field])
                            # Round up to nearest integer
                            import math
                            row[field] = str(math.ceil(value))
                        except ValueError:
                            pass  # Keep original if not numeric
                
                rows.append(row)
        
        # Write output CSV
        with open(output_csv, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)
        
        print(f"Successfully rounded metrics for {len(rows)} trees.")
        print(f"Output written to: {output_csv}")
        
    except FileNotFoundError:
        print(f"Error: Input file '{input_csv}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error rounding data: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Default paths
    input_file = "processedTreeData.csv"
    output_file = "roundUpData.csv"
    
    # Allow command line arguments
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    if len(sys.argv) > 2:
        output_file = sys.argv[2]
    
    round_up_metrics(input_file, output_file)
