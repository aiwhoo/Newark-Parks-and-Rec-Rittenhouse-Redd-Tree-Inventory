# Tree Inventory Data

This directory contains the raw and processed tree inventory data for Newark Parks and Recreation.

## Files

- **form-1__tree-inventory.json** - Raw tree inventory data collected from the survey form
- **processData.py** - Python script to convert JSON data to CSV format
- **roundUpData.py** - Python script to round numeric values in the processed data
- **processedTreeData.csv** - Processed tree data in CSV format
- **roundUpData.csv** - Final processed data with rounded metrics

## Usage

To process the raw data:

```bash
python processData.py form-1__tree-inventory.json processedTreeData.csv
python roundUpData.py processedTreeData.csv roundUpData.csv
```

## Data Fields

Each tree record contains:
- Surveyor Name
- Park Location
- Tree ID
- Photo URL
- Height (feet)
- GPS Coordinates (Latitude, Longitude, Accuracy)
- UTM Coordinates (Northing, Easting, Zone)
- Diameter at Breast Height
- Tree Spread measurements (two dimensions)
- Tree Condition (Good, Fair, Poor, Stump)
- Notes (mushrooms, rot, damage, etc.)
