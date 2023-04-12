import argparse
import utils
import key_manager
import enctyptor
import decryptor

parser = argparse.ArgumentParser(
    prog=utils.get_prog_name(),
    description=utils.get_description(),
    epilog=utils.get_epilog(),
)

parser.add_argument('command', choices=['generate_keys', 'encrypt', 'decrypt'],
                    help='A command that you want to execute')

# common arguments
parser.add_argument('-u', '--public_key_filename', type=str,
                    help='File, where to store public key. If not provided, public key is printing in stdout')
parser.add_argument('-r', '--private_key_filename', type=str,
                    help='File, where to store private key. If not provided, private key is printing in stdout')

# generate_key arguments
parser.add_argument('-n', '--n_bits', type=int, default=1024, help='Number of bits in each of generated primes.')

# encrypt/decrypt arguments
parser.add_argument('-m', '--original_message_filename', type=str, help='A file to encrypt. Supported formats: .txt')
parser.add_argument('-e', '--encrypted_message_filename', type=str, help='A file to decrypt. Supported formats: .txt')
parser.add_argument('-d', '--decrypted_message_filename', type=str,
                    help='A file with decrypted message. Supported formats.txt')

if __name__ == '__main__':
    args = parser.parse_args()
    if args.command == 'generate_keys':
        if args.n_bits < utils.MIN_N_BITS:
            print(f'The number of bits should be at least {utils.MIN_N_BITS}')
            exit(1)
        private_key, public_key = key_manager.generate_keys(args.n_bits)
        key_manager.output_keys(private_key, public_key, args.public_key_filename, args.private_key_filename)
    elif args.command == 'encrypt':
        public_key = key_manager.parse_key(key_manager.input_public_key(args.public_key_filename))
        message = utils.input_original_message(args.original_message_filename)

        utils.output_message('Encrypted', enctyptor.encrypt(message, public_key), args.encrypted_message_filename)
    elif args.command == 'decrypt':
        private_key = key_manager.parse_key(key_manager.input_private_key(args.private_key_filename))
        message = utils.input_encrypted_message(args.encrypted_message_filename)

        utils.output_message('Decrypted', decryptor.decrypt(message, private_key), args.decrypted_message_filename)
    else:
        print(f'Unknown command: {args.command}')
