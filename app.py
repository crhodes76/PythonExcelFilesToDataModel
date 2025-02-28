import os
import csv
from data_model import DataModel, load_excel_files

if __name__ == '__main__':
    excel_directory = input('Enter the directory where the excel files are located: ')
    data_model = load_excel_files(excel_directory)
    search_term = input('Enter the search term: ')
    results = data_model.query_like(search_term)
    print('Results:')
    for result in results:
        print(result)