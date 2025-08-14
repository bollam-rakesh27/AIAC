def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_primes_in_range(start, end):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

def main():
    start = int(input("Enter start of range: "))
    end = int(input("Enter end of range: "))
    primes = get_primes_in_range(start, end)
    print("Prime numbers:", ','.join(str(p) for p in primes))

if __name__ == "__main__":
    main()