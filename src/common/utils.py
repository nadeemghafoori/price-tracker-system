from passlib.hash import pbkdf2_sha512
import re

def has_number(inpt):
    return any(char.isdigit() for char in inpt)

class Utils(object):

    @staticmethod
    def email_is_valid(email):
        afterAt = email.split("@")[-1]                                          # email_address_matcher = re.compile('^[\w-]+@([\w-]+\.)+[\w]+$')
        remaining = afterAt.split('.')                                          # # return True if email_address_matcher.match(email) else False

        if len(remaining) == 2 and not has_number(remaining):
            print("hello from .com")
            return True
        elif len(remaining) == 3 and not has_number(remaining):
            return True
        else:
            return False

    @staticmethod
    def hash_password(password):        # double encryption 'the password which is coming from user is sha512' and 'it will be enrypted using pbkdf2_sha512'
        """
        Hashes a password using pbkdf2_sha512
        :param password: The sha512 password from the login/register form
        :return: A sha512->pbkdf2_sha512 encrypted password
        """
        return pbkdf2_sha512.encrypt(password)

    @staticmethod
    def check_hashed_password(password, hashed_password):
        """
        Checks that the password the user sent matches that of the database.
        The database password is encrypted more than the user's password at this stage.
        :param password: sha512-hashed password
        :param hashed_password: pbkdf2_sha512 encrypted password
        :return: True is password match, False otherwise
        """
        return pbkdf2_sha512.verify(password, hashed_password)