class DataModel:
    def __init__(self):
        self.data = []
        
    def add_data(self, new_data):
        self.data.extend(new_data)

    def query(self, query_function):
        return list(filter(query_function, self.data))
    
    def query_like(self, substring):
        return [row for row in self.data if any(substring in str(cell) for cell in row)]