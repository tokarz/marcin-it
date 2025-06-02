import csv
# import pandas as pd

def get_csv_rows(fileName):
    rows = []

    index = 0
    # Replace 'your_file.csv' with the path to your CSV file
    with open(fileName, encoding="utf-8" ,newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for row in reader:
            if(index > 0):
                rows.append(row)
            index+=1
        
    return rows
    


      
