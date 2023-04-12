import utils


def encrypt(message: str, public_key: (int, int), encoding='utf-8') -> str:
    # matching the lengths of the message to be divisible by `utils.WINDOW`
    if len(message) % utils.WINDOW != 0:
        message += utils.FILL_VALUE * (utils.WINDOW - len(message) % utils.WINDOW)

    # encrypting each chunk of size `utils.WINDOW`
    encrypted_str = []
    for i in range(len(message) // utils.WINDOW):
        cur_val = int.from_bytes(bytearray(message[i * utils.WINDOW:(i + 1) * utils.WINDOW], encoding),
                                 utils.ENCRYPTION_BYTEORDER)
        encrypted_str.append(str(pow(cur_val, public_key[0], public_key[1])))

    return f'{utils.ENCRYPTION_SEPARATOR}'.join(encrypted_str)


if __name__ == "__main__":
    print(encrypt('Some text in here should be rather long and hard to fit in 20 window.', (
        324398059060481119117097153724227552399034453955994033899937,
        1024105259473512494554749771370863434575707139134703687727821)))
