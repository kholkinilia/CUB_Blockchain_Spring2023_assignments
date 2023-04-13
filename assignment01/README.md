# Assignment 1: RSA implementation.

## How to use

Here is the help message of the script:

```
usage: python3 rsa.py [-h] [-u PUBLIC_KEY_FILENAME] [-r PRIVATE_KEY_FILENAME] [-n N_BITS] [-m ORIGINAL_MESSAGE_FILENAME] [-e ENCRYPTED_MESSAGE_FILENAME]
                      [-d DECRYPTED_MESSAGE_FILENAME]
                      {generate_keys,encrypt,decrypt}

DESCRIPTION: The implementation of RSA algorithm.

positional arguments:
  {generate_keys,encrypt,decrypt}
                        A command that you want to execute

optional arguments:
  -h, --help            show this help message and exit
  -u PUBLIC_KEY_FILENAME, --public_key_filename PUBLIC_KEY_FILENAME
                        File, where to store public key. If not provided, public key is printed in stdout
  -r PRIVATE_KEY_FILENAME, --private_key_filename PRIVATE_KEY_FILENAME
                        File, where to store private key. If not provided, private key is printed in stdout
  -n N_BITS, --n_bits N_BITS
                        Number of bits in each of generated primes.
  -m ORIGINAL_MESSAGE_FILENAME, --original_message_filename ORIGINAL_MESSAGE_FILENAME
                        A file to encrypt. Supported formats: .txt
  -e ENCRYPTED_MESSAGE_FILENAME, --encrypted_message_filename ENCRYPTED_MESSAGE_FILENAME
                        A file to decrypt. Supported formats: .txt
  -d DECRYPTED_MESSAGE_FILENAME, --decrypted_message_filename DECRYPTED_MESSAGE_FILENAME
                        A file with decrypted message. Supported formats.txt
```

Providing files is not necessary. If you don't provide necessary information, you will be asked to input it manually (by
stdin).

## Example of usage

You can run the following code yourself. The code operates on a message, at which you can take a look in
the `./resources/examples/original_message.txt`.

Run the following code from this (`assignment01` directory)

```shell
# generate keys and save them in pub.txt and priv.txt
python3 src/rsa.py generate_keys -u ./resources/examples/keys/pub.txt -r ./resources/examples/keys/priv.txt
# encrypt the original_message.txt using pub.txt as a public key and save the encryption to encrypted_message.txt
python3 src/rsa.py encrypt -u ./resources/examples/keys/pub.txt -m ./resources/examples/messages/original_message.txt -e ./resources/examples/messages/encrypted_message.txt
# decrypt the encrypted_message.txt using priv.txt as a private key and save the decryption to decrypted_message.txt
python3 src/rsa.py decrypt -r ./resources/examples/keys/priv.txt -d ./resources/examples/messages/decrypted_message.txt -e ./resources/examples/messages/encrypted_message.txt
# check if the result and the original message are the same
diff ./resources/examples/messages/decrypted_message.txt ./resources/examples/messages/original_message.txt
```

## Limitations

* The encryption is implemented with sliding window and the message is getting appended with `\0` bytes so that its
  length is divisible by the window size. Therefore, the decoder strips `\0` bytes. So, a message containing `\0` bytes
  may be decrypted wrongly.
* The encryptor/decryptor may not work with non-ASCII characters.
* The number of bits in the key-numbers should be at least 100. The reason is that the length of the window is fixed and the window size should be smaller than the key bits to avoid collisions. (presumably)
