import os
import csv
class DataModel:
    def __init__(self):
        self.data = []
        self.headers = []
        
    def add_data(self, new_data):
        self.data.extend(new_data)

    def query(self, query_function):
        return list(filter(query_function, self.data))
    
    def query_like(self, substring):
        substring_lower = substring.lower()
        return [row for row in self.data if any(substring_lower in str(cell).lower() for cell in row)]
    
def load_excel_files(directories: str):
    data_model = DataModel()
    directories_list = directories.split(',') if ',' in directories else [directories]
    for directory in directories_list:
        for file_name in os.listdir(directory):
            if file_name.endswith('.csv'):
                file_path = os.path.join(directory, file_name)
                with open(file_path, newline='') as csv_file:
                    reader = csv.reader(csv_file)
                    for row in reader:
                        data_model.add_data([row])
    return data_model