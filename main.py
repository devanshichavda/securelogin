import hashlib
#allows access to hashing algorithms like SHA256
import os

def create_hash(password):
  #function for hashing password
  return hashlib.sha256(password.encode()).hexdigest()

