# fibonacci.py

def fib():
    fibs = [1, 2]

    for i in range(1,9):
        # implement Fibonacci sequence to calculate the first 10 Fibonacci numbers, note Fn = Fn-1 + Fn-2

        next_fib = fibs[i] + fibs[i-1]
        fibs.append(next_fib)

    return fibs

def main():
    print(fib())

if __name__ == "__main__":
    main()
