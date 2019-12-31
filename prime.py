import argparse
import os
import shutil
import yaml

base_dir = os.getcwd()
join = os.path.join
exists = os.path.exists


def main(n):
    primes = calculate_primes(n)
    write_result(primes)


def write_result(primes):
    result_folder = join(base_dir, 'result')
    if exists(result_folder):
        shutil.rmtree(result_folder)
    os.makedirs(result_folder)
    result_file = join(result_folder, 'primes')

    with open(result_file, 'w') as result:
        result.write(yaml.dump(primes, default_flow_style=True))


def calculate_primes(n):
    eliminated = [False for i in range(0, n+1)]
    primes = [0 for i in range(0, n+1)]
    i = 0

    for number in range(2,n+1):
        if not eliminated[number]:
            primes[i] = number
            i += 1
        last_prime = 0
        compound_number = 0
        for j in range(0, i):
            current_prime = primes[j]
            additions_to_do = current_prime - last_prime
            last_prime = primes[j]
            for k in range(0, additions_to_do):
                compound_number += number
            if compound_number > n:
                break
            eliminated[compound_number] = True
            if number % current_prime == 0:
                break

    primes = primes[0:i]
    return primes


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Calculate all primes up to and including n")
    parser.add_argument('n', type=int)
    args = parser.parse_args()
    n = args.n
    main(n)