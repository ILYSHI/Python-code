def get_int(start_message, error_message, end_message):
    print(start_message)
    while True:
        try:
            a = input()
            a = int(a)
            print(end_message)
            return a
        except ValueError:
            print(error_message)


x = get_int('Input int number:', 'Wrong value. Input int number:', 'Thank you.')
