class UserDomain:
    """User domain class"""
    gmail_domain_user=0
    yahoo_domain_user=0
    @staticmethod
    def user_input():
        """User input"""
        user_name=input("Enter user email address: ")
        return user_name
    @staticmethod
    def dmain_finder(user_name):
        """splitting user email address with @"""
        user_name,user_domain_name=user_name.split('@')
        user_domain_name,split_dot=user_domain_name.split('.')

        return user_name,user_domain_name,split_dot
    
    @staticmethod
    def add_user(user_domain_name):
        """adding users depening on domains"""
       

        if "gmail" in user_domain_name:
            
            UserDomain.gmail_domain_user= UserDomain.gmail_domain_user + 1
            return UserDomain.gmail_domain_user
            
        elif "yahoo" in user_domain_name:
            
            UserDomain.yahoo_domain_user=UserDomain.yahoo_domain_user+1
            return UserDomain.yahoo_domain_user
        else:
            return False
    @staticmethod
    def main():
        
        user1=UserDomain.user_input()
        user_domain_name=UserDomain.dmain_finder(user1)
        domain_users=UserDomain.add_user(user_domain_name)
        user2=UserDomain.user_input()
        user_domain_name=UserDomain.dmain_finder(user2)
        domain_users=UserDomain.add_user(user_domain_name)
        user3=UserDomain.user_input()
        user_domain_name=UserDomain.dmain_finder(user3)
        domain_users=UserDomain.add_user(user_domain_name)
        user4=UserDomain.user_input()
        user_domain_name=UserDomain.dmain_finder(user4)
        domain_users=UserDomain.add_user(user_domain_name)
        print(f"Gmail users: {UserDomain.gmail_domain_user}")
        print(f"Yahoo users: {UserDomain.yahoo_domain_user}")
        
UserDomain.main()
        
        