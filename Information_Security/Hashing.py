import sys;
import hashlib;

if( len(sys.argv) == 1 ):
    print('At least one parameter required');
    exit();

password=sys.argv[1];

passwordhash = hashlib.pbkdf2_hmac('sha512', bytes(password, 'utf-8'), b'Km5d5ivMy8iexuHcZrsD', 200000);

print(passwordhash.hex());