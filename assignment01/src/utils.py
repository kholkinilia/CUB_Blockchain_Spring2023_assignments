def get_string_from_file(filename):
    with open(filename, 'r') as file:
        return ''.join(file.readlines())


def get_description():
    return "DESCRIPTION: The implementation of RSA algorithm."


def get_prog_name():
    return "python3 rsa.py"


def get_epilog():
    return ""


def input_message(command_type, message_filename=None):
    if message_filename:
        with open(message_filename, 'r') as file:
            return ''.join(file.readlines())

    print(f'Please input one-line message to {command_type}')
    return input()


def input_encrypted_message(encrypted_message_filename=None):
    return input_message('decrypt', encrypted_message_filename)


def input_original_message(original_message_filename=None):
    return input_message('encrypt', original_message_filename)


def output_message(message_type: str, message: str, message_filename=None):
    try:
        with open(message_filename, 'w') as file:
            file.write(message)
    except (TypeError, FileNotFoundError):
        print(f'{message_type} message:\n{message}')


WINDOW = 20
MIN_N_BITS = WINDOW * 5
FILL_VALUE = '\0'
ENCRYPTION_SEPARATOR = '-'
ENCRYPTION_BYTEORDER = 'little'
