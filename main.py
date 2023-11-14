import csv

def clean_hosts_file(input_file, output_cleaned_file):
    with open(input_file, 'r') as hosts_file:
        lines = hosts_file.readlines()

    cleaned_lines = []
    for line in lines:
        line_parts = line.split('#')[0].split()
        if line_parts:
            cleaned_line = line_parts[-1]
            cleaned_lines.append(cleaned_line.strip())

    with open(output_cleaned_file, 'w') as cleaned_file:
        cleaned_file.write('\n'.join(cleaned_lines))

def convert_hosts_to_csv(input_file, output_file):
    with open(input_file, 'r') as cleaned_hosts_file:
        cleaned_lines = cleaned_hosts_file.readlines()

    with open(output_file, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        for domain in cleaned_lines:
            writer.writerow([domain.strip()])

input_hosts_file = 'input.txt'
output_cleaned_file = 'cleaned_input.txt'
output_csv_file = 'output.csv'

clean_hosts_file(input_hosts_file, output_cleaned_file)

convert_hosts_to_csv(output_cleaned_file, output_csv_file)