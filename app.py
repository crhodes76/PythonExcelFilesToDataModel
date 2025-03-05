import os
import csv
from data_model import DataModel, load_excel_files
from termcolor import colored

if __name__ == '__main__':
    excel_directory = input('Enter the directory where the excel files are located, for multiple directories separate by a comma. ')
    data_model = load_excel_files(excel_directory)
    search_term = input('Enter the search term: ')
    results = data_model.query_like(search_term)
    
    if results:
        # Print column headers
        print('Results:')
       
        # Print each result with the search term highlighted
        for result in results:
            highlighted_result = [colored(cell, 'green') if search_term.lower() in str(cell).lower() else cell for cell in result]
            print(', '.join(highlighted_result))
    else:
        print('No results found.')