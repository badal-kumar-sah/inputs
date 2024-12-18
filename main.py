# Main file: main.py

from file1 import ModuleA
from file2 import ModuleB
from file3 import ModuleC
from file4 import ModuleD
from file5 import ModuleE

def main():
    print("Starting aggregation of modules...")

    a = ModuleA()
    b = ModuleB()
    c = ModuleC()
    d = ModuleD()
    e = ModuleE()

    result_a = a.execute_task()
    result_b = b.process_data(result_a)
    result_c = c.calculate_metrics(result_b)
    result_d = d.store_results(result_c)
    final_result = e.summarize(result_d)

    print("Final Result:", final_result)

if __name__ == "__main__":
    main()
