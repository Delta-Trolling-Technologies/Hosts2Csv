import pandas as pd
import os

def merge_and_remove_duplicates(input_folder, output_file):
    if not os.path.exists(input_folder):
        print(f"The '{input_folder}' doesn't exist.")
        return
    
    csv_files = [file for file in os.listdir(input_folder) if file.endswith('.csv')]
    
    if len(csv_files) < 2:
        print("2 csv files required minimum.")
        return
    
    result_df = pd.read_csv(os.path.join(input_folder, csv_files[0]))
    
    for file in csv_files[1:]:
        df = pd.read_csv(os.path.join(input_folder, file))
        result_df = pd.concat([result_df, df]).drop_duplicates().reset_index(drop=True)
    
    result_df.to_csv(output_file, index=False)
    
    print(f"Finished merging csv files: {output_file}")

input_folder = "merge_dir"
output_file = "merged.csv"
merge_and_remove_duplicates(input_folder, output_file)
