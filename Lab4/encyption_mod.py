# Importing hashlib module
"""
hashlib is used to encrypt the  messages using different algorithms

"""
import hashlib

# Function to return hash code of a password
def hash_function(pwd, algo):
    # Encoding pwd
    data = pwd.encode('utf-8')
    # Based on the algo generating hash code
    if algo == 'md5':
        hashed = hashlib.md5(data)
    elif algo == 'sha512':
        hashed = hashlib.sha224(data)
    elif algo == 'sha256':
        hashed = hashlib.sha256(data)
    # Adding salt at the end of hash code that is in hexdecimal form
    result = hashed.hexdigest()
    # Returning hash code
    return result

# Mian function
def main():

    # List with hashing algorithms
    hash_list = ["md5","sha256", "sha512"]
    # User inputs a string
    user_pwd = input()
    # Loop over hash_list
    for hash_algorithm in hash_list:
        # Function call to hash code
        hashed_pwd = hash_function(user_pwd, hash_algorithm)
        # Printing the result
        print("Testing hash algorithm:", hash_algorithm)
        print("Hashed Password =",str(hashed_pwd)+'\n')
# Function call main
main()
