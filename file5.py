class ModuleE:
    def __init__(self):
        self.summary = ""

    def summarize(self, stored_results):
        self.summary = "Summary Report:\n"
        for key, value in stored_results.items():
            self.summary += f"{key.capitalize()}: {value:.2f}\n"

        with open("summary_report.txt", "w") as file:
            file.write(self.summary)

        return self.summary
