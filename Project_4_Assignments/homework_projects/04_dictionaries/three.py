from hashlib import sha256

def login(email, stored_logins, password_to_check):
    """
    Returns True if the hash of the password we are checking matches the one in stored_logins
    for a specific email. Otherwise, returns False.

    email: the email we are checking the password for
    stored_logins: a dictionary pointing from an email to its hashed password
    password_to_check: a password we want to test alongside the email to login with
    """
    # Compare the hashed password of the entered password to the stored hash
    if stored_logins[email] == hash_password(password_to_check):
        return True
    return False

def hash_password(password):
    """
    Takes in a password and returns the SHA256 hashed value for that specific password.
    
    Inputs:
        password: the password we want
    
    Outputs:
        the hashed form of the input password
    """
    # Return the SHA256 hash of the password
    return sha256(password.encode()).hexdigest()

def main():
    # stored_logins is a dictionary with emails as keys and hashed passwords as values
    stored_logins = {
        "example@gmail.com": "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8",  # Hash for 'password'
        "code_in_placer@cip.org": "973607a4ae7b4cf7d96a100b0fb07e8519cc4f70441d41214a9f811577bb06cc",  # Hash for 'Karel'
        "student@stanford.edu": "882c6df720fd99f5eebb1581a1cf975625cea8a160283011c0b9512bb56c95fb"  # Hash for 'password'
    }
    
    # Test cases
    print(login("example@gmail.com", stored_logins, "word"))  # False
    print(login("example@gmail.com", stored_logins, "password"))  # True
    
    print(login("code_in_placer@cip.org", stored_logins, "Karel"))  # True
    print(login("code_in_placer@cip.org", stored_logins, "karel"))  # False
    
    print(login("student@stanford.edu", stored_logins, "password"))  # True
    print(login("student@stanford.edu", stored_logins, "123!456?789"))  # False

# Python boilerplate
if __name__ == '__main__':
    main()
