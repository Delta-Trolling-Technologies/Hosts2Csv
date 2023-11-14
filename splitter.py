import csv
import os

def split_csv_into_parts(input_csv, output_folder, lines_per_part):
    with open(input_csv, 'r') as csv_file:
        reader = csv.reader(csv_file)
        header = next(reader)

        part_number = 1
        current_part_lines = []
        for row in reader:
            current_part_lines.append(row)
            if len(current_part_lines) == lines_per_part:
                output_file = os.path.join(output_folder, f'part_{part_number}.csv')
                write_csv_part(output_file, header, current_part_lines)
                current_part_lines = []
                part_number += 1

        if current_part_lines:
            output_file = os.path.join(output_folder, f'part_{part_number}.csv')
            write_csv_part(output_file, header, current_part_lines)

def write_csv_part(output_file, header, lines):
    with open(output_file, 'w', newline='') as part_file:
        writer = csv.writer(part_file)
        writer.writerow(header)
        writer.writerows(lines)

input_csv_file = 'final.csv'
output_folder = 'parts'
lines_per_part = 999

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

split_csv_into_parts(input_csv_file, output_folder, lines_per_part)