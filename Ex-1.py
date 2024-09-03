def fib_sequence_until(n):

    fib_sequence = [0,1]
    while fib_sequence[-1] < n:
        next_value = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_value)

    return fib_sequence


def main():
    num = int(input("Insira um número: "))

    fib_sequence = fib_sequence_until(num)

    if num in fib_sequence:
        print(f"O número {num} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {num} não pertence à sequência de Fibonacci.")
        
main()