def get_int(start_message, error_message, end_message):
    flag = True
    try:
        print(start_message)
        a = input()
        a = int(a)
    except ValueError:
        while flag:
            print(error_message)
            a = input()
            try:
                a = int(a)
            except ValueError:
                continue
            else:
                print(end_message)
                return a
    else:
        print(end_message)
        return a
x = get_int('Input int number:', 'Wrong value. Input int number:', 'Thank you.')
