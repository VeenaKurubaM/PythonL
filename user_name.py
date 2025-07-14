class user_name_valid:
    """Validate Username class"""
    @staticmethod
    def user_name_accept():
        """ Enter user name"""
        user_name=input("Enter user name less than 12 chars: ")
        return user_name
    @staticmethod
    def user_name_validations(user_name):
        """ User name validations"""
        if len(user_name) > 12:
            print("User name should be max 12 letters")
            user_name_valid.main()
        elif not user_name.isalpha():
            print("User name should only contains alphabets")
            user_name_valid.main()
        else:
            print("User name is valid")
    @staticmethod
    def main():
        """Main method"""
        user_name_input=user_name_valid.user_name_accept()
        user_name_validation=user_name_valid.user_name_validations(user_name_input)
        return user_name_validation
user_name_valid.main()
        
    
        
    