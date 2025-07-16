class user_name:
    """user class"""
    @staticmethod
    def email_address(email):
        """email addree"""
        email_address=email.strip()
        user_name,email_domain=email_address.split("@")
        return user_name,email_domain

    @staticmethod
    def main():
        """splitting domain and user name"""
        user_email,email_domain=user_name.email_address(input("Enter email address: "))
        print(f"User Name is :{user_email} and domain is :{email_domain}" )
user_name.main()



