def main():
    user_input = input("Insira uma string: ")

    count_a = 0

    for char in user_input.lower():
        if char == 'a':
            count_a += 1
    if count_a > 0:
        print(f"A letra 'a' aparece {count_a} vezes na string.")
    else:
        print("A letra 'a' não aparece na string.")

main()