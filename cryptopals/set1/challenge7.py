from base64 import b64decode
from Crypto.Cipher import AES

def aes_ecb_decrypt(data, key):
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.decrypt(data)

def main():
    with open("challenge7.txt") as input_file:
        binary_data = b64decode(input_file.read())

    print(aes_ecb_decrypt(binary_data, 'YELLOW SUBMARINE').decode().rstrip())


if __name__ == "__main__":
    main()
