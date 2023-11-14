def remove_commas(input_file, output_file):
    try:
        with open(input_file, 'r') as f:
            lines = f.readlines()
        
        lines_without_commas = [line.replace(',', '') for line in lines]
        
        with open(output_file, 'w') as f:
            f.writelines(lines_without_commas)
        
        print(f"Removed commas: {output_file}")

    except FileNotFoundError:
        print(f"File not found: {input_file}")
    except Exception as e:
        print(f"Error: {e}")

input_file = "merged.csv"
output_file = "final.csv"
remove_commas(input_file, output_file)
