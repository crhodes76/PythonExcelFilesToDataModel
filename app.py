import os
import csv
from data_model import DataModel, load_excel_files
from termcolor import colored
from tabulate import tabulate

if __name__ == '__main__':
    excel_directory = input('Enter the directory where the excel files are located, for multiple directories separate by a comma. ')
    data_model = load_excel_files(excel_directory)
    search_term = input('Enter the search term: ')
    results = data_model.query_like(search_term)
    
    if results:
        print('Results:')
        for header, rows in results.items():
            table = [header] + rows
            highlighted_table = [
                [colored(cell, 'green') if search_term.lower() in str(cell).lower() else cell for cell in row]
                for row in table
            ]
            print(tabulate(highlighted_table, headers="firstrow", tablefmt="grid"))
    else:
        print('No results found.')