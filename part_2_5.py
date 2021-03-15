"""
Write some code to print the SHA256 hash of the string "This is a string"
"""
from hashlib import sha256

s = "This is a string"

# Your code goes here

def string_hash(s: str):
    return sha256(s.encode('utf-8')).hexdigest()

print(string_hash(s))
