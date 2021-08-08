import sys;
import hashlib;
import secrets;

if( len(sys.argv) == 1 ):
    print('At least one parameter required');
    exit();

password=sys.argv[1];
salt=secrets.token_bytes();

passwordhash = hashlib.pbkdf2_hmac('sha512', bytes(password, 'utf-8'), salt, 200000);

print(passwordhash.hex());