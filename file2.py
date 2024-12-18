class ModuleB:
    def __init__(self):
        self.log = []

    def process_data(self, input_data):
        original, processed = input_data["original"], input_data["processed"]
        with open("log.txt", "w") as log_file:
            for idx, value in enumerate(processed):
                result = value + sum(original)
                self.log.append(result)
                log_file.write(f"Step {idx}: {result}\n")
        return self.log
