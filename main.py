import hashlib
#allows access to hashing algorithms like SHA256
import os

def create_hash(password):
  #function for hashing password
  return hashlib.sha256(password.encode()).hexdigest()

def save_new_user(username, password_hash):
  #writes newly registered user login information to file
  with open('logins.txt', 'a') as file:
    file.write(f"{username}:{password_hash}\n")

def get_stored_info(username):
  #checks if stored username in text file matches inputted username
  try:
    with open('logins.txt', 'r') as file:
      for line in file:
        stored_username, stored_hash = line.strip().split(':')
        if stored_username == username:
          return stored_hash
  except FileNotFoundError:
    return None
  return None

def register():
  print("Registration")
  username = input("Enter a username: ")
  password = input("Enter a password: ")

  if get_stored_info(username):
    print("Username already exists.")
    return

  password_hash = create_hash(password)


