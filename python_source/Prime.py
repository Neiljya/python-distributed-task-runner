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
    print("Calculating primes")
    primes = calculate_primes(2000000)
    print(f"Found {len(primes)} primes")
