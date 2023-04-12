import utils


def decrypt(message: str, private_key: (int, int), encoding='utf-8') -> str:
    chunks = message.split(utils.ENCRYPTION_SEPARATOR)
    decoded_str = ""
    for chunk in chunks:
        decoded_val = pow(int(chunk), private_key[0], private_key[1])
        decoded_str += decoded_val.to_bytes(utils.WINDOW, utils.ENCRYPTION_BYTEORDER).decode(encoding).strip(
            utils.FILL_VALUE)
    return decoded_str


if __name__ == "__main__":
    decrypt(
        '481887059449271419350561756627779003559804063175731861754592-927633000975033181585366077126208370153027551075419758523954-848445381453624122389594762592408580952121916253551390008937-790287107035045125171289256677658161898559318623550646969685',
        (430608025730870179913987100829040115807280567683278322690773,
         1024105259473512494554749771370863434575707139134703687727821))
