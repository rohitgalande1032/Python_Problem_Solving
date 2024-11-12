# check given number is prime or not
def checkPrime(number):
    for i in range(2, number):
        if number%i == 0:
            return False
    return True


# Print all Primes upto given Numbers
def find_prime_upto_n(number):
    prime_list = []
    # Check each number from 2 up to n
    for num in range(2, number+1):
        isPrime = True # Assume number is prime

        # Check divisors up to the square root of num
        for i in range(2, int(num**0.5)+1):
            if num%i == 0:
                isPrime = False
                break

        # If no divisors were found, num is prime
        if isPrime:
            prime_list.append(num)

    return prime_list


# Print all Primes from given Range
def primes_from_range(start, end):
    primes = []
    for num in range(start, end):
        isPrime = True

        for i in range(2, int(num**0.5)+1):
            if num%i == 0:
                isPrime = False
                break
        
        if isPrime:
            primes.append(num)

    return primes

if __name__ == "__main__":
    number = 30
    print("Prime" if checkPrime(number) else "Not Prime")

    # Print all Primes upto given Numbers
    print(f"List of all prin=mes upto {number} = {find_prime_upto_n(number)}")

    #Print all primes from given range
    print("All primes from given range: ", primes_from_range(10, 50))
