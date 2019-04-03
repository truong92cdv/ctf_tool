# from Crypto.Util.number import bytes_to_long, long_to_bytes
from Crypto.PublicKey import RSA
from SECRETS import FLAG

sk = RSA.generate(1024)
pk = sk.publickey()
flag = FLAG
enc_flag = pk.encrypt(flag, 0)[0].encode('hex')

LIMIT = 450

while LIMIT > 0:
    print '1. Encrypt' 
    print '2. Decrypt'
    print '3. Get Flag'
    choice = int(raw_input(('What do you want to do: ')))
    LIMIT -= 1
    if choice == 1:
        ptxt = raw_input('Enter the message: ')
        ctxt = pk.encrypt(ptxt, 0)[0].encode('hex')
        print 'Ciphertext: ' + ctxt
    elif choice == 2:
        ctxt = raw_input('Enter the ciphertext: ')
        try:
            b = sk.decrypt(int(ctxt, 16))
            if b%2 == 0:
                print 'I like it!'
            else:
                print 'I hate it!'
        except:
            print 'Invalid ctxt!'
    elif choice == 3:
        print enc_flag
    else:
        break
