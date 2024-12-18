class ModuleA:
    def __init__(self):
        self.data = [i for i in range(1, 11)]

    def execute_task(self):
        processed_data = [x**2 for x in self.data if x % 2 == 0]
        return {"original": self.data, "processed": processed_data}
