import os
import csv
from collections import defaultdict

class DataModel:
    def __init__(self):
        self.data = defaultdict(list)
        
    def add_data(self, header, new_data):
        self.data[tuple(header)].extend(new_data)

    def query(self, query_function):
        results = defaultdict(list)
        for header, rows in self.data.items():
            filtered_rows = list(filter(query_function, rows))
            if filtered_rows:
                results[header].extend(filtered_rows)
        return results
    
    def query_like(self, substring):
        substring_lower = substring.lower()
        results = defaultdict(list)
        for header, rows in self.data.items():
            for row in rows:
                if any(substring_lower in str(cell).lower() for cell in row):
                    results[header].append(row)
        return results
    
def load_excel_files(directories: str):
    data_model = DataModel()
    directories_list = directories.split(',') if ',' in directories else [directories]
    for directory in directories_list:
        for file_name in os.listdir(directory):
            if file_name.endswith('.csv'):
                file_path = os.path.join(directory, file_name)
                with open(file_path, newline='') as csv_file:
                    reader = csv.reader(csv_file)
                    headers = next(reader)
                    for row in reader:
                        data_model.add_data(headers, [row])
    return data_model