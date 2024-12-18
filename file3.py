class ModuleC:
    def __init__(self):
        self.metrics = {}

    def calculate_metrics(self, data):
        if not data:
            raise ValueError("Data cannot be empty!")
        
        self.metrics['mean'] = sum(data) / len(data)
        self.metrics['max'] = max(data)
        self.metrics['min'] = min(data)
        return self.metrics
