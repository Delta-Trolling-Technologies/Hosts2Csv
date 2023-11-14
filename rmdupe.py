def remove_duplicates(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

        unique_lines = list(set(lines))

        with open(file_path, 'w') as file:
            file.writelines(unique_lines)

        print(f"Duplicates removed from {file_path} successfully.")

    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

file_path = 'final.csv'
remove_duplicates(file_path)
