import os

# Get the current working directory
current_dir = os.getcwd()

# Define the paths to components, src, and artifacts folders
components_folder = os.path.join(current_dir, 'components')
src_folder = os.path.join(current_dir, 'src')
artifacts_folder = os.path.join(current_dir, 'artifacts')

# Define the paths to input and output files
input_file_path = os.path.join(src_folder, 'example.py')
input_csv_path = os.path.join(artifacts_folder, 'train.csv')
output_csv_path = os.path.join(artifacts_folder, 'exampletrain.csv')

# Read the first row of data from train.csv
with open(input_csv_path, 'r') as input_file:
    first_row = input_file.readline().strip()

# Create a new file named exampletrain.csv in artifacts folder and write the first row to it
with open(output_csv_path, 'w') as output_file:
    output_file.write(first_row)

# Print success message
print(f"First row from {input_csv_path} written to {output_csv_path}")
