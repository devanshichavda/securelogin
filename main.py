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
  save_new_user(username, password_hash)
  print("You're now registered!")

def login():
  #enter username and password and check if values correspond
  print("Login")
  username = input("Enter username: ")
  password = input("Enter password: ")

  stored_hash = get_stored_info(username)
  if stored_hash:
    if create_hash(password) == stored_hash:
      print('Login Successful.')
      return True
    else:
      print("Incorrect Password.")
      return False
  else:
    print("Username not found. Please register.")
    return False

def main():
  while True:
    print("\n1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter your choice (1-3):")

    if choice == '1':
      register()
    elif choice == '2':
      login()
    elif choice == '3':
      print("Bye!")
      break
    else:
      print('Invalid.')
main()