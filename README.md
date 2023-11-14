# Hosts2Csv

## 1. How to use

1. Rename your downloaded or self created hosts file to: `input.txt`
   - And put it into the root directory of the cloned repo
2. Run `main.py`
   - This will create a `cleaned_input.txt` and an `output.csv`
   - We will only need `output.csv` so you can delete `cleaned_input.txt`
   - Don't forget to rename `output.csv`

**ONLY IF YOU WILL USE MORE THAN 1 HOSTS**

1. Create a folder named `merge_dir` and put all your csv files there
2. Run `merge.py`
   - This will create a `merged.csv` file
3. Run `cleaner.py`
   - This will create a `final.csv` file
4. Run `rmdupe.py`
   - This will remove any commas from your `final.csv` file
5. Run `splitter.py`
   - This will make a part every 1000th line
   - Your parts will be put into the `parts` folder

**YOU MAY WANT TO DO THIS WITH YOUR CSV IF IT HAS MORE THAN 1000 LINES, BUT YOU USED 1 HOSTS**

1. Rename `output.csv` to `final.csv`
2. Run `splitter.py`

Then just upload your csv file(s) to cloudflare zero trust

Happy blocking! :)
