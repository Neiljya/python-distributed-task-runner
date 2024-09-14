import time
import numpy as np

def matrix_multiplication(size):
    A = np.random.rand(size, size)
    B = np.random.rand(size, size)
    result = np.dot(A, B)
    return result

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Prime number calculation function
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def calculate_primes(limit):
    primes = []
    for num in range(2, limit):
        if is_prime(num):
            primes.append(num)
    return primes

if __name__ == "__main__":
    # Track time for each task

    # Prime number calculation
    start_time = time.time()
    print("Calculating primes")
    primes = calculate_primes(2000000)
    print(f"Found {len(primes)} primes")
    prime_time = time.time() - start_time
    print(f"Prime: {prime_time:.2f}s\n")

    # Matrix multiplication
    start_time = time.time()
    print("Performing matrix multiplication")
    result = matrix_multiplication(10000)
    print("Finished matrix multiplication")
    matrix_time = time.time() - start_time
    print(f"Matrix: {matrix_time:.2f}s\n")

    # Fibonacci sequence generation
    start_time = time.time()
    print("Generating Fibonacci")
    fib_sequence = fibonacci(35)
    print(f"Generated Fibonacci of {fib_sequence}")
    fib_time = time.time() - start_time
    print(f"Fibonacci: {fib_time:.2f}s\n")

    # Total time
    total_time = prime_time + matrix_time + fib_time
    print(f"Total Execution Time: {total_time:.2f}s")

