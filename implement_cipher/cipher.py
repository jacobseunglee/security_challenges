# Implement a cipher
# Convert text to ciphertext and vice versa
import sys
import codecs

def encrypt(string: str) -> str:
    ciphertext = []
    for char in string:
        unicode = r'\U000{:05X}'.format(ord(char) + 129295)
        ciphertext.append(codecs.decode(unicode, 'unicode-escape'))
    return ''.join(ciphertext)    
        

def decrypt(ciphertext: str) -> str:
    string = []
    for char in ciphertext:
        hex = codecs.encode(char,'unicode-escape').decode()[5:]
        unicode = r'\U000{:05X}'.format(int(hex, 16) - 129295)
        string.append(codecs.decode(unicode, 'unicode-escape'))
    return ''.join(string)

if __name__ == "__main__":
    usage_message = '''usage: cipher.py MESSAGE\n
Script to encrypt or decrypt text. Defaults to encryption.\n
optional arguments:
-e, --encrypt Encrypt MESSAGE
-d, --decrypt Decrypt MESSAGE
-h, --help    Show this message and exit
'''
    if sys.argv[1] in ("-h", "--help"):
        print(f"Help Menu\n{usage_message}")
        exit()
    if len(sys.argv) > 2:
        option = sys.argv[1]
        string = sys.argv[2]
    else:
        option = "-e"
        string = sys.argv[1]
    if option in ("-e", "--encrypt"):
        print(encrypt(string))
    elif option in ("-d", "--decrypt"):
        print(decrypt(string))
    else:
        print(f"Unknown option {option}\n{usage_message}")