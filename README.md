# Python Distributed Task Runner

This repository is an implementation of a **distributed system** that executes multiple Python scripts in parallel, collects results, and performs post-task processes like packaging the outputs.

## How It Works
1. **Task Distribution**: The ``BuildServer`` class scans the directory (``python_source/``) for Python scripts (``.py`` files). Each script is queued and processed by worker processes running in parallel.
2. **Parallel Execution**: Each script is executed in its own process, with its execution time being reocrded and stored in a result queue
3. **Post-Processing**: After all scripts are executed, a post-processing task is performed (packaging the outputs)
4. **Result Collection**: All results are collected from the result queue (execution success and time taken for each individual script).

The system also includes **error handling** if one occurs during script execution (e.g. syntax errors or ``subprocess.CalledProcessError``), the error is logged in the result queue. 

## File Structure
```bash
├── python_source/         # Directory containing the test scripts for distributed execution
│   ├── Prime.py           # Test script for prime number calculation
│   ├── Matrix.py          # Test script for matrix multiplication
│   └── Fibonacci.py       # Test script for Fibonacci sequence generation  
├── main.py                # Distributed system for parallel script execution
├── individual_test.py     # Test for sequential execution of all methods in the source folder
└── README.md              # Documentation
```

## Testing Parameters
The following parameters were used for testing:
- **Prime Calculation**: ```primes = calculate_primes(2000000)```
- **Matrix Multiplication**: ```result = matrix_multiplication(10000)```
- **Fibonacci Sequence Generation**: ```fib_sequence = fibonacci(35)```

## Test Results
### Individual Test:
```bash
Calculating primes
Found 148933 primes
Prime: 9.13s

Performing matrix multiplication
Finished matrix multiplication
Matrix: 8.27s

Generating Fibonacci
Generated Fibonacci of 9227465
Fibonacci: 1.68s

Total Execution Time: 19.08s
```

### Distributed System
```bash
Generating Fibonacci
Generated Fibonacci of 9227465
Performing matrix multiplication
Finished matrix multiplication
Calculating primes
Found 148933 primes
All workers finished

Execution Success: Fibonacci.py, Time: 1.71s
Execution Success: Matrix.py, Time: 0.30s
Execution Success: Prime.py, Time: 8.01s
Execution Time: 10.24s
Packaged into result.zip
Packaging Time: 0.00s

Total Execution Time: 10.24s
```

### Performance Gains
- **Total Execution Time (Individual Test): 19.08s**
- **Total Execution Time (Distributed System): 10.24s**

As seen from the test results, the distributed system achieves a **47% reduction in execution time**

## Potential Improvements & TODOs
The system, while improving execution time, can definitely be improved through various methods that I plan on experimenting on in the future such as:
**batch processing** for more complex tasks or **prioritizing tasks** so more time-sensitive tasks should be executed first.
