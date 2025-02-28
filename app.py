import os
import csv
from data_model import DataModel

def load_excel_files(directory: str):
    data_model = DataModel()
    for file_name in os.listdir(directory):
        if file_name.endswith('.csv'):
            file_path = os.path.join(directory, file_name)
            with open(file_path, newline='') as csv_file:
                reader = csv.reader(csv_file)
                for row in reader:
                    data_model.add_data([row])
    return data_model

if __name__ == '__main__':
    excel_directory = input('Enter the directory where the excel files are located: ')
    data_model = load_excel_files(excel_directory)
    search_term = input('Enter the search term: ')
    results = data_model.query_like(search_term)
    print('Results:')
    for result in results:
        print(result)