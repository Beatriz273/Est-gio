def main():

    user_input = input("Insira uma string: ")
    new_string = ''
    for char in user_input[::-1]:
        new_string += char

    print (new_string)

main()